'''
    runloop的原理介绍和在项目中的使用场景：

    runloop介绍：
        iOS 系统中，提供了两种RunLoop：NSRunLoop（OC封装后的API，线程不安全） 和 CFRunLoopRef(C的API，线程安全)

    runloop的使用场景：
        1、保持线程的存活，而不是线性的执行完任务就退出了
            不开启RunLoop的线程 、开启RunLoop的线程
        2、让线程在我们需要的时候响应消息
        3、让线程定时执行某任务
        4、监听Observer达到一些目的

'''