import numpy as np
import time
import math
import random


n = [10,50,100,150,200,300,400,500]
x = 1.2

sum_time1 = []
sum_time2 = []
sum_time3 = []
sum_time4 = []

for ele in n:
    a = np.random.random(ele) #随机生成ele*ele维
    p = np.poly1d(a)  #多项式函数
    time_start = time.time()
    temp = np.polyval(p , x)
    time_end = time.time()
    sum_time1.append(time_end-time_start)

    temp = float('Inf')
    time_start = time.time()
    for i in range(0 , ele ,1):
        temp = temp + a[i] * x **i
    time_end = time.time()
    sum_time2.append(time_end - time_start)


    time_start = time.time()
    q = 1
    for i in range(0,ele,1):
        q = q * x
        temp = temp +a[i]*q
    time_end = time.time()
    sum_time3.append(time_end-time_start)

    time_start = time.time()
    for i in range(0,ele,1):
        temp = temp * x + a[ele - i -1]
    time_end = time.time()
    sum_time4.append(time_end - time_start)


print(sum_time1)
print(sum_time2)
print(sum_time3)
print(sum_time4)