'''
Created by Vikash Kumar
Email: vikash0837@gmail.com
Below code generate 2D cosine plot with slider control for theta
'''
## References
# https://matplotlib.org/3.1.1/gallery/widgets/slider_demo.html
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
# initialize m and n and theta
m = np.asarray(range(1,257))
n = np.asarray(range(1,257))
theta = 0

def f(m, n):
    k= 0.004*np.pi*m + 0.006*np.pi*n + theta
    return np.cos(k)
X, Y = np.meshgrid(m,n)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z,cmap='gray')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("2D Cosine")
#Reference
# https://matplotlib.org/3.1.1/gallery/widgets/slider_demo.html
axcolor = 'lightgoldenrodyellow'
axtheta = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
stheta = Slider(axtheta, 'Theta', 0.0, 2*np.pi, valinit=1)


def update(val):
    theta = stheta.val
    k = 0.004 * np.pi * X + 0.006 * np.pi * Y + theta
    print("k shape",k.shape)
    Z = np.cos(k)
    #plt.cla()
    ax.plot_surface(X, Y, Z, cmap='gray')
    #ax.(X, Y, Z, cmap='gray')
    fig.canvas.draw_idle()

stheta.on_changed(update)
plt.show()
plt.clf()
plt.cla()
plt.close()


