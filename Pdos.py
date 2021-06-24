import numpy as np
import sys
import os
from numpy import asarray
from numpy import zeros
from numpy import append
#import scipy.constants as phys
import math
import funcpot
import yaml

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
        self.p_orbit     = config["Gaussian Parameters"][2]["p-Orbitals"]
        self.d_orbit     = config["Gaussian Parameters"][2]["d-Orbitals"]
        self.fm3_orbit   = config["Gaussian Parameters"][2]["f-3-Orbital"]
        self.fp3_orbit   = config["Gaussian Parameters"][2]["f+3-Orbital"]
        self.g_orbit     = config["Gaussian Parameters"][2]["g-Orbitals"]

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
            ab  =  zeros(self.points, dtype=[('var0', float),  ('var1', float),
                                             ('var2', float),  ('var3', float),
                                             ('var4', float),  ('var5', float),
                                             ('var6', float),  ('var7', float),
                                             ('var8', float),  ('var9', float),
                                             ('var10', float), ('var11', float),
                                             ('var12', float), ('var13', float)])
        
            Ef = []

            alpha_f = os.path.join(self.p_in, self.PDOS_alpha)
            beta_f  = os.path.join(self.p_in, self.PDOS_beta)
            for i in [alpha_f, beta_f]:
                Ef += funcpot.getEf(i, har2eV)
            print ('Fermi energy alpha [eV]: ', Ef[0], '\nFermi energy beta [eV]: ', Ef[1])
        
        
            tot_eigen_alpha   =  funcpot.read_files_general(alpha_f, self.eigenval, self.eigenval, 2)
            totE_diff_alpha   =  [x*har2eV for x in tot_eigen_alpha]
            Tdos_alpha        =  zeros(self.points)
            
            tot_eigen_beta    =  funcpot.read_files_general(beta_f, self.eigenval, self.eigenval, 2)
            totE_diff_beta    =  [x*har2eV for x in tot_eigen_beta]
            Tdos_beta         =  zeros(self.points)
           
            energies_a  =  np.linspace(min(totE_diff_alpha), max(totE_diff_alpha), self.points)
            energies_b  =  np.linspace(min(totE_diff_beta), max(totE_diff_beta), self.points)
            min_e_a     =  min(energies_a)
            max_e_a     =  max(energies_a)
            min_e_b     =  min(energies_b)
            max_e_b     =  max(energies_b)
            min_e       =  min(min_e_a, min_e_b) + 4*self.sigma
            max_e       =  max(max_e_a, max_e_b) + 4*self.sigma
            energies    =  np.linspace(min_e, max_e, self.points)
            dos_total   =  zeros(self.points)
            
            nelements = int(self.Nelements)
            print (nelements)
        
            Peig_alpha_Y    =  funcpot.read_files_general(os.path.join(self.p_in,self.Name) +
                                            "-ALPHA_k1-1.pdos", self.s_orbit,
                                            self.d_orbit, 2)
            Peig_alpha_N    =  funcpot.read_files_general(os.path.join(self.p_in,self.Name) +
                                            "-ALPHA_k2-1.pdos", self.s_orbit,
                                            self.d_orbit, 2)
            Peig_alpha_O   =  funcpot.read_files_general(os.path.join(self.p_in,self.Name) + 
                                            "-ALPHA_k3-1.pdos", self.s_orbit,
                                            self.d_orbit, 2)
            Peig_alpha_C =  funcpot.read_files_general(os.path.join(self.p_in,self.Name) +
                                            "-ALPHA_k4-1.pdos", self.s_orbit,
                                            self.d_orbit, 2)
            Peig_alpha_H    =  funcpot.read_files_general(os.path.join(self.p_in,self.Name) +
                                            "-ALPHA_k5-1.pdos", self.s_orbit,
                                            self.p_orbit, 2)

            Peig_beta_Y    =  funcpot.read_files_general(os.path.join(self.p_in,self.Name) +
                                            "-BETA_k1-1.pdos", self.s_orbit,
                                            self.d_orbit, 2)
            Peig_beta_N    =  funcpot.read_files_general(os.path.join(self.p_in,self.Name) +
                                            "-BETA_k2-1.pdos", self.s_orbit,
                                            self.d_orbit, 2)
            Peig_beta_O   =  funcpot.read_files_general(os.path.join(self.p_in,self.Name) + 
                                            "-BETA_k3-1.pdos", self.s_orbit,
                                            self.d_orbit, 2)
            Peig_beta_C =  funcpot.read_files_general(os.path.join(self.p_in,self.Name) +
                                            "-BETA_k4-1.pdos", self.s_orbit,
                                            self.d_orbit, 2)
            Peig_beta_H    =  funcpot.read_files_general(os.path.join(self.p_in,self.Name) +
                                            "-BETA_k5-1.pdos", self.s_orbit,
                                            self.p_orbit, 2)
       
            orbital_alpha_Y =  [sum(x) for x in zip(*Peig_alpha_Y)]
            orbital_alpha_N =  [sum(x) for x in zip(*Peig_alpha_N)]
            orbital_alpha_O =  [sum(x) for x in zip(*Peig_alpha_O)]
            orbital_alpha_C =  [sum(x) for x in zip(*Peig_alpha_C)]
            orbital_alpha_H =  [sum(x) for x in zip(*Peig_alpha_H)]
            orbital_beta_Y  =  [sum(x) for x in zip(*Peig_beta_Y)]
            orbital_beta_N  =  [sum(x) for x in zip(*Peig_beta_N)]
            orbital_beta_O  =  [sum(x) for x in zip(*Peig_beta_O)]
            orbital_beta_C  =  [sum(x) for x in zip(*Peig_beta_C)]
            orbital_beta_H  =  [sum(x) for x in zip(*Peig_beta_H)]
            
            Pdos_alpha_Y =  zeros(self.points)
            Pdos_alpha_N =  zeros(self.points)
            Pdos_alpha_O =  zeros(self.points)
            Pdos_alpha_C =  zeros(self.points)
            Pdos_alpha_H =  zeros(self.points)
            Pdos_beta_Y  =  zeros(self.points)
            Pdos_beta_N  =  zeros(self.points)
            Pdos_beta_O  =  zeros(self.points)
            Pdos_beta_C  =  zeros(self.points)
            Pdos_beta_H  =  zeros(self.points)
            electrons_4f =  0

            with open(funcpot.unique_file(self.p_out + self.Name + '_T-PDOS',
                                          'dat', 2), 'wb') as f1:
                for x in totE_diff_alpha:
                    Tdos_alpha      +=  funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)
                for y in totE_diff_beta:
                    Tdos_beta       +=  funcpot.gaussian(min_e, max_e, y, self.sigma, self.points)
            
                for x, w in zip(totE_diff_alpha, orbital_alpha_Y):
                    Pdos_alpha_Y     +=  w*funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)
                for x, w in zip(totE_diff_alpha, orbital_alpha_N):
                    Pdos_alpha_N     +=  w*funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)
                for x, w in zip(totE_diff_alpha, orbital_alpha_O):
                    Pdos_alpha_O  +=  w*funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)
                for x, w in zip(totE_diff_alpha, orbital_alpha_C):
                    Pdos_alpha_C  +=  w*funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)
                for x, w in zip(totE_diff_alpha, orbital_alpha_H):
                    Pdos_alpha_H  +=  w*funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)

                for x, w in zip(totE_diff_beta, orbital_beta_Y):
                    Pdos_beta_Y     +=  w*funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)
                for x, w in zip(totE_diff_beta, orbital_beta_N):
                    Pdos_beta_N     +=  w*funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)
                for x, w in zip(totE_diff_beta, orbital_beta_O):
                    Pdos_beta_O  +=  w*funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)
                for x, w in zip(totE_diff_beta, orbital_beta_C):
                    Pdos_beta_C  +=  w*funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)
                for x, w in zip(totE_diff_beta, orbital_beta_H):
                    Pdos_beta_H  +=  w*funcpot.gaussian(min_e, max_e, x, self.sigma, self.points)

                 
                dos_total     =  funcpot.tot_dens(Tdos_alpha,Tdos_beta)
            
                ab['var0']  =  energies
                ab['var1']  =  Tdos_alpha
                ab['var2']  =  Tdos_beta
                ab['var3']  =  dos_total
                ab['var4']  =  Pdos_alpha_Y
                ab['var5']  =  Pdos_alpha_N
                ab['var6']  =  Pdos_alpha_O
                ab['var7']  =  Pdos_alpha_C
                ab['var8']  =  Pdos_beta_H
                ab['var9']  =  Pdos_beta_Y
                ab['var10'] =  Pdos_beta_N
                ab['var11'] =  Pdos_beta_O
                ab['var12'] =  Pdos_beta_C
                ab['var13'] =  Pdos_beta_H
                #ab['var13']  =  Ligand_alpha
                #ab['var14']  =  Ligand_beta
                #ab['var15']  =  Pdos_alpha_Tb_S
                #ab['var16']  =  Pdos_beta_Tb_S
                np.savetxt(f1, ab, fmt=('%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f',\
                                         '%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f'))
