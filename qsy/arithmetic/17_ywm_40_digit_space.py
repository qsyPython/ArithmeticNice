'''
    一维数组的高级应用：
    设计一个可容纳40位数的求n!: n的阶乘
    输入：某个数字n
    输出：该数字的n!,
    并要求n!的结果在40位以内

    例如：
    输入：12
    输出：
        1!= 1
        2!= 2
        3!= 6
        4!= 24
        5!= 120
        6!= 720
        7!= 5040
        8!= 40320
        9!= 362880
        10!= 3628800
        11!= 39916800
        12!= 479001600
'''
# 逻辑 -> 遍历打印结果： 条件判断num为0和1时的阶乘

# 条件：num >1
def get_digit_factorial(num):
    result_num = 1
    for i in range(1,num+1):
        result_num = result_num*i
    return result_num

def factorial_ergodic(num):
    if num == 0 or num == 1:
        print('%s!=1'%num)
    else:
        for i in range(1,num+1):
            result_num = get_digit_factorial(i)
            print(type(result_num))
            if len(str(result_num)) <= 40:
                print('%s!=%s' % (i,result_num))
            else:
                break

flag = 1
while flag:
    input_str = input('请输入数字：')
    if input_str.isdigit():
        input_num = int(input_str)
        factorial_ergodic(input_num)
        flag = 0
    else:
        print('请输入正确数字')
        flag = 1




