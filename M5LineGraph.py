# -*- coding: utf-8 -*-
"""

@author: Grivin
"""
import matplotlib.pyplot as plt
data = [['Jun',4.3],['Jul',4.3],['Aug',4.4],['Sep',4.2],['Oct',4.1],['Nov',4.1],['Dec',4.1],['Jan',4.1],['Feb',4.1],['Mar',4.1],['Apr',3.9],['May',3.8],]

""" Program you solution to this assignment below using 
    the variable names as defined below                 """
    
    
x = [i[0] for i in data]
    
    
y = [i[1] for i in data]


plt.plot(list(range(0,12)),y)
plt.xticks(list(range(0,12)),x)
plt.xlabel('Month')
plt.ylabel("Unemployment Rate (%)")
plt.title("U.S. Unemployment Rate")
plt.show()