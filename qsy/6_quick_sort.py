'''
    排序：
    对下列数据进行升序排序：[12,34,7,9,1,90,27,46,93,61,52,40]
    要求：5种以上的排序方法，要求写出对应的时间和空间复杂度，（5种排序算法必须包含：快排）

    😁😁😁排序方法😁😁😁 --->>>
    直接插入排序：Straight Insertion Sort ✔
    二分法插入排序： Binary Sort
    希尔排序：Shell Sort
    直接选择排序：Straight Select Sort
    堆排序：Heap Sort
    交换排序：Swap Sort
    快速排序：Quick Sort   快速排序被认为是20世纪十大算法之一  ✔
    基数排序：Radix Sort
    归并排序：Merge sort
    冒泡排序：Bubble Sort ✔️


'''
import random

# 冒泡排序：内循环 相邻数据比较后移位。
# 时间复杂度：O(N2)
# 空间复杂度为O(1)：额外空间是tmp开辟的空间。
# 临时变量所占空间不随处理数据n的大小改变而改变。占用的空间是固定的！！！所以，是O(1)
def bubble_sort(origin_list):
    for i,item_i in enumerate(origin_list):
        for j,item_j  in enumerate(origin_list):
            if j<len(origin_list)-1-i and origin_list[j] > origin_list[j+1]:
                tmp = origin_list[j]
                origin_list[j] = origin_list[j+1]
                origin_list[j+1] = tmp
    return origin_list

print(bubble_sort([12,34,7,9,9,1,90,27,46,93,61,52,40]))


# 直接插入排序：Straight Insertion Sort
def straight_insertion_sort(origin_list):
    for i,item_i in enumerate(origin_list):
        for j,item_j in enumerate(origin_list):
            if origin_list[i] < origin_list[j]:
                temp = origin_list[i]
                origin_list[i] = origin_list[j]
                origin_list[j] = temp
    return origin_list
print(straight_insertion_sort([12, 34, 7, 9, 9, 1, 90, 27, 46, 93, 61, 52, 40]))


# 二分法插入排序： Binary Sort
def binary_sort(origin_list):
    for i,item_i in enumerate(origin_list):
        start = 0
        end = i - 1
        middle = 0
        temp = origin_list[i]
        while start < end:
            middle = (start + end)//2
            if origin_list[middle] > temp:
                end = middle - 1
            else:
                start = middle + 1
        for j,item_j in enumerate(origin_list):
            j = i - 1
            while j> end :
                origin_list[j+1] = origin_list[i]
                j -=1
        origin_list[end+1] = temp
print(binary_sort([12, 34, 7, 9, 9, 1, 90, 27, 46, 93, 61, 52, 40]))

# 快速排序算法：快排三种实现方式
# 1.快排的核心：“分趟”。就是“每一趟”下来，找到某1个元素应该待的位置，这个元素一般被称为pivot；
# 2.再分别对pivot前后两部分进行递归排序
# 平均时间复杂度为O(NlogN)

def quick_sort(origin_list,left,right): #递归内部不能调用含有变量的数据，除非：加单次执行的逻辑处理
    if left < right:
        # pivot = pivot_last_sort(origin_list,left,right)
        # pivot = pivot_first_sort(original_list,left,right)
        pivot = pivot_first_sort(origin_list, left, right)
        quick_sort(origin_list,left,pivot-1)
        quick_sort(origin_list,pivot+1,right)

# 实现方式1、固定位置：选取第1个元素 或最后1个元素
def pivot_first_sort(origin_list,left,right):
    key = original_list[left]
    while left < right:
        while left < right and original_list[right]>key:
            right -=1
        original_list[left] = original_list[right]
        while left < right and original_list[left]<=key:
            left +=1
        original_list[right] = original_list[left]
    original_list[left] = key
    return left

# 选取list中最后1个元素所在的基准位 pivot：以最后1个元素为基准，并返回该在位置
def pivot_last_sort(origin_list,left,right):
    key = origin_list[right] #获取最后1个元素，临时保留该数据
    while left < right:
        while left < right and origin_list[left] <= key:# 获取比 key大的左边位数
            left +=1
        origin_list[right] = origin_list[left] # 将左边该大值赋值到右侧
        while left <right and origin_list[right]>key: # 获取比 key小的右边位数
            right -=1
        origin_list[left] = origin_list[right]# 将右边该小值赋值到左侧
    origin_list[right] = key
    return right

# 2、随机取值基准：将该随机数移动到头 或 尾
# 先处理随机数和交换到头或尾：然后调用pivot_first_sort 或 pivot_last_sort

original_list = [12, 34, 7, 9, 9, 1, 90, 27, 46, 93, 61, 52, 40]
quick_sort(original_list,0,len(original_list)-1)
print(original_list)




