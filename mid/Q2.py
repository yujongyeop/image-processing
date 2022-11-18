import numpy as np, cv2

australia_bg = cv2.imread("images/Australia_bg.png", cv2.IMREAD_COLOR)
england = cv2.imread("images/England.png", cv2.IMREAD_COLOR)
if australia_bg is None or england is None: raise Exception("파일 영상 처리 에러")
(row,col) = england.shape[:2]
row = row//2
col = col//2
roi = australia_bg[:row, :col]

re_england = cv2.resize(england, (col,row), 0,0,cv2.INTER_LINEAR)
bin_england = cv2.threshold(re_england,50,255,cv2.THRESH_BINARY)[1]

(b,g,r) = cv2.split(bin_england)
b = cv2.bitwise_and(r,b)
foreground = cv2.bitwise_and(re_england,re_england, mask=r)
background = cv2.bitwise_and(roi,roi, mask=cv2.bitwise_not(r))
roi= cv2.add(background,foreground)
australia_bg[:roi.shape[0],:roi.shape[1]] = roi
cv2.imwrite('Australia_bg.png',australia_bg,[cv2.IMWRITE_PNG_COMPRESSION,9])
cv2.imshow('australia',australia_bg)
cv2.waitKey(0)