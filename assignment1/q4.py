'''
Created by Vikash Kumar
Email: vikash0837@gmail.com
Below code will create new image based on the threshold conditions of given two images
'''
import cv2
import numpy as np
img2 = cv2.imread("data/pirate.tif",0)
img1 = cv2.imread("data/cameraman.tif",0)

new_img=np.zeros(shape=img1.shape, dtype=np.uint8)
new_img = np.where(img1>=img2,255,0)
new_img = new_img.astype('uint8')
cv2.namedWindow("img1")
cv2.namedWindow("img2")
cv2.namedWindow("output")
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('output',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()