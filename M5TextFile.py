# -*- coding: utf-8 -*-

""" Program you solution to this assignment below using 
    the variable names as defined below                 """

#open the file in read mode
f = open('states.csv', 'r')
#read the data into the list
statesData = f.readline() #reads the data
if " " in statesData:
    data = [line.strip("\n").split(" ")for line in f.readlines()]
else:
    # If the data is actually separated by a comma
    data = [line.strip("\n").split(",") for line in f.readlines()] 
# Close the file
f.close()  

# When we split by space; State like 'District of Columbia' will bring a discrepancy so we will have to handle that.
i = 0
for lst in data:
    if len(lst) > 4: 
        cleaned = [" ".join(lst[:-4])] + lst[-4:]
        data[i] = cleaned
    i += 1

# Convert the data into the correct data types
data = [[line[0], int(line[1]), int(line[2]), float(line[3]), float(line[4])] for line in data]

# Create the list called sums
sums = [0, 0, 0, 0]

for lst in data:
    sums[0] += lst[1]
    sums[1] += lst[2]
    sums[2] += lst[3]
    sums[3] += lst[4]
    
# Displaying the sums list
print(sums)
print(statesData)
