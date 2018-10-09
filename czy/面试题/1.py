# 1、为什么说OC是一门动态语言？并写出对应代码对应来解释。
# Objective-C 它将很多静态语言在编译和链接时期做的事放到了运行时来处理，例如可以通过Runtime 这个运行时机制，
# 在运行时动态的添加变量、方法、类等，所以说Objective-C 是一门动态的语言
#
#
# `objc_object`是表示一个类的实例的结构体，它的定义如下(`objc/objc.h`)：
# ```objc
# struct objc_object {
#     Class isa  OBJC_ISA_AVAILABILITY;
# };
# typedef struct objc_object *id;
#
# 可以看到，这个结构体只有一个字体，即指向其类的isa指针。
# 这样，当我们向一个Objective-C对象发送消息时，运行时库会根据实例对象的isa指针找到这个实例对象所属的类。
# Runtime库会在类的方法列表及父类的方法列表中去寻找与消息对应的selector指向的方法。找到后即运行这个方法。
#