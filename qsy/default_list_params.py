'''
    python函数参数中带有默认参数list
    默认参数：为可变数据时，调用一次后会被记录。所以，再次调用数据会出现问题。
'''
def f(x,origin_list = []):
    for i in range(x):
        origin_list.append(i*i)
    return origin_list
# print(f(4))
# print(f(5))

# 解决办法 ：1、每次传递时，都修改传递的默认参数
print(f(4,origin_list=[]))
print(f(5,origin_list=[]))

# 解决办法 ：2、默认参数为None，即传递的不再是可变参数，而是不可变的参数None
def f(x,origin_list=None):
    if origin_list is None:
        origin_list = []
    for i in range(x):
        origin_list.append(i*i)
    return origin_list
print(f(4))
print(f(5))

# 解决办法 ：3、传递 *a形式的可变参数
# 但带来一个问题：*origin_list 当作参数时，origin_list的元素会被装配成类型为 tuple,tuple无法进行 写 的操作，需要在内部转为list
def f(x,*origin_list):
    origin_list = list(origin_list)
    for i in range(x):
        origin_list.append(i*i)
    return origin_list
print(f(4,*[]))
print(f(5,*[]))









