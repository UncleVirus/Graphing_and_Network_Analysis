# -*- coding: utf-8 -*-
"""
@author: Grivin
"""

f_in = open(r'C:\Users\grivi\Desktop\WMPython\Graphing and Network Analysis\\sf.csv',)
data = f_in.readlines()
f_in.close()

for i in range(len(data)):
    data[i] = data[i].strip().split(',')
    data[i] = [data[i][0][-5:],float(data[i][1])]
    
x = [datum[0] for datum in data]
y = [datum[1] for datum in data]