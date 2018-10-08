'''
  多项式求值:加减乘除
  分别实现多项式求值的四种运算，若针对不同规模的输入值a
  ，各算法的运行时间，问题规模n
  分别取10，50，100，150，200，300，400，500，10000，20000，50000，100000时绘制四种算法运行时间的比较图。
'''

import numpy as np
import time
import math
import random

n = [10,50,100,150,200,300,400,500]
x = 1.2 #将多项式中x的值设为1.2
Sum_time1 = []
Sum_time2 = []
Sum_time3 = []
Sum_time4 = []
for ele in n:
    a =  np.random.random(ele)
    p = np.poly1d(a)
    time_start = time.time()
    temp = np.polyval(p, x)
    time_end = time.time()
    Sum_time1.append(time_end - time_start)

    temp = float('Inf')
    time_start = time.time()
    for i in range(0, ele, 1):
        temp = temp + a[i] * x**i
    time_end = time.time()
    Sum_time2.append(time_end - time_start)

   # temp = int()
    time_start = time.time()
    q = 1
    for i in range(0, ele, 1):
        q = q * x
        temp = temp + a[i] * q
    time_end = time.time()
    Sum_time3.append(time_end - time_start)

    #temp = int()
    time_start = time.time()
    for i in range(0, ele, 1):
        temp = temp * x + a[ele - i - 1]
    time_end = time.time()
    Sum_time4.append(time_end - time_start)
print(Sum_time1)
print(Sum_time2)
print(Sum_time3)
print(Sum_time4)
