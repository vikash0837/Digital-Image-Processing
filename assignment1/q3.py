'''
Created by Vikash Kumar
Email: vikash0837@gmail.com
Below code create create 3-D mesh from gray image
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
# for the surface map
from mpl_toolkits.mplot3d import Axes3D

img = cv2.imread("data/cameraman.tif",0)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.figure(0)
plt.imshow(img,cmap='gray', vmin=0, vmax=255)
plt.figure(1)
ax = plt.axes(projection='3d')
y = range(img.shape[0])
x = range(img.shape[1])
X, Y = np.meshgrid(x, y)
# Reference for 3-D plot
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
ax.plot_surface(X, Y, img[:,:],cmap='gray')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('pixelValue')
plt.title("Mesh Plot")
plt.show()
