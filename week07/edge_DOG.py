import numpy as np
import cv2

image = cv2.imread("images/dog.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")


# SoG 연산
gaus = cv2.GaussianBlur(image, (7, 7), 0, 0)  # 가우스마스크 적용
dst1 = cv2.Laplacian(gaus, cv2.CV_16S, 7)  # 라플라시안 수행

# DoG 연산
gaus1 = cv2.GaussianBlur(image, (3, 3), 0)
gaus2 = cv2.GaussianBlur(image, (9, 9), 0)
dst2 = gaus1 - gaus2

cv2.imshow("image", image)
cv2.imshow("dst1- LoG", dst1.astype('uint8'))
cv2.imshow("dst2- DoG", dst2)
cv2.waitKey(0)
