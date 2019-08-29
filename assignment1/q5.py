'''
Created by Vikash Kumar
Email: vikash0837@gmail.com
Below code Generate 2-D sinusoidal curve
'''
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

m = np.asarray(range(1,257))
n = np.asarray(range(1,257))
#z = np.cos(0.4*3.14*m + 0.6*3.14*n + 3.14/4)


def f(m, n):
    return np.cos(0.4*3.14*m + 0.6*3.14*n)


X, Y = np.meshgrid(m,n)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z)
#ax.plot_wireframe(X,Y,Z)
#ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

