import pandas as pd
import sys
import os

from pandas import DataFrame as df

# Reads a file with format of PDOS (CP2K) and puts it in a DB-type of structure.
def file2DF(pfad2inputs):
    #rawFile = pd.read_csv(file2parse, skiprows=[0,1], header=None)
    allInputs = {}
    
    for file in os.listdir(pfad2inputs):
        if file.endswith(".pdos"):
            allInputs[file] = os.path.join(pfad2inputs, file)
    
    filesAsDf = {}
    for files, pdosFiles in allInputs.items():
        filesAsDf[files] = pd.read_csv(pdosFiles, skiprows = [0,1],
                                       header = None, delim_whitespace = True)
    return filesAsDf
        
