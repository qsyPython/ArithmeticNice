#
# 可变数组的遍历操作：remove
# 如下：可变数组a是动态变化的。i是递增的,
# 直接操作原list
a=[1,2,3,4,5]
# for i in a:
#     a.remove(i)
#     print(a)
# print ('最终结果:',a)

# 如何处理这种动态变化的list: 列表拷贝，然后对原列表进行删除操作就没问题了
# 遍历是拷贝的list，删除原有的list
a=[1,2,3,4,5]
for item in a[:]:
    a.remove(item)
print(a)
