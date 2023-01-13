# -*- coding: utf-8 -*-

""" Program you solution to this assignment below using 
    the variable names as defined below.                
    
    Recall that the data for this assignment is contained 
    in a file named length.csv                            """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = "Number of Characters"     # use this variable for the x-acis data


y = "Frequency."        # use this variable for the y-axis data

title="Analysis of President Trump's Tweet Length."

data=pd.read_csv(r"length.csv")
plt.hist(data)
plt.xlabel(x)
plt.ylabel(y)
plt.title(title)
plt.show()