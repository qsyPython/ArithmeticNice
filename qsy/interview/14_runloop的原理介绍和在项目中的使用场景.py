'''
    runloop的原理介绍和在项目中的使用场景：
    1、runloop介绍：
        程序启动的时候会开辟一个mainThread并将该线程添加到runloop中，并默认是开启状态：保证mainThread不被销毁，程序持续运行。
        保证能处理程序中各种事件；当应用处于休眠状态时，释放资源，提高系统运行效率。
        iOS 系统中，提供了两种RunLoop：NSRunLoop（OC封装后的API，线程不安全） 和 CFRunLoopRef(C的API，线程安全)

    2、runloop的使用场景：
            1、runloop和线程一对一。保持线程的存活，而不是线性的执行完任务就退出了
                不开启RunLoop的线程 、开启RunLoop的线程
            2、让线程在我们需要的时候响应消息：runloop安排执行哪一块代码
            3、让线程定时执行某任务：timer
            4、监听Observer达到一些目的：

    3、runloop和线程的关系：runloop和thread是一对一的关系，保存在全局字典中。
            thread本身不会自动创建runloop；对应线程结束时，runloop会被销毁。
            主线程 默认 开启runloop
            子线程没有，需要我们手动获取runloop以后，将子线程添加到runloop中。

    4、为什么把NSTimer对象以NSDefaultRunLoopMode模式 添加到主运行循环以后，
      滑动scrollview的时候，NSTimer却不动了？
      原则：苹果是保证界面优先的原则 + 除CommonMode外，不在同一runloop模式下代码的运行会暂停。
      当滑动时，runloop会切换到 UITrackingRunLoopMode，而NSTimer对象所在的runloop模式为NSDefaultRunLoopMode。
      UITrackingRunLoopMode是当前滑动的runloop模式，而NSDefaultRunLoopMode是timer的runloop的模式，就会出现暂停的现象。

      如何解决这个问题：把 NSTimer的模式改为 KCFRunloopCommonModes就可以了，兼容的runloop模式


'''