import numpy as np, cv2

img = cv2.imread("images/Gradation_NG.png", cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception("파일 영상 처리 에러")


histImg = cv2.equalizeHist(img)
cv2.imwrite('Gradation_Good.png',histImg,[cv2.IMWRITE_PNG_COMPRESSION,9])
cv2.imshow('Original', img)
cv2.imshow('Gradation_Good', histImg)
cv2.waitKey(0)