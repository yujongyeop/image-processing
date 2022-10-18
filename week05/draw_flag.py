from re import U
from turtle import width
import numpy as np
import cv2

img = np.zeros((300, 500, 3), np.uint8)
color = [(0, 0, 0), (32, 219, 253), (62, 48, 239)]
(row, col) = img.shape[:2]
width = col // 3 + 1
for i in range(3):
    w = width * i
    img[:, w:width+w] = color[i]
cv2.imshow("belgium", img)

height = row // 3+ 1
seq = [0,2,1]
for i in range(3):
    h = height*i
    img[h:h+height, :] = color[seq[i]]
cv2.imshow("Germany", img)

cv2.waitKey(0)