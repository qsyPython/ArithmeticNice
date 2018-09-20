# 3维数组的表示
# 输入：给定2个3维数组，按照对应位置获取拿到对应和的值，不同位置的补零处理，并输出一个新的3维数组

import numpy as np

def one_dimensional_add(array1,array2):
    one_dimensional = []
    if len(array1) > len(array2):
        for i in range(len(array1)):
            if i < len(array2):
              one_dimensional.append(array1[i]+array2[i])
            else:
              one_dimensional.append(array1[i])
    elif len(array1) < len(array2):
        for i in range(len(array2)):
            if i < len(array1):
              one_dimensional.append(array1[i]+ array2[i])
            else:
              one_dimensional.append(array2[i])
    else:
        one_dimensional = list(add_dimensional(array1,array2))

    return one_dimensional

def two_dimensional_add(array1,array2):
    two_dimensional = []
    if len(array1) > len(array2):
        for i in range(len(array1)):
            if i < len(array2):
                two_dimensional.append(one_dimensional_add(array1[i], array2[i]))
            else:
                two_dimensional.append(array1[i])
    elif len(array1) < len(array2):
        for i in range(len(array2)):
            if i < len(array1):
                two_dimensional.append(one_dimensional_add(array1[i], array2[i]))
            else:
                two_dimensional.append(array2[i])
    else:
        for i in range(len(array1)):
            two_dimensional.append(array1[i], array2[i])

    return two_dimensional

def three_dimensional_add(array1, array2):
    three_dimensional = []
    if len(array1) > len(array2):
        for i in range(len(array1)):
            if i < len(array2):
                three_dimensional.append(two_dimensional_add(array1[i], array2[i]))
            else:
                three_dimensional.append(array1[i])
    elif len(array1) < len(array2):
        for i in range(len(array2)):
            if i < len(array1):
                three_dimensional.append(two_dimensional_add(array1[i], array2[i]))
            else:
                three_dimensional.append(array2[i])
    else:
        for i in range(len(array1)):
            three_dimensional.append(array1[i], array2[i])

    return three_dimensional


def add_dimensional(left = list, right = list):
    if left is None:
        return right
    elif right is None:
        return left
    return  np.array(left) + np.array(right)


if __name__ == '__main__':

    a = [[[1,2,3]]]
    b = [[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]

    print(three_dimensional_add(a,b))














