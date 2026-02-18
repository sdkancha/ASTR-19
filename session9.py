import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
data = rng.uniform(low=0.0, high=1.0, size=1000)

plt.hist(data, bins=100, color='skyblue', edgecolor='black')

plt.xlabel('Value (Uniformly Distributed)')
plt.ylabel('Frequency')

plt.savefig('uniform_histogram.pdf', format='pdf')

plt.show()