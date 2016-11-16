# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 14:12:26 2016

@author: Avin
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
df = pd.read_csv("example.txt")
label = (df["SiteName"].head(10))
y = (df["Bytes"].head(10))
print("9th May")
plt.pie(y,labels=label,autopct="%1.1f%%")
print(df['SiteName'].head(10))
plt.show()
#with open("pie.txt",'a') as f:
#    f.write(str(a)+"\n"+str(b)+"\n"+str(c)+"\n"+str(d))
#print("done")
