'''
  多项式求值:加减乘除
  分别实现多项式求值的四种运算，若针对不同规模的输入值a
  ，各算法的运行时间，问题规模n
  分别取10，50，100，150，200，300，400，500，10000，20000，50000，100000时绘制四种算法运行时间的比较图。
'''
import numpy as np
import time,math,random

n = [10,50,100,150,200,300,400,500]
x = 1.2
sum_time1 = []
sum_time2 = []
sum_time3 = []
sum_time4 = []
for item in n:
    # polyval
    a = np.random.random(item)
    p = np.poly1d(a)
    time_start = time.time()
    temp = np.polyval(p, x)
    time_end = time.time()
    sum_time1.append(time_end - time_start)
    # 遍历
    temp = float('Inf')
    time_start = time.time()
    for i in range(0, item, 1):
        temp = temp + a[i] * x**i
    time_end = time.time()
    sum_time2.append(time_end - time_start)

    #
    time_start = time.time()
    q = 1
    for i in range(0, item, 1):
        q = q * x
        temp = temp + a[i] * q
    time_end = time.time()
    sum_time3.append(time_end - time_start)

    #
    time_start = time.time()
    for i in range(0, item, 1):
        temp = temp * x + a[item - i - 1]
    time_end = time.time()
    sum_time4.append(time_end - time_start)
print(sum_time1,'\n',sum_time2,'\n',sum_time3,'\n',sum_time4)
