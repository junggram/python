#opencv(computer vision) : 이미지/영상/동영상 처리에 사용할 수 있는 오픈 소스 라이브러리
#pip install opencv-python

import cv2

#print(cv2.__version__)

#이미지 읽기
img1=cv2.imread('./lizard.png')
print(type(img1))

#img1=cv2.imread('./lizard.png', cv2.IMREAD_COLOR)      # 채널(channel) : 3개 사용 (R,G,B)
#img1=cv2.imread('./lizard.png', cv2.IMREAD_GRAYSCALE)   # 채널(channel) : 1개 사용 
img1=cv2.imread('./lizard.png', cv2.IMREAD_REDUCED_COLOR_2) # 크기 줄이기 (2의 제곱)
cv2.imshow('image test', img1)
cv2.waitKey()
cv2.destroyAllWindows()

# 이미지를 다른 이름으로 저장
cv2.imwrite('./lizard2.png', img1)

# 이미지 크기 조절
img2=cv2.resize(img1,(320,100),interpolation=cv2.INTER_AREA)
cv2.imwrite('./lizard3.png', img2)

# 이미지 상하좌우 대칭 (Flip)
#a= cv2.imshow('image rotation',cv2.flip(img1, flipCode=0)) # 이미지 뒤집기
a= cv2.imshow('image rotation',cv2.flip(img1, flipCode=1)) #이미지 좌우 대칭
cv2.waitKey()
cv2.destroyAllWindows()

#이미지 처리 라이브러리 : pillow(PIL), Matplotlib ...