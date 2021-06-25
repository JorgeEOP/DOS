from pandas import DataFrame as df
from numpy import zeros
import pandas as pd
import numpy as np
import funcpot
import yaml
import sys
import os

#####################################################################
##  Plot Total DOS and Projected DOS per atom for specific orbital ## 
#####################################################################
#har2eV = phys.physical_constants["Hartree energy in eV"][0]
har2eV = 27.211386245988 

class projected_dos:
    def __init__(self,config):
        self.Name        = config["Name of the system"]
        self.Nelements   = config["Number of elements in the system"]
        self.Spin        = config["Spin Polarized system"]
        self.PDOS        = config["Name of PDOS"]
        self.p_in        = config["Path to Input"]
        self.p_out       = config["Path to Output"]
        self.PDOS_alpha  = config["Name of PDOS alpha"]
        self.PDOS_beta   = config["Name of PDOS beta"]
        self.sigma       = config["Gaussian Parameters"][0]["Standard deviation"]
        self.points      = config["Gaussian Parameters"][1]["Points"]
        self.MO          = config["Gaussian Parameters"][2]["MO"]
        self.eigenval    = config["Gaussian Parameters"][2]["Eigenval"]
        self.ocuppation  = config["Gaussian Parameters"][2]["Occupation"]
        self.s_orbit     = config["Gaussian Parameters"][2]["s-Orbitals"]

    def generate_pdos(self): 
        if self.Spin in ["No","no","N","n"]:
            Ef = []
            for i in [self.PDOS]:
                Ef += funcpot.getEf(i, har2eV)
            print ('Fermi energy [eV]: ', Ef[0])
            
            tot_eigen  = funcpot.read_files_general(self.PDOS, self.eigenval, self.eigenval, 2)
            totE_diff  = [x*har2eV for x in tot_eigen]
            Tdos       = zeros(self.points)
            
            ab1        = zeros(self.points, dtype=[('var1', float), ('var2', float), ('var3', float)])
            
            Peig_C     = funcpot.read_files_general(self.Name+"-k1-1.pdos", self.s_orbit, self.d_orbit, 2)
            orbital_C  = [sum(x) for x in zip(*Peig_alpha_C)]
            Pdos_C     = zeros(self.points)
            with open(funcpot.unique_file(self.Name + '_T-PDOS', 'dat', 2), 'wb') as f1:
                for x in totE_diff:
                    Tdos    += funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)
                for x, w in zip(totE_diff, orbital_C):
                    Pdos_C  += w*funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)
                
                ab1['var1']   =  energies
                ab1['var2']   =  Tdos
                ab1['var3']   =  Pdos_C
                np.savetxt(f1, ab1, fmt=('%4.6f', '%4.6f','%4.6f'))

        elif self.Spin in ["Yes","yes","Y","y"]:

            Ef = []

            alpha_f = os.path.join(self.p_in, self.PDOS_alpha)
            beta_f  = os.path.join(self.p_in, self.PDOS_beta)
            for i in [alpha_f, beta_f]:
                Ef += funcpot.getEf(i, har2eV)
            print ('Fermi energy alpha [eV]: ', Ef[0], '\nFermi energy beta [eV]: ', Ef[1])
        
            tot_eigen_alpha   =  funcpot.read_files_general(alpha_f, self.eigenval, self.eigenval, 2)
            totE_diff_alpha   =  [x*har2eV for x in tot_eigen_alpha]
            Tdos_alpha        =  np.zeros(self.points)
            
            tot_eigen_beta    =  funcpot.read_files_general(beta_f, self.eigenval, self.eigenval, 2)
            totE_diff_beta    =  [x*har2eV for x in tot_eigen_beta]
            Tdos_beta         =  np.zeros(self.points)
           
            energies_a  =  np.linspace(min(totE_diff_alpha), max(totE_diff_alpha), self.points)
            energies_b  =  np.linspace(min(totE_diff_beta), max(totE_diff_beta), self.points)
            min_e_a     =  min(energies_a)
            max_e_a     =  max(energies_a)
            min_e_b     =  min(energies_b)
            max_e_b     =  max(energies_b)
            min_e       =  min(min_e_a, min_e_b) + 4*self.sigma
            max_e       =  max(max_e_a, max_e_b) + 4*self.sigma
            energies    =  np.linspace(min_e, max_e, self.points)
            dos_total   =  np.zeros(self.points)

            Peigs_dic    = {}
            orbitals_dic = {}
            Pdos_dic     = {}
            All_daten    = {}
            
            nelements = int(self.Nelements)
            for iel in range(1,nelements+1):
                for spin in ['ALPHA', 'BETA']:
                    cols = funcpot.read_count(os.path.join(
                                              self.p_in, self.Name) + "-" +
                                              spin + "_k" + str(iel) + "-1.pdos",
                                              2)

                    Peigs_dic[str(spin)+"_k"+str(iel)] = funcpot.read_files_general(
                                            os.path.join(self.p_in, self.Name) +
                                            "-" + spin + "_k" + str(iel) + "-1.pdos",
                                            self.s_orbit, cols, 2)

                    orbitals_dic[str(spin)+"_k"+str(iel)] = [sum(x) for x in
                                       zip(*Peigs_dic[str(spin)+"_k"+str(iel)])]

                    Pdos_dic[str(spin)+"_k"+str(iel)] = np.zeros(self.points)

                    for x, w in zip(totE_diff_alpha,
                                    orbitals_dic[str(spin)+"_k"+str(iel)]):
                        Pdos_dic[str(spin)+"_k"+str(iel)] += w*funcpot.gaussian(min_e,
                                                                           max_e, x,
                                                                           self.sigma,
                                                                           self.points)

                    if spin == 'ALPHA':
                        for x in totE_diff_alpha:
                            Tdos_alpha +=  funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)
                    if spin == 'BETA':
                        for x in totE_diff_beta:
                            Tdos_beta +=  funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)

            # (-1,1) stellt fuer: -1 zu viele Reihe wie Noetig. 1 Spalte
            dos_total  = funcpot.tot_dens(Tdos_alpha, Tdos_beta)
            Tdos_alpha = Tdos_alpha.reshape((-1,1))
            Tdos_beta  = Tdos_beta.reshape((-1,1))

            All_daten = {'energies':energies, 'Tdos_alpha':Tdos_alpha,
                         'Tdos_beta':Tdos_beta, 'dos_total':np.asarray(dos_total)}
            All_daten.update(Pdos_dic)

            print (All_daten.keys())

            with open(funcpot.unique_file(self.p_out + self.Name + '-T-PDOS',
                                          'dat', 2), 'wb') as outstream:
                All_daten_df = df()
                for dos_key,pdos_val in All_daten.items():
                    All_daten_df = pd.concat([All_daten_df, df(pdos_val)], axis=1)
                np.savetxt(outstream, All_daten_df, fmt='%4.7f')

