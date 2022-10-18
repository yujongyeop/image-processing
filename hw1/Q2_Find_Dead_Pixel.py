import numpy as np
import cv2

red, green = (0,0,128), (0,128,0)
chanel_BG = np.zeros((862,2526),np.uint8)
def OpenImg(num):
    img_name = "images/DeadPixel" + str(num) + ".bmp"
    img = cv2.imread(img_name, cv2.IMREAD_COLOR)
    img = np.float32(img)
    if img is None:
        raise Exception("파일 영상 처리 에러")
    else:
        FindDeadPixel(img, num)

def FindDeadPixel(img, num):
    totalDeadPixel = 0
    center_status = True
    (b,g,r) = cv2.split(img)
    b[:,:] =0
    g[:,:] =0
    mask = cv2.threshold(r, 0, 255, cv2.THRESH_BINARY)[1]
    (row, col) = mask.shape
    width = col // 3 + 1
    height = row // 3 + 1
    for i in range(3):
        for j in range(3):
            deadPixel = 0
            w = width * i
            h = height * j
            roi = mask[h:h+height, w:w+width]
            roiDeadPixel = cv2.reduce(roi, dim=0, rtype=cv2.REDUCE_SUM)
            deadPixel = int(roiDeadPixel.sum() / 255)
            if i == 1 and j == 1:
                if deadPixel > 1:
                    center_status = False
            totalDeadPixel += deadPixel
    mask = cv2.merge((b,g,mask))
    if totalDeadPixel < 10 and center_status:
        ShowImg(mask, 'GOOD', num)
    else:
        ShowImg(mask,'NG',num)

def ShowImg(mask, status, num):
    li = [chanel_BG,chanel_BG,mask]
    title = 'DeadPixel' + str(num) + '.bmp'
    if status =='NG':
        cv2.putText(mask,status, (2440,50), cv2.FONT_HERSHEY_SIMPLEX, 2, red)
    else:
        cv2.putText(mask,status, (2350,50), cv2.FONT_HERSHEY_SIMPLEX, 2, green)
    cv2.imshow(title, mask)

for i in range(3):
    OpenImg(i+1)

cv2.waitKey(0)