# 一维数组的高级应用
# 设计一个可容纳40位数的求n!
#     输入：某个数字n
#     输出：该数字的n!,
#     并要求n!的结果在40位以内
#
#     例如：
#     输入：12
#     输出：
#         1!= 1
#         2!= 2
#         3!= 6
#         4!= 24
#         5!= 120
#         6!= 720
#         7!= 5040
#         8!= 40320
#         9!= 362880
#         10!= 3628800
#         11!= 39916800
#         12!= 479001600

def factorial(N):
    data = [0]*40
    digit = 0
    i = j = r = k = 0
    data[0] = 1
    data[1] = 1
    digit = 1
    i = 1
    while i < N + 1:

        j = 1
        while j < digit + 1:
            data[j] =  data[j]* i
            j += 1

        j = 1
        while j < digit + 1:
            if data[j] > 10:
                data[j + 1] += int(data[j]/10)
                data[j] = data[j]%10
            j += 1

        if(data[digit + 1] > 0):
            digit += 1

        print("\n%d！= " %(i),end = " ")

        k = digit
        while k > 0:
            print(data[k],end = " ")
            k -= 1
        i += 1
if __name__ == '__main__':
    factorial(4)


















