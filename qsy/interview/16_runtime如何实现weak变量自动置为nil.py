'''
    runtime如何实现weak变量自动置nil?
    runtime维护1个weak表，用于存储指向某个对象的所有weak指针。
    weak表时个哈希表，key是指向对象的指针，value是所有指向该对象的weak指针的地址构成的数组。
    当某对象的引用计数为0，遍历指向该对象的weak指针的地址所构成的数组，并置为nil。

    伪代码来一发：
    @property(nontomatic,weak)id<HashDelegate> delegate;
    或
    __weak id obj1 = obj;
    runtime维护着objc_storeWeak(value,key)，第1个参数为value：obj1的地址的数组，key为该对象obj的地址。
    若key对应obj为0，则会从变量的地址weak表中删除value！

'''