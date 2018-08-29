'''
    排序：
    对下列数据进行升序asc排序：[12,34,7,9,1,90,27,46,93,61,52,40]
    要求：5种以上的排序方法，要求写出对应的时间和空间复杂度

    😁😁😁排序方法😁😁😁 --->>>
    直接插入排序：Straight Insertion Sort ✔
    二分法插入排序： Binary Sort
    希尔排序：Shell Sort
    直接选择排序：Straight Select Sort
    堆排序：Heap Sort
    交换排序：Swap Sort
    快速排序：Quick Sort
    基数排序：Radix Sort
    归并排序：Merge sort
    冒泡排序：Bubble Sort ✔️


'''
# 冒泡排序：内循环 相邻数据移位
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
            if j == i - 1 and j > end:
                origin_list[j+1] = origin_list[j]
                j -=1
        origin_list[end+1] = temp
print(binary_sort([12, 34, 7, 9, 9, 1, 90, 27, 46, 93, 61, 52, 40]))
# 快速排序算法：快排三种实现方式
# 1、选取第1个元素 或者 最后2个元素作为基准
# 2、随机取值基准的方法
# 3、三数取中方法：




