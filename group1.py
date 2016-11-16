# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:45:38 2016

@author: Avin
"""

import pandas as pd
df=pd.read_csv("new_example.txt")
df['Connect']=df['Connect'].convert_objects(convert_numeric=True)
df['ElapseTime'] = pd.to_timedelta(df['ElapseTime'])
#print(df.dtypes)
aggregations={
           'Connect':'sum',
           'Bytes':'sum',
           'ElapseTime':'sum'         }
           
df1=df.groupby('SourceIp',as_index=False).agg(aggregations)

print("Ip with maximum no. of connection:\n")
top100=df1.nlargest(10,'Connect')
print(top100)
#for i,row in top100.iterrows():
#    with open('top_ip_connect_9thmay2013.txt','a') as f:
#        f.write(str(top100['SourceIp'][i])+","+str(top100['Bytes'][i])+","+str(top100['Connect'][i])+","+str(top100['ElapseTime'][i])+"\n")
#    
print("Ip with maximum no. of Bytes:\n")
top100=df1.nlargest(10,'Bytes')
print(top100)
#for i,row in top100.iterrows():
#    with open('top_ip_bytes_9thmay2013.txt','a') as f:
#        f.write(str(top100['SourceIp'][i])+","+str(top100['Bytes'][i])+","+str(top100['Connect'][i])+","+str(top100['ElapseTime'][i])+"\n")
#    

print("Ip with maximum no. of ElapseTime:\n")
top100=df1.nlargest(10,'ElapseTime')
print(top100)
#for i,row in top100.iterrows():
#    with open('top_ip_elapsetime_9thmay2013.txt','a') as f:
#        f.write(str(top100['SourceIp'][i])+","+str(top100['Bytes'][i])+","+str(top100['Connect'][i])+","+str(top100['ElapseTime'][i])+"\n")
#    
