'''
   线程安全的问题：
   进程：运行中的应用程序，主要管理资源
   线程：进程的基本执行单位
   多线程：在同一时刻，一个CPU只能处理1条线程，但CPU可以在多条线程之间快速的切换，只要切换的足够快，就造成了多线程一同执行的假象。
   主线程: 处理UI，所有更新UI的操作都必须在主线程上执行。
   多线程的目的：1、耗时操作后台处理；2、CPU高效率使用

   线程处理的基本原则：
   所有属性都是nonatomic；
   尽量避免多线程抢夺同一资源；
   尽量将加锁、资源抢夺的业务逻辑交给服务器端处理，减小移动客户端的压力
   线程安全问题：当多个线程访问同1块资源时，很容易引发数据错乱和数据安全问题.

   线程安全问题的解决办法：
   1、自旋锁：使用原子属性atomic，新的线程来了，会进入死循环，直到旧线程完成
   使用原子属性atomic，但atomic不是绝对的线程安全，假设有3个线程，一个线程进行写入操作，一个线程进行读取操作，最后一个线程进行写入操作。
   如果使用atomic，在读取完成之前，值可能会被篡改。这时候，可以使用栅栏块（dispatch_barrier_async）解决。
   2、互斥锁: @synchronized，新的线程来了，会休眠。
   @synchronized(锁对象self){
        // 需要锁定的代码
   }

    # 对线程可进行的操作：
    1、获取当前线程
    [NSThread currentThread]; number为1，name为main表示主线程。
    [NSThread mainThread];获取主线程
    [NSThread isMainThread];是否是主线程
    [NSThread isMultiThreaded];判断当前线程是否是多线程
    2、休眠多久
    [NSThread sleepForTimeInterval:2];
    //休眠到指定时间
    [NSThread sleepUntilDate:[NSDate date]];
    3、强制退出线程
    [NSThread exit];

'''