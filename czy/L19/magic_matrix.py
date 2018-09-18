# 输入一个数字，如3
#     输出3*3的魔方阵，如：
#     8 1 6
#     3 5 7
#     4 9 2
#     魔方阵要求：若输入数字n，魔方阵中共有n*n个数字；同时，无论横排、竖排还是对角线中数字的和都是一样的

# 奇数阶魔方阵就是指行列数都是n（n>=3 且 n%2 == 1）的魔方阵
#
# 奇数阶魔方阵的数字规律
# 通过对奇数阶魔方阵的分析，其中的数字排列有如下的规律：
# （1）自然数1出现在第一行的正中间；
# （2）若填入的数字在第一行（不在第n列），则下一个数字在第n行（最后一行）且列数加1（列数右移一列）；
# （3）若填入的数字在该行的最右侧，则下一个数字就填在上一行的最左侧；
# （4）一般地，下一个数字在前一个数字的右上方（行数少1，列数加1）；
# （5）若应填的地方已经有数字或在方阵之外，则下一个数字就填在前一个数字的下方。（一般地，n的倍数的下一个数字是在该数的下方。）
# 按照上述的规律，我们来完成3阶的魔方阵：
# 第一步：将“1”填入1行2列的位置，即 （按规律（1））；
# 第二步：将“2”填入3 (最后) 行3 ( = 2 + 1 )列的位置，即 （按规律（2））；
# 第三步：将“3”填入2行1列的位置，即 （按规律（3））；
# 第四步：将“4”填入3行1列的位置（“3”的下面）；即 （按规律（5））
# 第五步：将“5”填入2行2列的位置；即 （按规律（4））；
# 第六步：将“6”填入1行3列的位置，即 （按规律（4））；
# 第七步：将“7”填入2行3列的位置（“6”的下面），即 （按规律（5））；
# 第八步：将“8”填入1行1列的位置，即 （按规律（3））；
# 第九步：将“9”填入3行2列的位置，即 （按规律（2））。
# 至此，一个3阶魔方阵构造完成了。

def magicMatrix(n):

    #创建2维数组
    nums = []
    for i in range(n):
        rows = [0] * n
        nums.append(rows);
    rowIndex = 0
    colIndex = 0

    #自然数1出现在第一行的正中间
    nums[0][int(n/2)] = 1
    rowIndex = 0
    colIndex = int(n/2)

    for i in range(2,n*n +1):
        #若填入的数字在第一行且不在最后n列，则下一个数字在第n列且列数加1
        if rowIndex == 0 and colIndex != n - 1:
            rowIndex = n - 1
            colIndex = colIndex + 1
            nums[rowIndex][colIndex] = i
            continue
        #若填入的数字在该行的最右侧且不在第一行，则下一个数字就在上一行的最左侧
        if colIndex == n - 1 and rowIndex != 0:
            rowIndex = rowIndex - 1
            colIndex = 0
            nums[rowIndex][colIndex] = i
            continue
        # 若应填的地方已经有数字或者在方阵之处，则下一个数字就填在前一个数字的下方
        # 一般的n的倍数的下一个数字是在该数的下方
        if rowIndex == 0 or colIndex == n -1 or nums[rowIndex -1][colIndex + 1] != 0:
            rowIndex = rowIndex + 1
            nums[rowIndex][colIndex] = i
        else:  #一般的，下一个数字在前一个数字的右上方（行数减1，列数加1）
            rowIndex -= 1;
            colIndex += 1;
            nums[rowIndex][colIndex] = i;

    for i in range(n):
        print(nums[i])


if __name__ == '__main__':

    magicMatrix(3)





