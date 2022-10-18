import numpy as np, cv2

img = cv2.imread("images/Area.bmp", cv2.IMREAD_COLOR)
if img is None: raise Exception("파일 영상 처리 에러")

bluePixelNum = 0

masks = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)
blueChanel = masks[0]
for i in range(blueChanel.shape[0]):
    for j in range(blueChanel.shape[1]):
        if blueChanel.item(i,j) == 255:
            bluePixelNum+=1
print(bluePixelNum)
cv2.imshow('Origin', img)
cv2.waitKey(0)