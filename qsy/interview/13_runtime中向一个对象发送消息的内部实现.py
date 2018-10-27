'''
    objc在向一个对象发送消息时，发生了什么？
    消息发送机制/消息分发机制、消息补救机制
'''

# 例如：[objc sendMessage:param1];
# 先转换为 runtime 的 objc_msgSend(id,SEL...)
# 1、先通过isa指针确定该对象（动态类型）分类优先级高于本类
# 2、获取到具体某动态类后，根据SEL，获取到对应的method，然后根据method从该类的 常用methods缓存 中寻找该method，若有就执行该method的IMP；没有见3
# 3、若没有，就会去该类的methodslist查找，若有执行找到的method的IMP；没有见4
# 4、若没有，会从该类的父类中，按2和3的查找顺序开始查找，若有就执行，若没有就会继续找该父类的父类，重复2和3，直到NSObject，若到NSObject时，就执行；没有见5
# 5、若还是没有，就会有触发发送消息的补救机制：
#    5.1、先走决议方法,拦截了该selector,并自定义实现IMP：+ (BOOL)resolveInstanceMethod:(SEL)sel; 或 + (BOOL)resolveClassMethod:(SEL)sel; 若对应动态类中实现了该方法，就执行，若没有，就走下面5.2
#    5.2、再走快速转发，直接交给代理对象来处理：- (id)forwardingTargetForSelector:(SEL)aSelector; 若对应动态类中实现了该方法，就执行，若没有，就走下面5.3
#    5.3、再走正常转发，签名selector和参数，返回该签名不为nil后，转给其他对象处理：- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector; - (void)forwardInvocation:(NSInvocation *)anInvocation;  若对应动态类中实现了该方法，就执行，若没有，见6
# 6、抛出异常："xxx unrecognized selector sent to instance 0x100...." 程序crash