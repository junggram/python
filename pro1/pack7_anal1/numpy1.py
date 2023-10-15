# numpy:
# Numpy는 C언어로 구현된 파이썬 라이브러리로써, 고성능의 수치계산과 선형대수학을 위해 제작되었다.
# Numerical Python의 줄임말이기도 한 Numpy는 벡터 및 행렬 연산에 있어서 매우 편리한 기능을 제공

grades=[1,3,-2,4] # 변량

def grades_sum(grades):
    tot = 0
    for g in grades:
        tot+=g
    return tot

print('합은 ',grades_sum(grades))

def grades_avg(grades):
    tot=grades_sum(grades)
    avg=tot/len(grades)
    return avg
    
print('평균은 ',grades_avg(grades))

def grades_variance(grades): # 편차 ^ 2의 평균 = 분산
    avg=grades_avg(grades)
    vari=0
    for su in grades:
        vari += (su-avg) ** 2
    # return vari / len(grades) # 
    return vari / (len(grades)-1) # R에서는 표본집단으로 봐서 -1
print('분산은 ',grades_variance(grades))

def grades_std(grades):
    return grades_variance(grades) ** 0.5 # 분산 ^ 0.5 = 표준편차

print('표준편차는 ',grades_std(grades))
    
print('-------'*5)
    
print('numpy 함수 사용')
import numpy
print('합은 ',numpy.sum(grades))
print('평균은 ',numpy.mean(grades))
print('분산은 ',numpy.var(grades))
print('표준편차는 ',numpy.std(grades))