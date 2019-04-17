import numpy as np
from numpy import asarray
from numpy import linspace
from numpy import zeros
from numpy import append
from funcpot import gaussian
from funcpot import unique_file
import math
import funcpot
import yaml

#####################################################################
##  Plot Total DOS and Projected DOS per atom for specific orbital ## 
#####################################################################

with open('ParamPdos.yaml', 'r') as ymlfile:
    inputval = yaml.load(ymlfile)

Hartree  =  inputval['Constants'][0]['Hartree']
sigma    =  inputval['Gaussian Parameters'][0]['Standard deviation']
points   =  inputval['Gaussian Parameters'][1]['Points']
ctr0  =  inputval['Gaussian Parameters'][2]['MO']

ctr1  =  inputval['Gaussian Parameters'][2]['Eigenval']
ctr2  =  inputval['Gaussian Parameters'][2]['s-Orbitals']
ctr3  =  inputval['Gaussian Parameters'][2]['p-Orbitals']
ctr4  =  inputval['Gaussian Parameters'][2]['d-Orbitals']
ctr5  =  inputval['Gaussian Parameters'][2]['f-3-Orbital']
ctr6  =  inputval['Gaussian Parameters'][2]['f+3-Orbital']
ctr7  =  inputval['Gaussian Parameters'][2]['g-Orbitals']

ab  =  zeros(points, dtype=[('var1', float), ('var2', float), ('var3', float), ('var4', float),\
           ('var5', float), ('var6', float), ('var7', float), ('var8', float), ('var9', float),\
        ('var10', float), ('var11', float), ('var12', float),('var13', float),('var14', float),\
        ('var15', float),('var16', float)])

e_fermi_alpha  =  funcpot.read_files('TbPc006DOS-ALPHA_k1-1.pdos', 0, 0, 2)
e_fermi_beta   =  funcpot.read_files('TbPc006DOS-BETA_k1-1.pdos', 0, 0, 2)

tot_eigen_alpha   =  funcpot.read_files_general('TbPc006DOS-ALPHA_k1-1.pdos', ctr1, ctr1, 2)
totE_diff_alpha   =  [x*Hartree for x in tot_eigen_alpha]
e_fermi_alpha_eV  =  e_fermi_alpha*Hartree
Tdos_alpha        =  zeros(points)

tot_eigen_beta    =  funcpot.read_files_general('TbPc006DOS-BETA_k1-1.pdos', ctr1, ctr1, 2)
totE_diff_beta    =  [x*Hartree for x in tot_eigen_beta]
e_fermi_beta_eV   =  e_fermi_beta*Hartree
Tdos_beta         =  zeros(points)

energies_a  =  linspace(min(totE_diff_alpha),max(totE_diff_alpha),points)
energies_b  =  linspace(min(totE_diff_beta),max(totE_diff_beta),points)
min_e_a     =  min(energies_a)
max_e_a     =  max(energies_a)
min_e_b     =  min(energies_b)
max_e_b     =  max(energies_b)
min_e       =  min(min_e_a,min_e_b) + 4*sigma
max_e       =  max(max_e_a,max_e_b) + 4*sigma
energies    =  linspace(min_e,max_e,points)
dos_total   =  zeros(points)

print ('Fermi energy alpha eV: ', e_fermi_alpha_eV, '\nFermi energy beta eV: ', e_fermi_beta_eV)

Peig_alpha_N    =  funcpot.read_files_general('TbPc006DOS-ALPHA_k1-1.pdos', ctr2, ctr4, 2)
Peig_alpha_C    =  funcpot.read_files_general('TbPc006DOS-ALPHA_k2-1.pdos', ctr2, ctr4, 2)
Peig_alpha_Tb   =  funcpot.read_files_general('TbPc006DOS-ALPHA_k3-1.pdos', ctr5, ctr6, 2)
Peig_alpha_Tb_S =  funcpot.read_files_general('TbPc006DOS-ALPHA_k3-1.pdos', ctr2, ctr7, 2)
Peig_alpha_H    =  funcpot.read_files_general('TbPc006DOS-ALPHA_k4-1.pdos', ctr2, ctr3, 2)
Peig_beta_N     =  funcpot.read_files_general('TbPc006DOS-BETA_k1-1.pdos', ctr2, ctr4, 2)
Peig_beta_C     =  funcpot.read_files_general('TbPc006DOS-BETA_k2-1.pdos', ctr2, ctr4, 2)
Peig_beta_Tb    =  funcpot.read_files_general('TbPc006DOS-BETA_k3-1.pdos', ctr5, ctr6, 2)
Peig_beta_Tb_S  =  funcpot.read_files_general('TbPc006DOS-BETA_k3-1.pdos', ctr2, ctr7, 2)
Peig_beta_H     =  funcpot.read_files_general('TbPc006DOS-BETA_k4-1.pdos', ctr2, ctr3, 2)

