
# 获取一个数各个位置上的字数,转为字符串后再强转为list
def get_loc_num(num):
    num_str = str(num)
    loc_list = list(num_str)
    return loc_list

def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    natural_list = []
    if left != right:
        pass
        # for i in range(left, right):
    else:
        temp = get_loc_num(left)
        is_natural = False
        for i in temp:
            if left%i != 0:
                is_natural = False
                break








print(selfDividingNumbers(123,123))