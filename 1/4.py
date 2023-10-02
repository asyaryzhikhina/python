import numpy as np
import matplotlib.pyplot as plt


plt.plot(x, eval(input())) # NameError: name 'x' is not defined
with plt.xkcd():
    plt.title(input())
    plt.xlabel(input())
plt.ylabel(input())
plt.grid(True)
plt.show()
