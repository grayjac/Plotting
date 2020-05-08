#!/usr/bin/env python3


# ME499-S20 Python Lab 4
# Programmer: Jacob Gray
# Last Edit: 4/30/2020


import time
import numpy as np
from msd import MassSpringDamper
from matplotlib import pyplot as plt
from utils import simulate_gachapon
from utils import random_list
from counter import get_element_counts


smd = MassSpringDamper(m=1.0, k=5.0, c=2.5)
state, times = smd.simulate(1.0, -1.0, 40.0)


"""plt.plot(times, state[:, 0])
plt.title('Position vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.savefig('problem_1_plot.png')"""


results = []


for i in range(1000):
    results.append(simulate_gachapon(15))

q75, q25 = np.percentile(results, [75, 25])
iqr = q75 - q25
h = 2 * iqr * len(results) ** (-1/3)
bins = int((max(results) - min(results)) / h)

"""plt.hist(results, bins=bins)
plt.title('Distribution of gachapon results')
plt.ylabel('Number of occurrences')
plt.xlabel('Number of iterations until all prizes collected')
plt.savefig('problem_2_plot.png')"""


length_list = []
runtimes = []


for i in range(50, 2500, 50):
    length_list.append(i)
    my_list = random_list(i)
    initial_time = time.time()
    get_element_counts(my_list)
    final_time = time.time()
    runtimes.append(final_time - initial_time)


plt.scatter(length_list, runtimes)
plt.title('Runtime vs. List Length')
plt.ylabel('Runtime (s)')
plt.xlabel('Length of list (number of elements)')
plt.savefig('problem_3_plot.png')




