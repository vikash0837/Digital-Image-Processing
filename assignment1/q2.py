'''
Created by Vikash Kumar
Email: vikash0837@gmail.com
Below code create new image with linear combination of given two input images
'''
import cv2
def nothing(x):
    pass
img1= cv2.imread("data/cameraman.tif",0)
img2= cv2.imread("data/pirate.tif",0)
cv2.namedWindow('Image1')
cv2.namedWindow('Image2')
cv2.namedWindow("output")
# Reference for creating trackbar
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_trackbar/py_trackbar.html
# create trackbars for color change
cv2.createTrackbar('alpha','output',0,100,nothing)


while(1):
    cv2.imshow('image1',img1)
    cv2.imshow('image2',img2)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    alpha = cv2.getTrackbarPos('alpha','output')
    alpha = float(alpha/100)
    print("current value of alpha:{} ".format(alpha))
    # test for same shape before adding
    img= alpha*img1 + (1-alpha)*img2
    img = img.astype('uint8')
    cv2.imshow('output',img)
cv2.destroyAllWindows()