import cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))

while True:
    ret, frame = capture.read()
    if not ret:
        break
    if cv2.waitKey(30) >= 0:
        break
    
    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    title = "View Frame from Camera"
    cv2.imshow(title, frame)
    
capture.release()