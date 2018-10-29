'''
  求2个数的最大公约数和最小公倍数
  给定a、b都大于0的整数

'''
# 最大公约数：辗转相除法
def max_common_divisor(a,b):
    while b:
        c = a % b
        a = b
        b = c
    return a

# 最小公倍数：最小公倍数 = 两整数的乘积 ÷ 最大公约数
def min_common_multiple(a,b):
    return int(a*b/max_common_divisor(a,b))

if __name__ == '__main__':
    print(max_common_divisor(2,4),min_common_multiple(2,9))
