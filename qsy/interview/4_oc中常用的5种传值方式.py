'''
    传值涉及到从前到后 / 从后到前。
    用前到后传值：在前VC，声明delegate、notification和block；
    从后到前传值：在后VC，声明delegate、notification和block；

    都可以使用:5种
    property
    delegate: A中声明协议，声明代理属性；B中遵守协议，设置代理，执行代理方法
    singleton：单例中持有某属性或方法
    notification: 注册给某对象为观察者；发布通知，传递数据给观察者执行就ok。记得在addObserver的对象的类中，dealloc中remove

    block: A中重命名block，声明block属性，定义block；B中执行block块。
'''

