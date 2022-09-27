from email.mime import image
import numpy as np, cv2

image = cv2.imread("", cv2.IMREAD_COLOR)
logo = cv2.imread("", cv2.IMREAD_COLOR)
if image is None or logo is None:
    raise Exception("영상파일 읽기 오류")

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

# /작성중