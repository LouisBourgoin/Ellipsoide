import matplotlib
import scipy
import numpy as np
import matplotlib.pyplot as plt
import random
import pylab as pl


Cd01 = 343.29047897483446
Cd005 = 411.64012001684284
Cd015 = 313.53718338075549
Cd02 = 296.83251490414807


lmbd = np.linspace(0.01,0.99,100)
K90plt = (8/3)*lmbd**(-1/3)*((-lmbd)/(1-lmbd**2)-(2*lmbd**2-3)/(1-lmbd**2)**(3/2)*np.arcsin(np.sqrt(1-lmbd**2)))**(-1);
Cdsph = (24/0.1);
Cdth90plt = Cdsph*K90plt;


plt.figure()
plt.ylabel(r"Cx")
plt.xlabel(r"$\lambda$")
plt.xscale('log')
plt.yscale('log')
plt.grid( linestyle='-', which="both",  linewidth=0.5)
plt.plot(lmbd,Cdth90plt, 'r-', label="ligne -")   
plt.plot(0.1,Cd01,marker="x", markersize=5, markerfacecolor="blue")
plt.plot(0.05,Cd005,marker="x", markersize=5, markerfacecolor="blue")
plt.plot(0.15,Cd015,marker="x", markersize=5, markerfacecolor="blue")
plt.plot(0.2,Cd02,marker="x", markersize=5, markerfacecolor="blue")
