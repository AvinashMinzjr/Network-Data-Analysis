# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 13:53:09 2016

@author: Avin
"""

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
df = pd.read_csv("example.txt")

total_usr = ((df["SourceIp"].unique())).tolist()
print("Total_Users")
print(len(total_usr))

total_site = df["SiteName"].tolist()
print("Total_sites")
print(len(total_site))

total_bytes = df["Bytes"].tolist()
print("Total_Bandwidth_in Bytes")
print(sum(total_bytes))

#total_connect = df["Connect"].tolist()
#print("Total_Session")
#print(sum((total_connect)))
