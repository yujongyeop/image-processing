import numpy as np, cv2

img = cv2.imread("images/Guinee.png", cv2.IMREAD_COLOR)
if img is None: raise Exception("파일 영상 처리 에러")

masks = cv2.threshold(img,150,255,cv2.THRESH_BINARY)[1]
# 녹색 (0, 153,0) 노란색 (0, 255, 255) 빨간색(255,0,0)
(b,g,r) = cv2.split(masks)
(row, col) = masks.shape[:2]
for i in range(row):
    for j in range(col):
        item_g = g.item(i,j)
        item_r = r.item(i,j)
        
        if item_r==255 and item_g==255:
            continue
        if item_r == 255:
            r.itemset((i,j),0)            
            g.itemset((i,j),153)            
        elif item_g == 255:
            r.itemset((i,j),255)            
            g.itemset((i,j),0)
mali = cv2.merge([b,g,r])
cv2.imwrite('Mali.png',mali,[cv2.IMWRITE_PNG_COMPRESSION,9])
cv2.imshow('Mali',mali)
cv2.waitKey(0)

