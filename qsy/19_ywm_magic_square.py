'''
    魔方阵
    输入一个数字，如3
    输出3*3的魔方阵，如：
    8 1 6
    3 5 7
    4 9 2
    魔方阵要求：魔方阵中共有n*n个数字；数字不重复使用；同时，无论横排、竖排还是对角线所有数字的和都是一样的。
'''

def magic_square():
    flag = 1
    while flag:
        input_str = input('请输入数字：')
        if input_str.isdigit():
            n = int(input_str)
            flag = 0
            row,col = 0,n//2
            magic = []
            for i in range(n):
                magic.append([0]*n)
            magic[row][col] = 1
            for i in range(2,n*n+1):
                r, l = (row - 1 + n) % n, (col + 1) % n
                if (magic[r][l] == 0):
                    row, col = r, l
                else:
                    row = (row + 1) % n
                magic[row][col] = i
            # 输出
            t = len(str(n * n))  # 计算n*n的位数
            for i in magic:
                for j in i:
                    print("%-*d" % (t, j), end="  ")  # 左对齐，占位是t
                print("")
        else:
            flag = 1
            print('请输入数字！！！')

magic_square()
