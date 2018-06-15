import numpy as np
#속도가 빠른 수치분석 프로그램이다.

arr = np.arange(10)
# print(type(arr))

arr = np.random.normal(5, 3, 500)
# print(arr)

#평균
print(arr.mean())
#합계
print(arr.sum())
#표준편차
print(arr.std())
#분산
print(arr.var())
#최대값
print(arr.max())
#최소값
print(arr.min())

#최대값, 최소값 위치
print(arr.argmax(), ' - ', arr.argmin())
