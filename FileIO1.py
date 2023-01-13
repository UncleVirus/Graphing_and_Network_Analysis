# -*- coding: utf-8 -*-
"""
@author: Grivin
"""

f_in = open(r'C:\Users\grivi\Desktop\WMPython\Graphing and Network Analysis\\sf.csv',) 
data = f_in.readlines()
f_in.close()

for i in range(len(data)):
    data[i] = data[i].strip()
    data[i] = data[i].split(',')
    for j in range(len(data[i])):
        if j == 1:
            data[i][j] = float(data[i][j])
        if j == 0:
            data[i][j] = data[i][j][-5:]