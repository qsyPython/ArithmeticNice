'''
    循环引用产生、查询和解决

    如何查询是否循环引用？ dealloc是否被执行

    1、delegate: 使用strong ，而非weak会导致
    self.delegate = self;
    代理持有 self，self同时持有该delegate，就会导致无法释放
    解决：采用weak弱引用delegate，weak修饰的变量在释放后自动指向nil，防止野指针存在。

    2、block
    循环引用：若是调用该block的某对象持有该block + 在block中直接使用该对象 / 对象的变量 == 这样就会导致循环引用！！！

    typedef void(^MyBlock)() myBlock
    @property(nonomatic,copy)myBlock *myBlock;
    self.myBlock = ^(){
        [self getName];
    };
    解决：__weak typeof(self)weakSelf = self;
    然后block中 __strong typeof(weakSelf) strongSelf = weakSelf;//加一下强引用，避免weakSelf被释放掉
    使用strongSelf。
    当__weak修饰的对象weakSelf被系统回收时, 它的内存地址会自动指向nil，而不再指向self。
    __unsafe_unretained 修饰的对象，当weakSelf被系统回收时, 它的内存地址不会自动指向nil。出现发生野指针错误！

    3、timer 当一个对象中持有timer时，该对象若是被销毁前未进，停止timer和置为nil处理，该对象和timer之间就会造成循环引用。
    解决：
    对象self remove前
    [self.timer invalidate];
    self.timer = nil;

    4、单例内部持有某控制器：
    单例本身是一个会一旦创建，一直存在的。当持有某控制器时，控制器被pop后，仍无法持有。
    解决：
    单例中不要持有控制器，哈哈哈
'''

