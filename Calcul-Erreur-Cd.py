import matplotlib
import scipy
import numpy as np
import matplotlib.pyplot as plt
import random
import pylab as pl


Cd90 = 297

l = 0.2;

K90 = (8/3)*l**(-1/3)*((-l)/(1-l**2)-(2*l**2-3)/(1-l**2)**(3/2)*np.arcsin(np.sqrt(1-l**2)))**(-1);

Cdsph = (24/0.1);
Cdth90 = Cdsph*K90;

print('Cdth90 : ' + str(Cdth90))

ErrCd90 = abs(((Cdth90-Cd90)/Cdth90)*100)
print('ErrCd90 : ' + str(ErrCd90))
