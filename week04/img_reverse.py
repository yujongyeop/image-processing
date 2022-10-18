import numpy as np
import cv2

img = cv2.imread("images/test.png", cv2.IMREAD_GRAYSCALE)

row, col = img.shape
height = row // 2 + 1
width = col // 2 + 1
roi = img[:, width:]
avg = cv2.mean(roi)[0]
roi_row, roi_col = roi.shape[:2]
for i in range(roi_row):
    for j in range(roi_col):
        if roi.item(i, j) > avg:
            roi.itemset((i, j), 255)
        else:
            roi.itemset((i, j), 0)


cv2.imshow('img', img)
cv2.waitKey(0)