'''
   删除排序数组中的重复项：

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

'''

def delete_sort_array(origin_list):
    if len(origin_list) == 0:
        return 0
    elif len(origin_list) == 1:
        return 1
    else:
        for index,item in enumerate(origin_list[:]):
            if index+1 < len(origin_list):
                if origin_list[index] == origin_list[index+1]:
                    origin_list.pop(index)
        return len(origin_list)
print(delete_sort_array([1,1,5,5,6,6,13,14]))





