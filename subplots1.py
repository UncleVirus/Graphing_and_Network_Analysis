# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
ax.plot([0,1,2,3])
fig.suptitle('Test')
plt.show()
print('fig type: ' + str(type(fig))+'\n')
print('ax type: ' + str(type(ax))+'\n')