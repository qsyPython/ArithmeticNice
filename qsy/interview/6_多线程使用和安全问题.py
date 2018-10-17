'''
   线程安全的问题：
   进程：运行中的应用程序，主要管理资源
   线程：进程的基本执行单位
   多线程：在同一时刻，一个CPU只能处理1条线程，但CPU可以在多条线程之间快速的切换，只要切换的足够快，就造成了多线程一同执行的假象。
   主线程: 处理UI，所有更新UI的操作都必须在主线程上执行。
   多线程的目的：1、耗时操作后台处理；2、CPU高效率使用

   多线程使用:NSThread、GCD、NSOperation。

   线程处理的基本原则：
   所有属性都是nonatomic；
   尽量避免多线程抢夺同一资源；
   尽量将加锁、资源抢夺的业务逻辑交给服务器端处理，减小移动客户端的压力
   线程安全问题：当多个线程访问同1块资源时，很容易引发数据错乱和数据安全问题.
    举例：
    NSInteger total = 0;
    # c *lock = [NLock new];
    - (void)threadNotSafe {
        for (NSInteger index = 0; index < 3; index++) {
            dispatch_async(dispatch_get_global_queue(0, 0), ^{
                # [lock lock];
                total += 1;
                NSLog(@"total: %ld", total);
                total -= 1;
                NSLog(@"total: %ld", total);
                # [lock unlock];
            });
        }
    }

线程安全问题的解决办法：(按照执行效率从低到高)
   1、自旋锁：使用原子属性atomic就是自旋锁，新的线程来了，会进入死循环，直到旧线程完成
   使用原子属性atomic，但atomic不是绝对的线程安全，假设有3个线程，一个线程进行写入操作，一个线程进行读取操作，最后一个线程进行写入操作。
   如果使用atomic，在读取完成之前，值可能会被篡改。这时候，可以使用栅栏块（dispatch_barrier_async）解决。

   OSSpinLock *lock = OS_SPINLOCK_INIT;
   OSSpinLockLock(&lock);
   // 需要执行的代码
   OSSpinLockUnlock(&lock);

   2、互斥锁: @synchronized，新的线程来了，会休眠。
   NSObject *object = [NSObject new];
   @synchronized(object){
        // 需要锁定的代码
   }

   3、线程锁：列出3种实现
   NSLock *lock = [NSLock new] 或 NSCondition *lock = [NSCondition new];
   [lock lock];
   // 需要锁定的代码
   [lock unlock];

    或
   dispatch_semaphore_t lock = dispatch_semaphore_create(1);    //传入的参数必须大于或者等于0，否则会返回Null
   long wait = dispatch_semaphore_wait(lock, DISPATCH_TIME_FOREVER);    //wait = 0，则表示不需要等待，直接执行后续代码；wait != 0，则表示需要等待信号或者超时，才能继续执行后续代码。lock信号量减一，判断是否大于0，如果大于0则继续执行后续代码；lock信号量减一少于或者等于0，则等待信号量或者超时。
   //需要锁定的代码
   long signal = dispatch_semaphore_signal(lock);    //signal = 0，则表示没有线程需要其处理的信号量，换句话说，没有需要唤醒的线程；signal != 0，则表示有一个或者多个线程需要唤醒，则唤醒一个线程。（如果线程有优先级，则唤醒优先级最高的线程，否则，随机唤醒一个线程。）


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