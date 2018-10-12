'''
    传值涉及到从前到后。
    前声明delegate、notification和block，从后到前，后声明delegate、notification和block
    都可以使用:5种
    property
    delegate:A中声明协议，声明代理属性；B中遵守协议，执行代理方法
    singleton：单例中持有某属性
    notification:注册给某对象；发布通知执行就ok
    block:A中重命名block，声明block属性，定义block；B中执行block
'''

