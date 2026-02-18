import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0, 1, 100)

def calculate_sin(x):
	return np.sin(x)
def calculate_cos(x):
	return np.cos(x)

ysin = calculate_sin(x)
ycos = calculate_cos(x)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot(x, ysin)
axs[0].set_title('sin(x)')
axs[0].set_xlabel('x')
axs[0].set_ylabel('sin(x)')
axs[0].grid(True)

axs[1].plot(x, ycos)
axs[1].set_title('cos(x)')
axs[1].set_xlabel('x')
axs[1].set_ylabel('cos(x)')
axs[1].grid(True)

plt.tight_layout()

plt.savefig('trig_functions.pdf')


plt.show()