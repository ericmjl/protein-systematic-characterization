# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 18:24:27 2016

@author: Vivian Zhong
"""
import pandas as pd
import os

files = os.listdir()
master_df = pd.DataFrame(columns=["SampleID", "Well", "Replicate", "Well Type",
                                  "Date", "Luminescence",
                                  "Normalized to Negative", "Vlumins"])
for f in files:
    if f.endswith(".csv") and f != "master_datafile.csv":
        print(f)
        df = pd.read_csv(f, index_col="SampleID")
        df["Luminescence"] = df["Luminescence"] + 1 - df["Luminescence"].min()
        # Negative control normalization to a Mock test
        # print(df["Luminescence"]["Mock"])
        try:
            df["Normalized to Negative"] = (df["Luminescence"] /
                                            df["Luminescence"]["Mock"].values[0])
        except:
            df["Normalized to Negative"] = (df["Luminescence"] /
                                            df["Luminescence"]["Mock"])
        # Positive control normalization, calculates the normalized polymerase
        # activity relative to pol activity in the Vic control
        try:
            df["Vlumins"] = (df["Normalized to Negative"] /
                             df["Normalized to Negative"]["Vic"].values[0])
        except:
            df["Vlumins"] = (df["Normalized to Negative"] /
                             df["Normalized to Negative"]["Vic"])
        df = df.reset_index()
        master_df = master_df.append(df, ignore_index=True)

# Overwrite master file with new compiled dataframe
master_df.to_csv("master_datafile.csv")