orbital_alpha_N     =  [sum(x) for x in zip(*Peig_alpha_N)]
orbital_alpha_C     =  [sum(x) for x in zip(*Peig_alpha_C)]
orbital_alpha_Tb    =  [sum(x) for x in zip(*Peig_alpha_Tb)]
orbital_alpha_Tb_S  =  [sum(x) for x in zip(*Peig_alpha_Tb_S)]
orbital_alpha_H     =  [sum(x) for x in zip(*Peig_alpha_H)]
orbital_beta_N      =  [sum(x) for x in zip(*Peig_beta_N)]
orbital_beta_C      =  [sum(x) for x in zip(*Peig_beta_C)]
orbital_beta_Tb     =  [sum(x) for x in zip(*Peig_beta_Tb)]
orbital_beta_Tb_S   =  [sum(x) for x in zip(*Peig_beta_Tb_S)]
orbital_beta_H      =  [sum(x) for x in zip(*Peig_beta_H)]

Pdos_alpha_N     =  zeros(points)
Pdos_alpha_C     =  zeros(points)
Pdos_alpha_Tb    =  zeros(points)
Pdos_alpha_Tb_S  =  zeros(points)
Pdos_alpha_H     =  zeros(points)
Pdos_beta_N      =  zeros(points)
Pdos_beta_C      =  zeros(points)
Pdos_beta_Tb     =  zeros(points)
Pdos_beta_Tb_S   =  zeros(points)
Pdos_beta_H      =  zeros(points)
electrons_4f     =  0
with open(unique_file('T_PDOS', 'dat', 2), 'wb') as f1:
    for x in totE_diff_alpha:
        Tdos_alpha      +=  gaussian(min_e, max_e, x, sigma, points)
    for y in totE_diff_beta:
        Tdos_beta       +=  gaussian(min_e, max_e, y, sigma, points)

    for x, w in zip(totE_diff_alpha, orbital_alpha_N):
        Pdos_alpha_N     +=  w*gaussian(min_e, max_e, x, sigma, points)
    for x, w in zip(totE_diff_alpha, orbital_alpha_C):
        Pdos_alpha_C     +=  w*gaussian(min_e, max_e, x, sigma, points)
    for x, w in zip(totE_diff_alpha, orbital_alpha_Tb):
        Pdos_alpha_Tb    +=  w*gaussian(min_e, max_e, x, sigma, points)
    electrons_4f      =  [sum(Pdos_alpha_Tb)]
    for x, w in zip(totE_diff_alpha, orbital_alpha_Tb_S):
        Pdos_alpha_Tb_S  +=  w*gaussian(min_e, max_e, x, sigma, points)
    for x, w in zip(totE_diff_alpha, orbital_alpha_H):
        Pdos_alpha_H     +=  w*gaussian(min_e, max_e, x, sigma, points)

    for y, z in zip(totE_diff_beta, orbital_beta_N):
        Pdos_beta_N     +=  z*gaussian(min_e, max_e, y, sigma, points)
    for y, z in zip(totE_diff_beta, orbital_beta_C):
        Pdos_beta_C     +=  z*gaussian(min_e, max_e, y, sigma, points)
    for y, z in zip(totE_diff_beta, orbital_beta_Tb):
        Pdos_beta_Tb    +=  z*gaussian(min_e, max_e, y, sigma, points)
    for y, z in zip(totE_diff_beta, orbital_beta_Tb_S):
        Pdos_beta_Tb_S  +=  z*gaussian(min_e, max_e, y, sigma, points)
    for y, z in zip(totE_diff_beta, orbital_beta_H):
        Pdos_beta_H     +=  z*gaussian(min_e, max_e, y, sigma, points)
     
    dos_total     =  funcpot.tot_dens(Tdos_alpha,Tdos_beta)
    Ligand_alpha  =  [xw1+xw2+xw3 for xw1, xw2, xw3 in zip(Pdos_alpha_N, Pdos_alpha_C, Pdos_alpha_H)]
    Ligand_beta   =  [xw1+xw2+xw3 for xw1, xw2, xw3 in zip(Pdos_beta_N, Pdos_beta_C, Pdos_beta_H)]

    ab['var1']   =  energies
    ab['var2']   =  Tdos_alpha
    ab['var3']   =  Tdos_beta
    ab['var4']   =  dos_total
    ab['var5']   =  Pdos_alpha_N
    ab['var6']   =  Pdos_alpha_C
    ab['var7']   =  Pdos_alpha_Tb
    ab['var8']   =  Pdos_alpha_H
    ab['var9']   =  Pdos_beta_N
    ab['var10']  =  Pdos_beta_C
    ab['var11']  =  Pdos_beta_Tb
    ab['var12']  =  Pdos_beta_H
    ab['var13']  =  Ligand_alpha
    ab['var14']  =  Ligand_beta
    ab['var15']  =  Pdos_alpha_Tb_S
    ab['var16']  =  Pdos_beta_Tb_S
    np.savetxt(f1, ab, fmt=('%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f',\
                             '%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f', '%4.6f'))

print (electrons_4f)
