# 一维数组的倒置
#    [5,4,3,2,1]
#    变为：
#    [1,2,3,4,5]
# 将字符串第个和最后一个互换,依次递减，直到中间值为止
def invert(array,p,length):
    if not array is None:
        for i in range(int(length / 2)):
            temp = array[i + p]
            array[i + p] = array[length + p - 1 - i]
            array[length + p - 1 - i] = temp

if __name__ == '__main__':
    arr_num = [3,2,1,6,0,5]
    print (arr_num)
    invert(arr_num,0,len(arr_num))
    print (arr_num)
