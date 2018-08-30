# 对下列数据进行升序排序：[12,34,7,9,1,90,27,46,93,61,52,40]
# 要求：写5种以上的排序算法，并写出对应的时间和空间复杂度，（5种排序算法必须包含：快排排序法）

#交换排序 冒泡排序算法
#传统方法 #时间复杂度 平均O(n^2) 最好情况 O(n) 最坏情况 O(n^2) 空间复杂度O(1)
def bubbleSort(array):
    length = len(array)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return  array;

# 升级版冒泡排序法：通过从低到高选出最大的数放到后面，
# 再从高到低选出最小的数放到前面，如此反复，直到左边界和右边界重合。
# 当数组中有已排序好的数时，这种排序比传统冒泡排序性能稍好。
#时间复杂度 平均O(n^2) 最好情况 O(n) 最坏情况 O(n^2) 空间复杂度O(1)
# def bubbleSort(array):
#
#     left = 0
#     right = len(array) - 1
#     while left < right:
#         for i in  range(left,right):
#             if array[i] > array[i + 1]:
#                 temp = array[i]
#                 array[i] = array[i + 1]
#                 array[i + 1] = temp
#         right -= 1
#
#         for j in reversed(range(left + 1,right + 1)):
#             if array[j + 1] < array[j]:
#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp
#         left += 1
#
#     return  array;

#.快速排序
# 选取一个基准元素，通常为数组最后一个元素（或者第一个元素）。
# 从前向后遍历数组，当遇到小于基准元素的元素时，把它和左边第一个大于基准元素的元素进行交换。
# 在利用分治策略从已经分好的两组中分别进行以上步骤，直到排序完成。
# 时间复杂度 平均O(nlogn) 最好情况 O(nlogn) 最坏情况 O(n^2) 空间复杂度O(1)
#互换元素
# def swap(array,x,y):
#     temp = array[x]
#     array[x] = array[y]
#     array[y] = temp
#
# #遍历元素
# def patition(array,left,right):
#     j = left  #遍历数组
#     i = j - 1  #用来指向小于基准的位置
#     key = array[right] #基准元素 从左到右遍历数组，把小于等于基准元素的放到左边，大于基准元素的放到右边
#     while j < right:
#         if array[j] <= key:
#             i = i + 1
#             swap(array,j,i)
#         j += 1
#     i = i + 1
#     swap(array,right,i)
#     return i
#
# def quickSort(array,left,right):
#     if left < right:
#         mid = patition(array,left,right)
#         quickSort(array,left,mid - 1)
#         quickSort(array, mid + 1, right)

#插入排序  直接插入排序
#和交换排序不同的是它不用进行交换操作，而是用一个临时变量存储当前值。
# 当前面的元素比后面大时，先把后面的元素存入临时变量，前面元素的值放到后面元素位置，再到最后把其值插入到合适的数组位置
#时间复杂度 平均O(n^2) 最好情况 O(n) 最坏情况 O(n^2) 空间复杂度O(1)


# def insertSort(array):
#     temp = 0;
#     length = len(array)
#     for i in range(1,length):
#         j = i - 1
#         if array[i] < array[j]:
#             temp = array[i]
#             array[i] = array[j]
#             while temp < array[j - 1]:
#                 array[j] = array[j - 1]
#                 j -= 1
#             array[j] = temp

#希尔(shell)排序
#在直接插入排序的思想下设置一个最小增量dk,刚开始dk设置为n/2。
# 进行插入排序，随后再让dk=dk/2,再进行插入排序，直到dk为1时完成最后一次插入排序，此时数组完成排序。
#时间复杂度 平均 O(nlogn) - O(n^2) 最好情况 O(n^1.3) 最坏情况 O(n^2) 空间复杂度O(1)
# def insertsort(array,length,dk):
#     for i in range(dk,length):
#         j = i - dk
#         if array[i] < array[j]:
#             temp = array[i]
#             array[i] = array[j]
#             while array[j] > temp:
#                 array[j + dk] = array[j]
#                 j -= dk;
#             array[j + dk] = temp
#
#
# def shellSort(array):
#     length = len(array)
#     dk = int(length/2)
#     while dk >= 1:
#         insertsort(array,length,dk)
#         dk = int(dk/2)

# 选择排序 直接选择排序
#依次选出数组最小的数放到数组的前面。
# 首先从数组的第二个元素开始往后遍历，找出最小的数放到第一个位置。
# 再从剩下数组中找出最小的数放到第二个位置。以此类推，直到数组有序
#时间复杂度 平均 O(n^2) 最好情况 O(n^2) 最坏情况 O(n^2) 空间复杂度O(1)
# def selectsort(array):
#     for i in range(len(array)):
#        key = i  #临时变量用于存放数组最小值的位置
#        for j in range(i + 1,len(array)):
#            if array[j] < array[key]:
#                key = j
#        if key != i:
#         temp = array[key]
#         array[key] = array[i]
#         array[i] = temp

#归并排序
#归并算法应用到分治策略，
# 简单说就是把一个答问题分解成易于解决的小问题后一个个解决，
# 最后在把小问题的一步步合并成总问题的解。
# 这里的排序应用递归来把数组分解成一个个小数组，直到小数组的数位有序，
# 在把有序的小数组两两合并而成有序的大数组。
##时间复杂度 平均 O(nlogn) 最好情况 O(nlogn) 最坏情况 O(nlogn) 空间复杂度O(n)
# def merge(array,left,mid,right):
#     len = right - left + 1   #数组长度
#     temp = []
#     k = 0
#     i = left  #前一数组的起始元素
#     j = mid + 1  # 后一数组的起始元素
#     while i <= mid and j <= right:
#         if array[i] <= array[j]:
#             temp[k] = array[i]
#             i += 1
#         else:
#             temp[k] = array[j]
#             j += 1
#         k += 1
#
#
#     while i <= mid:
#         temp[k] = array[i]
#         k += 1
#         i += 1
#     while j <= right:
#         temp[k] = array[j]
#         k += 1
#         j += 1
#     for z in range(len):
#         array[left] = temp[z]
#         left += 1

# def mergeSort(array,left,right):
#     if left != right:
#         mid = int((left + right)/2)
#         mergeSort(array, left,mid)
#         mergeSort(array, mid + 1, right)
#         merge(array,left, mid, right)

def main():
    array = [1,7,3,10,33,44,12]
    print(bubbleSort([1,7,3,10,33,44,12]))
   # quickSort(array,0,len(array) - 1)
   # insertSort(array)
   # shellSort(array)
   # selectsort(array)
   # mergeSort(array,0,len(array)-1)
   # print(array)

if __name__ == '__main__':
    main()