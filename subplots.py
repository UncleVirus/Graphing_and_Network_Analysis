# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

fig,ax = plt.subplots(nrows=2, ncols = 2)
ax[0,0].plot([0,1,2,3])
ax[0,1].plot([0,1,3,2])
ax[1,0].plot([3,2,1,0])
ax[1,1].plot([3,1,2,0])
fig.suptitle('Test')
plt.show()
print('fig type: ' + str(type(fig))+'\n')
#print(str(dir(fig))+'\n\n')
print('ax type: ' + str(type(ax[0,0]))+'\n')
#print(str(dir(ax[0,0])))