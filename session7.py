import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)

def calculate_exp(input_x):
    return np.exp(input_x)


y = calculate_exp(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y)


plt.xlabel("Time [milliseconds]")
plt.ylabel("Awesomeness")
plt.title("Exponential Growth")
plt.grid(True)


plt.savefig("awesomeness_plot.pdf")

plt.show()