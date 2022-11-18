import numpy as np
import cv2

image = cv2.imread("images/canny.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

canny = cv2.Canny(image, 100, 150)

cv2.imshow("image", image)
cv2.imshow("canny", canny)
cv2.waitKey(0)

