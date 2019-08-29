'''
Created by Vikash Kumar
Email: vikash0837@gmail.com
Below code use thresholding in gray image using trackbar
'''
import numpy as np
import cv2
def nothing(x):
    pass
img=cv2.imread('data/lena_gray_512.tif',0)
img=np.asarray(img)
cv2.namedWindow('image')
# Reference for creating trackbar
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_trackbar/py_trackbar.html
# create trackbars for color change
cv2.createTrackbar('T1','image',0,255,nothing)
cv2.createTrackbar('T2','image',255,255,nothing)
def transform(t1,t2,img_data):
    img_data = np.where(img_data < t1, t1, img_data)
    if(t2>t1):
        img_data = np.where(img_data > t2, t2, img_data)
    return img_data

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    t1 = cv2.getTrackbarPos('T1','image')
    t2 = cv2.getTrackbarPos('T2','image')
    print("current valueod T1:{} and current value of T2:{}".format(t1,t2))
    img=transform(t1,t2,img)
cv2.destroyAllWindows()


