import numpy as np
import cv2

image = cv2.imread("images/P1.bmp", cv2.IMREAD_COLOR)
image.reshape
if image is None:
    raise Exception("영상파일 읽기 오류")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(row, col) = gray.shape
corner = cv2.cornerHarris(gray, 10, 3, 0.04)
coord = np.where(corner > 0.1* corner.max())
coord = np.stack((coord[1], coord[0]), axis=-1)
print(coord)
image[corner > 0.1 * corner.max()] = [0,0,255]

target = np.float32([(135,243),(1238,0),(1600,945),(3,1135)])
board = np.float32([(0,0),(col,0),(col,row),(0,row)])
perspect_mat = cv2.getPerspectiveTransform(target, board)
dst = cv2.warpPerspective(image, perspect_mat, (col,row), cv2.INTER_CUBIC)
cv2.imshow("origin", image)
cv2.imshow("dst", dst)
cv2.waitKey(0)
