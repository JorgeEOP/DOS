import math
import numpy as np
import cmath
import itertools
import os

HBAR   = 1.05457e-34    #SI
ME     = 9.10938e-31    #SI 
CTE   = (2 * ME / (HBAR**2))
im    = np.complex(0,1)

#######################################################
#### Functions for the Barrier, D-Barrier problems ####
#######################################################

'''Wavevectors'''
def wk1(y):
    k1m = math.sqrt(CTE * y)
    return k1m

def wk2(y,V0):
    k2m = cmath.sqrt(CTE * (y - V0))
    return k2m

'''Matrices'''
  #Exponentials
def Matrix(z,x):
    Mat = np.array([[np.exp(z*x),np.exp(-z*x)],[z*np.exp(z*x),-z*np.exp(-z*x)]])
    return Mat
  #Linear
def MatrixLin(x):
    Mat = np.array([[1,x],[0,1]])
    return Mat

'''Pontentials'''
def steppot(i,x,V0):
    if i >= x:
        V = V0
        return V
    else:
        V = 0.0
        return V

def squarepot(i,x,V0):
    if i >= x and i <= x:
        V = V0
        return V
    else:
        V = 0.0
        return V

''' Thomas Algoritm function  '''
def TDMAsolver(a, b, c, d):
    nf = len(d) # number of equations
    ac, bc, cc, dc = map(np.array, (a, b, c, d)) # copy arrays
    for it in xrange(1, nf):
        mc = ac[it-1]/bc[it-1]
        bc[it] = bc[it] - mc*cc[it-1]
        dc[it] = dc[it] - mc*dc[it-1]

    xc = bc
    xc[-1] = dc[-1]/bc[-1]

    for il in xrange(nf-2, -1, -1):
        xc[il] = (dc[il]-cc[il]*xc[il+1])/bc[il]

    return xc

########################################
#### Functions for Printing options ####
########################################

'''Create all the time a file with different name'''
def unique_file(rootname, ext, ty_p):
    actualname  =  "%s.%s" % (rootname, ext)
    c           =  itertools.count()
    if ty_p  ==  1:
        while os.path.exists(actualname):
            actualname  =  "%s%d.%s" % (rootname, next(c), ext)
        return actualname
    elif ty_p  == 2:
        actualname  =  "%s.%s" % (rootname, ext)
        return actualname

####################
#### Open files ####
####################

'''Open and read files and special lines'''
'Ctrs are the colums to read from a file '
def read_files(filename, ctr1, ctr2, lines_2_skip):
    col1  =  []
    col2  =  []
    with open(filename, 'r') as f1:
        header           =  f1.readline().strip().split()
        lines            =  f1.readlines()[lines_2_skip:]
        specific_string  =  float(header[15])
#        for line in lines:
#            col1.append(line.strip().split()[ctr1])
#            col2.append(line.strip().split()[ctr2])
        return specific_string

####################
#### Open files ####
####################

'''Open and read files General'''
def read_files_general(filename, ctr1, ctr2, lines_2_skip):
    cols        =  [[] for i in range(ctr1, ctr2 + 1)]
    col_2_read  =  np.arange(ctr1, ctr2 + 1)
    cols = np.loadtxt(filename, skiprows=lines_2_skip, usecols=col_2_read)
    return np.transpose(cols)

##############################################
#### Functions for Density of states CP2K ####
##############################################

'''Gaussian function'''
def gaussian(emin, emax, centre, sigma, npts):
    energies  =  np.linspace(emin, emax, npts)
    gauss     =  1./(np.sqrt(2 * np.pi) * sigma) *  np.exp(-(energies - centre)**2/(sigma**2))
    return gauss

'''Total density of states (alpha + beta)'''
def tot_dens(dos_alpha, dos_beta):
    return [i+j for i,j in zip(dos_alpha,dos_beta)]

