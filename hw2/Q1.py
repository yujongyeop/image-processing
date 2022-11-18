import numpy as np, cv2

img = cv2.imread("images/sibal.jpg", cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception("파일 영상 처리 에러")

mask = np.ones((5,17), np.uint8)

th_img = cv2.threshold(img, 175 , 255, cv2.THRESH_BINARY)[1]
morph = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations=3)
morph_r = np.zeros((mask.shape[0],mask.shape[1],-1), np.uint8)
morph_b = np.zeros((mask.shape[0],mask.shape[1],0), np.uint8)
color = cv2.merge([morph_b, morph_r,morph])


cv2.imshow('origin', img)
cv2.imshow('th', th_img)
cv2.imshow('morph', morph)
cv2.imshow('color', morph)
cv2.waitKey(0)