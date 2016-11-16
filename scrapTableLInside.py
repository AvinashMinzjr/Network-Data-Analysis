# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 12:12:33 2016

@author: Avin
"""

import pandas as pd

dproxy=pd.read_csv('sproxy_list.txt')
dproxy_list = pd.read_csv('proxy_list.txt')
ip_list = dproxy_list["proxy_list"].tolist()
print(dproxy)

for index, row in dproxy.iterrows():
    site_val = row[0]
    print(site_val)
    url="http://example.html"%(site_val,site_val)
    print("Writing Table From "+url+".....")
    df = pd.read_html(str(url))
    df2 = pd.DataFrame.from_records(df[1])
    #df2.drop(df2.columns[[0,5,10]], axis=1, inplace=True)
    abc=len(df2.index)
    i=1
    with open('dfFile.txt', 'a') as f:
        while(abc>3):
            f.write(df2[1][i]+","+df2[2][i]+","+df2[3][i]+","+df2[4][i]+"\n")
            abc = abc - 1
            i = i + 1
