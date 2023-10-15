# Matplotlib

# - http://matplotlib.org
# - 플로팅 라이브러리로 matplotlib.pyplot 모듈을 사용하여 그래프 등의 시각화 가능.
# - 그래프 종류 : line, scatter, contour(등고선), surface, bar, histogram, box, ...
# - Figure
# 모든 그림은 Figure라 부르는 matplotlib.figure.Figure 클래스 객체에 포함.
# 내부 plot이 아닌 경우에는 Figure는 하나의 아이디 숫자와 window를 갖는다.
# figure()를 명시적으로 적으면 여러 개의 윈도우를 동시에 띄우게 된다.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False #tick이 음수일 때 깨짐 방지

# x = ['서울', '수원', '인천']
# y = [5,3,7]
#
# plt.xlim([-1,3]) #x,y 의  tick 최소값과 최댓값 입력
# plt.ylim([0,10])
# plt.plot(x, y) #주비터와 콜랩에서는 여기까지만 써도 차트가 나온다.
# plt.yticks(list(range(0,11,3)))
# plt.show()
#
# data = np.arange(1,11,2) # [1,3,5,7,9]
# print(data)
# plt.plot(data)
# x = [0,1,2,3,4]
# for a, b in zip(x, data):
#     #print(a,b)
#     plt.text(a,b,str(b)) #그래프에 숫자 찍어줌
# plt.show()
# x = np.arange(10)
# y = np.sin(x)
# print(x,y)
# plt.plot(x,y,'go--', linewidth=2, markersize=10) #style 'bo', 'r+' 등등
# plt.show()
#
# # ----------hold : 복수의 차트를 하나의 영역에 겹쳐서 출력
# x = np.arange(0, np.pi * 3, 0.1) #pi 값을 줌,, 
# y_sin = np.sin(x)
# y_cos = np.cos(x)
#
# plt.plot(x,y_sin,'r')
# plt.plot(x, y_cos,'b')
# plt.title('사인 & 코사인')
# plt.legend(['sin','cos']) #범례 (가장 알맞은 위치에 locate)
# plt.show()
#
# print('@@@@@@@@@@@@@@@@@@@@')
# # ----------subplot : Figure를 여러 개로 나눔
# plt.subplot(2,1,1) #2행 1열, 1행에서 active
# plt.plot(x,y_sin,'r')
# plt.subplot(2,1,2)
# plt.scatter(x,y_cos)
# plt.show()

# irum = 'a','b','c','d','e'
# kor = [80,50,70,70,90,]
# eng = [60,70,80,70,60,]
# plt.plot(irum, kor,'ro-')
# plt.plot(irum, eng,'gs--')
# plt.ylim([0,100])
# plt.legend(['국어','영어'], loc=3) # loc 는 시계 반대방향으로 돌아감
# plt.grid(True)
#
# fig = plt.gcf() # 보여주는 내용을 이미지로 저장
# plt.show()
# fig.savefig('차트.png') # 이미지 저장은 png로 저장하는걸 강력 추천
#
# from matplotlib.pyplot import imread
# img = imread('차트.png')
# plt.imshow(img)
# plt.show()