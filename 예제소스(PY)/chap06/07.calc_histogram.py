import numpy as np, cv2

def calc_histo(image, hsize, ranges=[0, 256]):  # 행렬 원소의 1차원 히스토그램 계산
    hist = np.zeros((hsize, 1), np.float32)  # 히스토그램 누적 행렬
    gap = ranges[1] / hsize  # 계급 간격

    for row in image:  # 2차원 행렬 순회 방식
        for pix in row:
            idx = int(pix / gap)
            hist[idx] += 1
    return hist

def calc_histo2(image, hsize, ranges=[0, 256]):  # 행렬 원소의 1차원 히스토그램 계산
    hist = np.zeros((hsize, 1), np.float32)  # 히스토그램 누적 행렬
    gap = ranges[1] / hsize  # 계급 간격

    idxs = (image/gap).astype(int).flatten()
    for i in idxs:
        hist[i] += 1

    return hist


image = cv2.imread("images/pixel.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")

th_img = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)[1] # 이진화 수행
cv2.imshow("th_img", th_img)
hsize, ranges = [16], [0, 256]  # 히스토그램 간격수, 값 범위
hist = calc_histo2(image, hsize[0], ranges)  # 사용자 정의 히스토그램 계산

print("사용자 정의 함수: \n", hist.flatten())  # 행렬을 벡터로 변환하여 출력
cv2.imshow("image", image)
cv2.waitKey(0)