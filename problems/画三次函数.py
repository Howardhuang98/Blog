import matplotlib.pyplot as plt
import numpy as np


def func(x):
    y = 3.77055206e+25*x**3-3.77055209e+25*x**2+5.57363838e+17*x-4.10974943e-06
    return y

plt.figure()
x = np.arange(0,1,0.001,dtype=float)
plt.plot(x,func(x))
plt.xlim(0,1)
plt.show()