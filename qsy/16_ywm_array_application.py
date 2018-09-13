'''
    一维数组的应用:
    如给定的[27000,32000,32500,27500,30000,29000,31000,32500,30000,26000]

    交互1、
    用户输入1：表示 Display employee salary
    用户输入2：表示 Modify employee salary
    用户输入3：表示 Quit

    交互2、
    若交互1中输入的为1：用户还需要输入上面一维列表的位数，如输入1，对应着输出32000
    若交互1中输入的为2：用户还需要输入上面一维列表的位数，如输入1，则再次增加输入交互3：新的薪水如38000，替换掉一维列表中的32000，返回
    若交互1中输入的为3：直接返回
'''

origin_list = [27000,32000,32500,27500,30000,29000,31000,32500,30000,26000]
print("输入1：表示 Display employee salary\n输入2：表示 Modify employee salary\n输入3：表示 Quit")

while 1:
    input_str = input("请输入数字:")
    if input_str is '1' or input_str is '2':
        while 1:
            input_num = input('请输入员工编号:') #条件：输入内容为整数 + 长度小于list总长
            if input_num.isdigit() and int(input_num) < len(origin_list):
                if input_str is '1':
                    print(origin_list[int(input_num)])
                else:
                    while 1:
                        input_salary = input('请输入新的工资:')
                        if input_salary.isdigit():
                            origin_list[int(input_num)] = int(input_salary)
                            print(origin_list)
                            break
                        else:
                            print('请输入正确的薪水数字！！！')
                            continue
                break
            else:
                print('请输入正确的员工编号！！！')
                continue
        break
    elif input_str is '3':
          print('Quit')
          break
    else:
        print('请按要求输入数字1或2或3')
        continue

