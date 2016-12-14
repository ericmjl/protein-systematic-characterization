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

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
    
files = [f for f in os.listdir() if f.endswith('.csv')]
total_rows = 0
masterfile_rows = 0

# Read in dictionary of file hashes from hash.log
with open("hash.log", "r") as f:
    hash_log = f.read()
    hash_log = ast.literal_eval(hash_log)
    
def error_file_changed(fname):
    return "File {0} has been changed.".format(fname)
    
def error_rows_different(master, total):
    if master > total:
        return "Master data file has more rows than the raw data files."
    return "Master data file has less rows than the raw data files."
        
def error_sampleid_not_documented(name):
    return "SampleID {0} is not recorded in documentation.".format(name)
    
def test_hash():
    for f in files:    
        assert md5(f) == hash_log[f], error_file_changed(f)
        
def test_total_rows_same():
    masterfile_rows = 0
    total_rows = 0
    for f in files:
        if f == "master_datafile.csv":
            df = pd.read_csv(f)
            masterfile_rows = len(df.index)
        else:
            df = pd.read_csv(f)
            total_rows += len(df.index)
    assert masterfile_rows == total_rows, error_rows_different(masterfile_rows, total_rows)
    
def test_documentation():
    doc = pd.read_excel("sample_name.xlsx")
    df = pd.read_csv("master_datafile.csv")
    for name in df["SampleID"]:
        if name not in doc["SampleID"]:
            error_sampleid_not_documented(name)


