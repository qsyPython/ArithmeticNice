# 一维数组的应用:
#     如给定的[27000,32000,32500,27500,30000,29000,31000,32500,30000,26000]
#
#     交互1、
#     用户输入1：表示 Display employee salary
#     用户输入2：表示 Modify employee salary
#     用户输入3：表示 Quit
#
#     交互2、
#     若交互1中输入的为1：用户还需要输入上面一维列表的位数，如输入1，对应着输出32000
#     若交互1中输入的为2：用户还需要输入上面一维列表的位数，如输入1，则再次增加输入交互3：新的薪水如38000，替换掉一维列表中的32000，返回
#     若交互1中输入的为3：直接返回

def display_employee_salary(array):
    is_success = True
    while is_success:
        op_num = input("请输入员工编号：")
        if op_num.isdigit() and int(op_num) >= 0 and int(op_num) < len(array):
            print(array[int(op_num)])
            is_success = False

def modify_employee_salary(array):
    is_success = True
    while is_success:
        op_num = input("请输入需要修改的员工编号：")
        if op_num.isdigit() and int(op_num) >= 0 and int(op_num) < len(array):
            op_salary = input("请输入工资：")
            array[int(op_num)] = op_salary
            is_success = False


if __name__ == '__main__':
     num = [27000,32000,32500,27500,30000,29000,31000,32500,30000,26000]
     print("一维数组的操作" + str(num))
     is_success = True
     while is_success:
        op_num = input("请输入(1显示员工工资*2修改员工工资*3推出)：")
        if int(op_num) == 1:
            display_employee_salary(num)
        elif int(op_num) == 2:
            modify_employee_salary(num)
        elif int(op_num) == 3:
            is_success = False





