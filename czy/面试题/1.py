# 1、为什么说OC是一门动态语言？并写出对应代码对应来解释。

Objective-C 它将很多静态语言在编译和链接时期做的事放到了运行时来处理,主要有三种动态特性
1、动态类型：
即运行时再决定对象的类型。简单说就是id类型，任何对象都可以被id指针所指，只有在运行时
才能决定是什么类型。像内置的明确的基本类型都属于静态类型(int、NSString等)。
静态类型在编译的时候就能被识别出来。所以，若程序发生了类型不对应，编译器就会发出警告。
而动态类型就编译器编译的时候是不能被识别的，要等到运行时(runtime)，即程序运行的时候才会根据语境来识别。
在实际使用中，往往使用内省(introspection)来确定该对象的实际所属类：
id obj = someInstance;
if ([obj isKindOfClass:someClass])
{
    someClass *classSpecifiedInstance = (someClass *)obj;
    // Do Something to classSpecifiedInstance which now is an instance of someClass
    //...
}

-isMemberOfClass:是 NSObject的方法，用以确定某个 NSObject对象是否是某个类的成员。
与之相似的为 -isKindOfClass:，可以用以确定某个对象是否是某个类或其子类的成员。
这两个方法为典型的introspection方法。在确定对象为某类成员后，可以安全地进行强制转换，继续之后的工作。


2.动态绑定：

基于动态类型，在某个实例对象被确定后，其类型便被确定了。
该对象对应的属性和响应的消息也被完全确定，这就是动态绑定。
比如我们一般向一个NSObject对象发送-respondsToSelector:或者 -instancesRespondToSelector:
等来确定对象是否可以对某个SEL做出响应，而在OC消息转发机制被触发之前，
对应的类 的+resolveClassMethod:和+resolveInstanceMethod:将会被调用，
在此时有机会动态地向类或者实例添加新的方 法，也即类的实现是可以动态绑定的；isKindOfClass也是一样的道理。

void dynamicMethodIMP(id self, SEL _cmd)
{
    // implementation ....
}

/该方法在OC消息转发生效前被调用
+ (BOOL) resolveInstanceMethod:(SEL)aSEL
{
    if (aSEL == @selector(resolveThisMethodDynamically)) {
        //向[self class]中新加入返回为void的实现，SEL名字为aSEL，实现的具体内容为dynamicMethodIMP class_addMethod([self class], aSEL, (IMP) dynamicMethodIMP, “v@:”);
        return YES;
    }
    return [super resolveInstanceMethod:aSel];
}

当然也可以在任意需要的地方调用class_addMethod或method_setImplementation
（前者添加实现，后者替换实现），来完成动态绑定的需求。


3、动态加载

根据需求加载所需要的资源，这点很容易理解，对于iOS开发来说，
基本就是根据不同的机型做适配。最经典的例子就是在Retina设备上加载@2x的图片
，而在老一些的普通屏设备上加载原图。随着Retina iPad的推出，和之后可能的Retina Mac的出现，这个特性相信会被越来越多地使用。



二、列举出你项目中运用到的所有设计模式，并用代码简单实现

1、原型
原型模式使子类可以在客户端任意时刻进行复制，常见例如iOS的copy操作。


2、单例
保证一个类只有一个实例，并提供一个访问它的全局访问点
多线程下使用得注意，可能会创建多次
@interface Singleton: NSObject
+ (instancetype)shareInstance;
@ end

# import "Singleton.h"
@implementation Singleton

static Singleton * _instance = nil;

+(instancetype)shareInstance
{
static dispatch_once_t onceToken;
dispatch_once( & onceToken, ^ {
    _instance = [[self alloc] init];
});

return _instance;
}

@end

3、工厂方法
定义创建对象的接口，让子类决定实例化哪一个类。工厂方法使得一个类的实例化延迟到子类。
例如：定制多种样式UITableViewCell

@interface DZTableViewCellStyle1:UITableViewCell

@end
@ implementation DZTableViewCellStyle1

创建方法

@end

@interface DZTableViewCellStyle2:UITableViewCell

@end

@ implementation DZTableViewCellStyle2

创建方法

@end

@interface DZTableViewCellStyle3:UITableViewCell

@end

@ implementation DZTableViewCellStyle3

创建方法

@end

4、抽象工厂
抽象工厂提供一个固定的接口，用于创建一系列有关联或相依存的对象，而不必指定其具体类或其创建的细节。客户端与从工厂得到的具体对象之间没有耦合。

例如 NSNumber类


