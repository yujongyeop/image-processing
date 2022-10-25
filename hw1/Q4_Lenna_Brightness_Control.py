import numpy as np
import cv2

img = cv2.imread("images/Lenna_dark.png", cv2.IMREAD_COLOR)
origin = cv2.imread("images/Lenna_dark.png", cv2.IMREAD_COLOR)

#hsv 후  ycrcb가 더 선명함
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
(h,s,v) = cv2.split(img_hsv)
v = cv2.add(v,90)
img_hsv = cv2.merge([h,s,v])
img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
img_bgr = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
(y,cr,cb) = cv2.split(img_bgr)
y = cv2.equalizeHist(y)
img_bgr = cv2.merge([y,cr,cb])
img = cv2.cvtColor(img_bgr, cv2.COLOR_YCrCb2BGR)
cv2.imshow('Origin', origin)
cv2.imshow('Brightness increase', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
