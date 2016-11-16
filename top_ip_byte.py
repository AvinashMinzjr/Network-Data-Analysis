# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:32:00 2016

@author: Avin
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("example.txt")
objects = df["SourceIp"].head(10)
y_pos = np.arange(len(objects))
performance = df["Bytes"].head(10)
#objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
#y_pos = np.arange(len(objects))
#performance = [10,8,6,4,2,1]
# 
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Usage')
plt.title('top 10 Users by Bandwidth')
plt.tight_layout()
plt.plot()
plt.show()
#plt.savefig('abc1.png')
#pie chart
df = pd.read_csv("top_ip_bytes_9thmay2013.txt")
label = (df["SourceIp"].head(10))
y = (df["Bytes"].head(10))
print("9th May")
plt.pie(y,labels=label,autopct="%1.1f%%")
print(df['SourceIp'].head(10))
plt.show()
