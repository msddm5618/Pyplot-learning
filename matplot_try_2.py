import numpy as np
import matplotlib.pyplot as plt

# Generate the data

label_m = ['Method 1', 'Method 2', 'Method 3', 'Method 4']
label_x = ['$2^3$', '$2^5$', '$2^7$', '$2^9$', '$2^{11}$']
N_m = len(label_m)
N = 10
np.random.seed(0)
data = np.random.rand(N_m, N)*180

ind = np.arange(N)  # the x locations for the groups
xtic = np.arange(1, N+1, step=2)

line1 = plt.plot(ind, data[0,:], ls='-', marker='o', label=label_m[0])
line2 = plt.plot(ind, data[1,:], ls='--', marker='v', label=label_m[1])
line3 = plt.plot(ind, data[2,:], ls='-.', marker='*', label=label_m[2])
line4 = plt.plot(ind, data[3,:], ls=':', marker='+', label=label_m[3])

plt.ylabel('GFlop/s')
plt.yticks(np.arange(0, 201, 20))
plt.ylim(0,200)
plt.xlabel("Memory(MB)")
plt.xticks(xtic, label_x)

plt.legend(loc = 9, ncol = 2)


plt.show()
