# 3维数组的表示
# 输入：给定2个3维数组，按照对应位置获取拿到对应和的值，不同位置的补零处理，并输出一个新的3维数组

import numpy as np

def threeDimensional(left = list, right = list):
    if left is None:
        return right
    elif right is None:
        return left
    return  np.array(left) + np.array(right)


if __name__ == '__main__':

    a = [[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]
    b = [[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]
    leftLegth = len(a)
    rightLegth = len(b)
    max = leftLegth;
    if leftLegth > rightLegth:
        max = leftLegth;
        for i in range(rightLegth,leftLegth):
            b.append([])
    elif leftLegth < rightLegth:
        max = rightLegth;
        for i in range(leftLegth,rightLegth):
            a.append([])

    for i in range(max):
        leftTwoArray = a[i]
        rightTwoArray = b[i]
        leftLegth = len(a[i])
        rightLegth = len(b[i])
        max = leftLegth;
        if leftLegth > rightLegth:
            max = leftLegth;
            for j in range(rightLegth, leftLegth):
                b[i].append([])
        elif leftLegth < rightLegth:
            max = rightLegth;
            for j in range(leftLegth, rightLegth):
                a[i].append([])

        for j in range(max):
            leftThreeArray = a[i][j]
            rightThreeArray = b[i][j]
            leftLegth = len(a[i][j])
            rightLegth = len(b[i][j])
            max = leftLegth
            if leftLegth > rightLegth:
                max = leftLegth
                for k in range(rightLegth, leftLegth):
                    b[i][j].append(0)
            elif leftLegth < rightLegth:
                max = rightLegth
                for k in range(leftLegth, rightLegth):
                    a[i][j].append(0)

    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(a[i])):
            c[i].append([])
            for k in range(len(a[j])):
                print(threeDimensional(a[i][j],b[i][j]))
                c[i][j].append(list(threeDimensional(a[i][j],b[i][j])))

    print(a)
    print(b)
    print(c)















