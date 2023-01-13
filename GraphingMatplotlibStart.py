# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:31:13 2018

@author: Grivin
"""

import matplotlib.pyplot as plt

f_in = open(r'C:\Users\grivi\Desktop\WMPython\Graphing and Network Analysis\\sf.csv',)
data = f_in.readlines()
f_in.close()

for i in range(len(data)):
    data[i] = data[i].strip().split(',')
    data[i] = [data[i][0][-5:],float(data[i][1])]
    
x = [datum[0] for datum in data]
y = [datum[1] for datum in data]

plt.plot(y)
plt.suptitle('San Franciso, CA Housing Prices')
plt.xlabel('YY-MM')
plt.ylabel('Average Home Price ($)')
plt.gcf().set_size_inches(12,6)
p = 20
plt.xticks(range(0,len(x),p),[x[i] for i in range(len(x)) if i % 20 == 0])
plt.show()