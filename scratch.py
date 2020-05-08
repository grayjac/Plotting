#!/usr/bin/env python3

import numpy as np
import random
import matplotlib.pyplot as plt
import time

a = np.array([1, 2, 3])
b = np.array([3, -2, 5])
print(sum(a * b))
print(a.dot(b))
print(random.choice(a))
times = np.linspace(0, 10, 1000)  # Linearly interpolates between 0 and 10 and gives 1000 equally spaced elements
values = np.sin(np.pi * times)
noised_values = values + np.random.normal(0, 0.05, 1000)

plt.plot(times, noised_values, linewidth=2, color='mediumaquamarine', label='Noise')
plt.plot(times, values, linestyle='dashed', label='Orig')

plt.title('Signal Analysis')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.legend()
plt.ylim(-1.0, 1.0)
# plt.savefig('my_graph.png')

5
x = [0, 1, 2, 3, 4]
print(time())
