# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

"""Input data from file"""
f_in = open('wordsWMDict.csv','r')  # file must be in same file folder as Python program
data = f_in.readlines()
f_in.close()

"""Strip and split data into a list of lists """
for i in range(len(data)):
    data[i] = data[i].strip().split(',')
    data[i][1] = int(data[i][1])

""" Delete stopwords """
stopWords = ['and','a','the','of','by','to','in','of','its','for','is','with']
data = [x for x in data if x[0] not in stopWords]

""" Create lists for x-axis labels and y-axis frequencies """
data.sort(key = lambda x:x[1],reverse=True)
numPlot = 15
data = data[:numPlot]
freq = [freq for [word,freq] in data]
words = [word for [word,freq] in data]
xs = range(len(data)) # for xticks
                      # xticks must be a list of integers of the same length as the
                      # data to be plotted

""" Create fig variable for the Figure object and ax variable for the Axes object """
fig,ax = plt.subplots()

""" Axes object properties and methods """
ax.bar(xs,freq, align='center',color='k')
ax.xaxis.set_label_text('Words',fontsize=14)
ax.yaxis.set_label_text('Frequency',fontsize=14)
ax.set_xticks(xs)
ax.set_xticklabels(words, rotation = 45)
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
ax.set_ylim(0,int(max(freq)*1.2))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(False)
ax.tick_params(axis = 'y', which = 'both', direction = 'in', width = 2, color = 'black')

""" Figure object properties and methods """
fig.suptitle('W&M Mission Statement Word Histogram',fontsize=20)
fig.set_size_inches(9,5)
fig.savefig('histWM.jpg',bbox_inches='tight')

""" Display the graph """
plt.show()