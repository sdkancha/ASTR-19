import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()


probability_of_success = 0.25 
sample_size = 1000
data = rng.geometric(p=probability_of_success, size=sample_size)


plt.hist(data, bins=100)


plt.xlabel('Number of Trials to First Success')
plt.ylabel('Frequency')

plt.savefig('geometric_histogram.pdf', format='pdf')

plt.show()