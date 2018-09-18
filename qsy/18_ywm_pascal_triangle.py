'''
    显示杨辉三角
    输入数字，如4
    显示对应杨辉三角：
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

'''
# 获取某具体的某一行的list数据:每一行是上一行中倒3角中2个数字之和
# 思路：每一组数据都是list，要用list，该list要动态变化，以及赋值给自己，要用到到while，while内部加yield可提前走出，
# 如何记录上一组数据？list 操作后再次赋值给list就ok
# 如何执行一次操作后中断进行别的操作？while内部加yield L可提前走出

def triangles(n):
    L,index=[1],0
    while index<n:# 每1行，第1个和最后1个是不变的为1；中间的数据为：newList 的i 和 i+1
        yield L # 跳出函数并返回L
        L = [1]+[(L[i] + L[i+1]) for i in range(len(L)-1)]+[1]
        index += 1

def print_triangle():
    input_str = input('请输入数字：')
    flag = 1
    while flag:
        if input_str.isdigit(): # 字符串包含的都是数字
            flag = 0
            input_num = int(input_str)
            origin_list = triangles(input_num+1)
            for item in origin_list:
                print(item)
        else:
            flag = 1
            print('请输入数字！！！')

print_triangle()





