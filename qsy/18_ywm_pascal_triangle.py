'''
    显示杨辉三角
    输入数字，如9
    显示对应杨辉三角：
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

'''

def triangles(n):
    L,index=[1],0
    while index<n:# 每1行，第1个和最后1个是不变的为1；中间的数据为：newList 的i 和 i+1
        yield L
        L = [1]+[L[i] + L[i+1] for i in range(len(L)-1)]+[1]
        index += 1

def print_triangle():
    input_str = input('请输入数字：')
    flag = 1
    while flag:
        if input_str.isdigit(): # 字符串包含的都是数字
            flag = 0
            input_num = int(input_str)
            for item in triangles(input_num):
                print(item)
        else:
            flag = 1
            print('请输入数字！！！')
print(print_triangle())





