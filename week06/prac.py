import numpy as np
import cv2
from Common.filters import filter

## 블러링 처리
def Bluring():
    blur_mask = [1/9, 1/9, 1/9,
             1/9, 1/9, 1/9,
             1/9, 1/9, 1/9]
    blurMask = np.array(blur_mask, np.float32).reshape(3,3)
    dst = filter(img, blurMask)
    dst = cv2.convertScaleAbs(dst)
    return dst

## 샤프닝 처리
def Sharpening():
    sharpening_mask = [0, -1, 0,
                   -1, 5, -1,
                   0, -1, 0]
    sharpMask = np.array(sharpening_mask, np.float32).reshape(3,3)
    dst = filter(img, sharpMask)
    dst = cv2.convertScaleAbs(dst)
    return dst

## 소벨 처리(엣지 검출)
def Sobel():
    sobel_row = [-1, -2, -1,
                0, 0, 0,
                1, 2, 1]
    sobel_col = [-1, 0, 1,
                -2, 0, 2,
                -1, 0, 1]
    rowMask = np.array(sobel_row, np.float32).reshape(3, 3)
    colMask = np.array(sobel_col, np.float32).reshape(3, 3)
    dst1 = filter(img, rowMask)
    dst2 = filter(img, colMask)
    dst = cv2.magnitude(dst1,dst2)

    dst = cv2.convertScaleAbs(dst)
    return dst

## 라플라시안 처리(엣지 검출)
def Laplacian():
    dst = cv2.Laplacian(img, cv2.CV_16S,1)
    dst =cv2.convertScaleAbs(dst)
    return dst

img = cv2.imread('images/water.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    raise Exception('파일 읽기 오류')

blur_Result = Bluring()
sharpening_Result = Sharpening()
sobel_Result = Sobel()
laplacian_Result = Laplacian()
cv2.imshow('Original', img)
cv2.imshow('Result - Blur', blur_Result)
cv2.imshow('Result - Sharpening', sharpening_Result)
cv2.imshow('Result - Sobel', sobel_Result)
cv2.imshow('Result - Laplacian', laplacian_Result)
cv2.waitKey(0)
