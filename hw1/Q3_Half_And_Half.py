import numpy as np
import cv2

pizza1 = cv2.imread("images/pizza1.png", cv2.IMREAD_COLOR)
pizza2 = cv2.imread("images/pizza2.png", cv2.IMREAD_COLOR)
halfAndHalf = np.zeros((pizza1.shape), np.uint8)

(row, col) = pizza1.shape[:2]
width = col // 2 + 1
roi1 = pizza1[:,:width]
roi2 = pizza2[:,width:]
halfAndHalf[:,:width] = roi1
halfAndHalf[:,width:] = roi2
cv2.imshow('pizza1', pizza1)
cv2.imshow('pizza2', pizza2)
cv2.imshow('half and half', halfAndHalf)
cv2.waitKey(0)
