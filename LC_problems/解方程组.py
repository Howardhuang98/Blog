import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.optimize

point = 0.33**2

def func(x, r):
    y = r[0] * x ** 3 + r[1] * x ** 2 + r[2] * x + r[3]
    return y


def func2(x):
    a, b, c, d = x[0], x[1], x[2], x[3]

    return [a + b + c + d - 1e10,
            a * point ** 3 + b * point ** 2 + c * point ** 1 + d,
            3 * a + 2 * b + c - 1e10,
            3 * a * point ** 2 + 2 * b * point + c
            ]
def func3(x):
    a, b, c, d = x[0], x[1], x[2], x[3]

    return [ d + 1e10,
            a * point ** 3 + b * point ** 2 + c * point ** 1 + d,
            c + 1e10,
            3 * a * point ** 2 + 2 * b * point + c
            ]

result = scipy.optimize.fsolve(func2, [0, 0, 5, 10000])
r2 = scipy.optimize.fsolve(func3,[0,-1e10,0,-1e10])
print(result,r2)
plt.figure()
x1 = np.arange(point, 1, 0.001, dtype=float)
x2 = np.arange(0, point, 0.001, dtype=float)
plt.plot(x1, func(x1, result))
plt.plot(x2,func(x2,r2))
plt.show()

y1 = func(x1, result)
y2 = func(x2,r2)
pddata2 = pd.DataFrame(data=[x2,y2])
pddata1 = pd.DataFrame(data=[x1,y1])
all = pddata2.append(pddata1)
all.to_excel(r"11.xlsx")
