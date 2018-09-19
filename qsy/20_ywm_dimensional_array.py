'''
    3维数组求和的表示：
    输入：给定2个3维数组，按照对应位置获取拿到对应和的值，不同位置的补零处理，并输出一个新的3维数组
    [5,2,3]
    [[5,2,3],[4,5,6]]
    c = [[[5,2,3],[4,5,6]],[[0,7,8],[10,10,9],[10,3,3]]]
    d = [[[5,8]],[[10,3,2],[0,0,1]]]
'''


# 2维数组 -> 转化为结果全为0的二维数组
# def double_convert(origin_list):
#     des_list = []
#     for arr in origin_list:
#         des_inner_list = []
#         for item in arr:
#             des_inner_list.append(0)
#         des_list.append(des_inner_list)
#     return des_list

# 1维list处理:返回处理后的1维list的对应和:
def handle_first_list(arr1,arr2):
    des_first_arr = []
    if len(arr1) > len(arr2):
        for index,item in enumerate(arr1):
            if index <= len(arr2)-1:
                des_first_arr.append(item + arr2[index])
            else:
                des_first_arr.append(item)
    elif len(arr1)< len(arr2):
        for index,item in enumerate(arr2):
            if index <= len(arr1)-1:
                des_first_arr.append(item + arr1[index])
            else:
                des_first_arr.append(item)
    else:
        for index,item in enumerate(arr1):
            des_first_arr.append(item + arr2[index])
    return des_first_arr
print(handle_first_list([1,3,5],[0,2]))

# 2维list处理:返回处理后的2维list的对应和:
def handle_double_list(arr1,arr2):
    des_double_arr = []
    if len(arr1) > len(arr2):
        for index, item in enumerate(arr1):
            if index <= len(arr2) - 1:  # 缺少的直接补到2维list中
                des_double_arr.append(handle_first_list(item,arr2[index]))
            else:
                des_double_arr.append(item)
    elif len(arr1) < len(arr2):
        for index, item in enumerate(arr2):
            if index <= len(arr1) - 1:  # 缺少的直接补到2维list中
                des_double_arr.append(handle_first_list(item,arr1[index]))
            else:
                des_double_arr.append(item)
    else:
        for index,item in enumerate(arr1):
            des_double_arr.append(handle_first_list(item,arr2[index]))
    return des_double_arr

print(handle_double_list([[1, 3, 5], [0, 2]],[[4,2]]))

# 3维list处理
def dimensional_list(arr1,arr2):
    dimen_list = []
    if len(arr1) > len(arr2):
        for index,item in enumerate(arr1):
           if index <= len(arr2)-1: # 缺少的直接补到3维list中
               dimen_list.append(handle_double_list(item,arr2[index]))
           else:
               dimen_list.append(item)
    elif len(arr1) < len(arr2):
        for index,item in enumerate(arr2):
           if index <= len(arr1)-1: # 缺少的直接补到3维list中
               dimen_list.append(handle_double_list(item,arr1[index]))
           else:
               dimen_list.append(item)
    else: # list中个数相等
        for index,item in enumerate(arr1):
            dimen_list.append(handle_double_list(item,arr2[index]))
    return  dimen_list


print(dimensional_list([[[5,2,3],[4,5,6]],[[0,7,8],[10,10,9],[10,3,3]]],[[[5,8]],[[10,3,2],[0,0,1]]]))

