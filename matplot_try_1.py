import numpy as np
import matplotlib.pyplot as plt

# Generate the data
label_v = ['Param 1', 'Param 2', 'Param 3', 'Param 4']
label_m = ['Method 1', 'Method 2', 'Method 3', 'Method 4', 'Method 5', 'Method 6', 'Method 7', 'Method 8', 'Method 9']
N_v = len(label_v)
N_m = len(label_m)
np.random.seed(0)
data = np.random.randint(40, 60, (N_v, N_m))

ind = np.arange(N_m)  # the x locations for the groups
width = 0.35  # the width of the bars: can also be len(x) sequence

plt.grid(linestyle='--', axis ='y')

rect1 = plt.bar(ind-width/2, data[0,:], width, label=label_v[0], edgecolor='k', linewidth=1)
rect2 = plt.bar(ind-width/2, data[1,:], width, bottom=data[0,:], label=label_v[1], edgecolor='k', linewidth=1)
rect3 = plt.bar(ind+width/2, data[2,:], width, label=label_v[2], edgecolor='k', linewidth=1)
rect4 = plt.bar(ind+width/2, data[3,:], width, bottom=data[2,:], label=label_v[3], edgecolor='k', linewidth=1)

line1 = plt.plot([7.5,7.5], [0,140], linestyle='--', color='black')

plt.xticks(ind, label_m)
plt.ylabel('Power(W)')
plt.yticks(np.arange(0, 141, 10))
plt.ylim(0,140)
plt.legend(loc = 9, ncol = 2)

# Add text
height=data[0,8]+data[1,8]
plt.annotate('{}'.format(height),
             xy=(8-width/2,height),
             xytext=(0,3),
             textcoords="offset points",
             rotation='vertical',
             ha='center', va='bottom')

height=data[2,8]+data[3,8]
plt.annotate('{}'.format(height),
             xy=(8+width/2,height),
             xytext=(0,3),
             textcoords="offset points",
             rotation='vertical',
             ha='center', va='bottom')


plt.show()
