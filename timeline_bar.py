#this line prepares IPython for working with matplotlib
%matplotlib inline  

# # this actually imports matplotlib
# import numpy as np
# import matplotlib.pyplot as plt  

# x = np.linspace(0, 10, 30)  #array of 30 points from 0 to 10
# y = np.sin(x)
# z = y + np.random.normal(size=30) * .2
# plt.plot(x, y, 'b+:', label='A sine wave')
# #plt.axhspan(0, 0.25, 0, 1, hold=None, hatch='/')
# plt.axvline(x=3, ymin=0, ymax=1, hold=None,linewidth=4, color='r')
# #plt.axvspan(0, 5, 0, 1, hold=None)
# plt.bar(0, 0.25, width=1, bottom=None, hold=None, data=None)
# #plt.plot(x, z, 'b-', label='Noisy sine')
# plt.legend(loc = 'lower right')
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.show()

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_ylim(0, 50)
ax.set_xlim(0, 200)


#ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
#               facecolors=('red', 'yellow', 'green'))



ax.set_xlabel('seconds since start')
ax.set_ylabel('Simulation')

ax.set_yticks([5,15, 25])
ax.set_yticklabels(['S1','S2', 'S3'])


bars_collection_xx =[(100, 20),(150, 10)]
bars_collection_yy = (25,5)
for xx in bars_collection_xx:
    print xx,bars_collection_yy
    ax.broken_barh([xx], bars_collection_yy, facecolors='red',hatch='xxx')


bars_collection_xx =[(100, 20),(150, 10)]
bars_collection_yy = (5,5)
for xx in bars_collection_xx:
    print xx,bars_collection_yy
    ax.broken_barh([xx], bars_collection_yy, facecolors='red',hatch='xxx')


bars_collection_xx =[(100, 20),(150, 10)]
bars_collection_yy = (15,5)
for xx in bars_collection_xx:
    print xx,bars_collection_yy
    ax.broken_barh([xx], bars_collection_yy, facecolors='red',hatch='xxx')


    
    
#ax.broken_barh([(100, 10), (150, 10)], (25, 5), facecolors='red',hatch='xxx')

#ax.broken_barh([(100, 10), (150, 10)], (5, 5), facecolors='blue',hatch='xxx')

#ax.broken_barh([(100, 10), (150, 10)], (15, 5), facecolors='green',hatch='xxx')


plt.axvline(x=10, ymin=0, ymax=1, hold=None)

ax.grid(True)

ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

xposition = [20, 50, 100]

for xc in xposition:
    plt.axvline(x=xc, color='r', linestyle='-')

yposition = [5, 15, 25]
for yc in yposition:
    plt.axhline(y=yc, color='b', linestyle='-')
    
plt.show()
