import numpy as np
import cv2

# 회선 수행 함수(교제에서 제공하는 함수)
def filter(image, mask):

    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)                 # 회선 결과 저장 행렬
    xcenter, ycenter = mask.shape[1] // 2, mask.shape[0] // 2  # 마스크 중심 좌표

    for i in range(ycenter, rows - ycenter):                  # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1               # 관심영역 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1               # 관심영역 너비 범위

            roi = image[y1:y2, x1:x2].astype("float32")         # 관심영역 형변환
            tmp = cv2.multiply(roi, mask)                       # 회선 적용
            dst[i, j] = cv2.sumElems(tmp)[0]                    # 출력화소 저장

    return dst                     # 자료형 변환하여 반환
img = cv2.imread("images/Letter.png", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise Exception("파일 영상 처리 에러")

roi = img[:, :]
sobel_col = [-1, 0, 1,
             -2, 0, 2,
             -1, 0, 1]
colMask = np.array(sobel_col, np.float32).reshape(3, 3)
result = filter(roi, colMask)

result = cv2.convertScaleAbs(result)
cv2.imwrite('VerticalEdge.png',result,[cv2.IMWRITE_PNG_COMPRESSION,9])
cv2.imshow('VerticalEdge',result)
cv2.waitKey(0)
