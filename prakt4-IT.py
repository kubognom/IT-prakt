# 4 функция
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
beta = (1, 0.3)
def f(x, b0, b1):
    return b0* x ** b1
xdata = np.linspace(1, 9, 50)


y = f(xdata, *beta)
ydata = y + 0.05 * np.random.randn(len(xdata))
beta_opt, beta_cov = sp.optimize.curve_fit(f, xdata, ydata)
print(beta_opt)
lin_dev = sum(beta_cov[0])
print(lin_dev)
residuals = ydata - f(xdata, *beta_opt)
fres = sum(residuals**2)
print(fres)
fig, ax = plt.subplots()
ax.scatter(xdata, ydata)
ax.plot(xdata, y, 'r', lw=2)
ax.plot(xdata, f(xdata, *beta_opt), 'b', lw=2)
ax.set_xlim(0,5)
ax.set_xlabel("x", fontsize=18)
ax.set_ylabel("f(x, ,бета)", fontsize=18)
plt.show()



