# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 12:18:08 2016

@author: Avin
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
df = pd.read_csv("top_example.txt")
label = (df["SourceIp"].head(10))
y = (df["Connect"].head(10))
print("example")
plt.pie(y,labels=label,autopct="%1.1f%%")
print(df['SourceIp'].head(10))
plt.show()
