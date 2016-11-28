# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:40:14 2016

@author: Vivian Zhong

Run after compiler.py. Checks to make sure that 
    1) masterfile.csv contains all and only all the collective data from the raw data files (throws an error)
    2) no raw files have been modified (prints a warning)
"""
import pandas as pd
import os
import hashlib
import ast

class DataMismatchException(Exception):
    """
    raised if the total number of rows in raw data files does not match the number of rows in the masterfile.
    """
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
    
files = os.listdir()
total_rows = 0
masterfile_rows = 0

# Read in dictionary of file hashes from hash.log
with open("hash.log", "r") as f:
    hash_log = f.read()
    hash_log = ast.literal_eval(hash_log)

for file in files:
    if file.endswith(".csv") and file != "master_datafile.csv":
        df = pd.read_csv(file)
        total_rows += len(df.index)
        #check hash
        if md5(file) != hash_log[file]:
            print("Raw data file" + file + "has been modified since last compilation.")
    if file == "master_datafile.csv":
        df = pd.read_csv(file)
        masterfile_rows = len(df.index)
        #check hash
        if md5(file) != hash_log[file]:
            print("Master datafile" + file + "has been modified since last compilation.")
if total_rows != masterfile_rows:
    raise DataMismatchException
print("Finished checks.")



