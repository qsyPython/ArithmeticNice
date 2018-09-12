'''
   1、一维数组的倒置
   [5,4,3,2,1]
   变为：
   [1,2,3,4,5]
'''

# 逻辑：遍历；第1个和最后1个互换，依次递减1和加1后继续互换
def invert(array,start,end):
    while start<end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1
    return array

origin_list = [1,2,3,5]
print(invert(origin_list,0,len(origin_list)-1))