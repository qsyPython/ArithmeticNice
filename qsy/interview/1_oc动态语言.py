# 1、为什么说OC是一门动态语言？并写出对应代码对应来解释。
# runtime：
# 动态类型：只有在运行时才会确定真正的类型，如id
[self viedidLoad];
# id obj = someInstance;
# if [obj isKindOfClass:someclass] { #isKindOfClass 类和子类；isMemberOfClass 当前类
#    someClass *classSpecifiedInstance = (someClass *)obj;
#    // do something
# }

# 动态绑定：只有在运行时，才会确定执行什么方法。
# 面向过程：传统的函数一般在编译时就已经把sel和IMP打包到编译后的源码中了
# 面向对象：OC最常使用的是消息机制objc_msgSend(id, SEL, ...)：调用1个实例的方法，所做的是向该实例的指针发送消息，实例在收到消息后，从自身的实现中寻找响应这条消息的方法

# 动态绑定：在实例所属类确定后，将某些属性和相应的方法绑定到实例上，包括原来类已实现的 + 通过runtime实现的。
# sel 和 imp 互换
# class_addMethod(添加方法)  和  method_setImplementation（交换实现）
# 在Cocoa层，我们一般向一个NSObject对象发送-respondsToSelector:或者-instancesRespondToSelector:等来确定对象是否可以对某个SEL做出响应
# 下面是决议，当该对应实例指针确定后，实例收到消息会，从自身实现中未找到对应的方法，就会走如下的决议:
# void dynamicMethodIMP(id self, SEL _cmd){
#     // do something
# }
#
# +(BOOL)resolveInstanceMethod:(SEL)aSEL {
#   if (aSEL == @selector(resolveThisMethodDynamically)){
#      class_addMehtod([self class],aSEL,(IMP)dynamicMethodIMP,"v@:")
#      return YES;
# }
#  return [super resolveInstanceMethod:aSEL]
# }
#

# 动态载入：程序在运行时，根据需要再加载可执行的代码和资源
# 根据不同的机型做适配。在Retina设备上加载@2x的图片，普通屏设备上加载原图
