# -*- coding: utf-8 -*-
"""

@author: Grivin
"""

""" The list below contains words that you are to exclude form your analysis """
stopWords = ['to', 'the', 'a', 'to', 'is', 'and', 'in', 'of', 'that', 'it', 'be','at', 'this', 'are', 'be', 'for', 'will', 'with', 'at', 'have','on','&amp', 'by']

""" Program you solution to this assignment below using 
    the variable names as defined below.                
    
    Recall that the data for this assignment is contained 
    in a file named length.csv                            """
    
import itertools
import matplotlib.pyplot as plt
stopWords = ['to', 'the', 'a', 'to', 'is', 'and', 'in', 'of', 'that', 'it', 'be','at', 'this', 'are', 'be', 'for', 'will', 'with', 'at', 'have','on','&amp', 'by']
#relative reference
file = open('words.csv',)
f = file.read()
#total words in the file
array = []
for word in f.split():
    array.append(word)
#unique words from trumps tweets
unique_words = []
for word in array:
    if word in unique_words:
        continue
    else:
        unique_words.append(word)
#clean array of words not present in stopWords array
cleanArray = []
for word in array:
    if word in stopWords:
        continue
    else:
        cleanArray.append(word)
#dictionary for order of occurence of words
new_dict = dict()
for word in cleanArray:
    if word in new_dict:
        new_dict[word] +=1
    else:
        new_dict[word] = 1
#order the dictionary according the order of occurence
#use a list for the sorting
sorted_words = sorted(new_dict.items(), key = lambda x: x[1], reverse=True)
#convert the list to a dictionary
converted_dict = dict(sorted_words)
#slicing the 10 most used words
final_dict = dict(itertools.islice(converted_dict.items(), 10))
#plotting the data using matplotlib
#x -> x-axis data
#y -> y-axis data
x = list(final_dict.keys())
y = list(final_dict.values())
plt.bar(range(len(final_dict)), y, tick_label=x)
ax = plt.gca()
#rotation of x-axis ticks
ax.tick_params(axis='x', labelrotation = 45)
#title
plt.title("Histogram of Trump's most used words on Twitter against their occurence")
#axis label
plt.xlabel("Words in Trump's Tweets")
plt.ylabel("Number of Occurence")
#saving to a .jpg file
plt.savefig('tweets.jpg')
plt.show()