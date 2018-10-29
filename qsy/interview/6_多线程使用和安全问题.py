'''
   1、多线程使用:NSThread、GCD、NSOperation。
   进程：运行中的 应用程序，主要管理资源
   线程：进程的基本 执行单位
   多线程：在同一时刻，一个CPU只能处理1条线程，但CPU可以在多条线程之间快速的切换，只要切换的足够快，就造成了多线程一同执行的假象。
   主线程: 处理UI，所有更新UI的操作都必须在主线程上执行。
   多线程的目的：1、耗时操作后台处理；2、CPU高效率使用，4核

   # 对线程可进行的操作（NSThread）：
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

   线程处理的基本原则：
   所有属性都是nonatomic（非线程安全）；
   尽量避免多线程抢夺同一资源；
   尽量将加锁、资源抢夺的业务逻辑交给服务器端处理，减小移动客户端的压力

   2、线程安全问题：当多个线程访问同1块资源时，很容易引发数据错乱和数据安全问题.
    举例：
    - (void)threadNotSafe {
    NSInteger total = 0;
    # c *lock = [NSLock new];
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

   线程安全问题的解决办法：(简单介绍：按照执行效率从低到高)
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

  3、线程安全的面试问题：参考：https://www.jianshu.com/p/70f97716881e 和 https://blog.csdn.net/qq_30513483/article/details/53814482
  谈下iOS开发中知道的哪些锁? 哪个性能最差?SD和AFN使用的哪个?
 一般开发中你最常用哪个? 哪个锁apple存在问题又是什么问题?
 锁：
@synchronized 关键字互斥锁：很常用，性能最差；无需创建锁、隐式的添加异常处理例程，若异常时会自动释放互斥锁，对于不想手动处理异常处理例程可选该锁；性能最差！！！
NSLock 互斥锁：性能较好，比较常用；但不能递归或循环多次调用lock方法，会造成死锁：线程A在lock某段代码后，未unlock，导致线程B一直等待，无法访问，造成阻塞！！！
    NSRecursiveLock 递归锁：升级版的NSLock，递归会追踪每次lock，每次lock后，都会平衡调用unlock。解决了NSLock 互斥锁的死锁。
    NSCondition：根据条件进行等待和唤醒线程。对应api：wait，signal（唤醒一个等待的线程），broadcast（唤醒所有线程）。进入等待状态，场景：按某顺序执行多个线程
    NSConditionLock 条件锁：根据condition进行切换lock和unlock，对应api：lockWhenCondition 、unlockWithCondition；场景：按某顺序执行多个线程
    pthread_mutex 互斥锁（C语言）：没啥好说的，就是C语言的实现，对应api：pthread_mutex_lock(&mutex)、pthread_mutex_unlock(&mutex);
dispatch_semaphore 信号量锁（GCD）：常用，使用如下。
信号量：就是一种可用来控制访问资源的数量的标识，设定了一个信号量，在线程访问之前，加上信号量的处理，则可告知系统按照我们指定的信号量数量来执行多个线程。
信号量signal：值表示，同一时间，最多几个资源（线程）可被访问，内部已实现了锁的机制。
常用场景：异步处理图片时，防止cpu从吃不消，限制最大线程数 = signal的初始化值。
=========================🙋🙋🙋🙋🙋🙋🙋🙋🙋============================================================

    dispatch_semaphore_t signal = dispatch_semaphore_create(1); //传入值必须 >=0, 若传入为0则阻塞线程并等待timeout,时间到后会执行其后的语句；
    dispatch_time_t overTime = dispatch_time(DISPATCH_TIME_NOW, 3.0f * NSEC_PER_SEC);// DISPATCH_TIME_FOREVER 表示不需要传值

    //线程1
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
    NSLog(@"线程1 等待ing");
    dispatch_semaphore_wait(signal, overTime); //signal 值会 -1
    NSLog(@"线程1");
    dispatch_semaphore_signal(signal); //signal 值会 +1
    NSLog(@"线程1 发送信号");
    NSLog(@"--------------------------------------------------------");
       });

    //线程2
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
    NSLog(@"线程2 等待ing");
    dispatch_semaphore_wait(signal, overTime);
    NSLog(@"线程2");
    dispatch_semaphore_signal(signal);
    NSLog(@"线程2 发送信号");
    });

理解信号量：停车场剩余4个车位，那么即使同时来了四辆车也能停的下。如果此时来了五辆车，那么就有一辆需要等待。
信号量的值（signal）就相当于剩余车位的数目，dispatch_semaphore_wait函数就相当于来了一辆车，dispatch_semaphore_signal就相当于走了一辆车。
停车位的剩余数目在初始化的时候就已经指明了（dispatch_semaphore_create（long value）），调用一次 dispatch_semaphore_signal，剩余的车位就增加一个；调用一次dispatch_semaphore_wait 剩余车位就减少一个；
当剩余车位为 0 时，再来车（即调用 dispatch_semaphore_wait）就只能等待。有可能同时有几辆车等待一个停车位。有些车主没有耐心，给自己设定了一段等待时间，这段时间内等不到停车位就走了，如果等到了就开进去停车。
而有些车主就像把车停在这，所以就一直等下去。
=========================🙋🙋🙋🙋🙋🙋🙋🙋🙋============================================================

    OSSpinLock：性能最好，但有问题，苹果已废弃。iOS中维护了 5 个不同的QoS(线程优先级):background，utility，default，user-initiated，user-interactive。
    线程优先级的原则：高优先级线程始终会在低优先级线程前执行，一个线程不会受到比它更低优先级线程的干扰。
    问题：如果一个低优先级的线程获得锁并访问共享资源，这时一个高优先级的线程也尝试获得这个锁，它会处于 spin lock 的忙等状态从而占用大量 CPU。
    低优先级线程占用锁，由于高优先级线程占用着CPU，从而导致第优先级线程的任务迟迟完不成、无法释放 lock


AFN3.1 .0: 使用@synchronized、NSlock 、和 dispatch_semaphore_t信号量实现加锁
SDWebImage: 使用@synchronized

    4、ios下如何实现指定线程数目的线程池？



'''