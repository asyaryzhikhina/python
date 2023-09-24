import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(-2, 2.01, 0.001)
c = 100
b = 0.25
a = 5
y1 = np.array([])
y = np.array([])
for x in x1:
    for i in range(c):
        y = np.append(y, np.cos(np.pi*x*a**i)*b**i)
    y2 = np.sum(y)
    y1 = np.append(y1, y2)
    y = np.array([])
