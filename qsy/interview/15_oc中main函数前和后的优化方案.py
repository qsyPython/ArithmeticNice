'''
    iOS main函数前和main函数后的优化方案？
    main函数之前：
    A、main函数之前都干了什么？
        1、系统先读取App的可执行文件(Mach-O文件)，获得dyld（动态链接器）的路径，加载dyld，然后剩下的就交给dyld来处理了，去初始化运行环境。
        2、开启缓存策略，加载程序相关依赖库(其中也包含我们的可执行文件)，并对这些库进行链接，最后调用每个依赖库的初始化方法，在这一步，runtime被初始化。
        3、当所有依赖库的初始化后，轮到最后1位(程序可执行文件：Mach-O文件)进行初始化，在这时runtime会对项目中所有类进行类初始化，然后调用所有的load方法。
        4、最后dyld返回main函数地址，main函数被调用，来到程序入口main函数

        总结main函数前的过程：
        读取Mach-O文件，获得dyld路径，dyld加载初始化环境；
        加载程序相关的依赖库，建立链接，并调用每个库的初始化方法，该过程初始化runtime
        依赖库初始化后，初始化Mach-O文件，该过程中runtieme会对所有类初始化，调用所有load方法
        dyld返回main函数地址p%，main函数被调用，来到程序入口main函数

        介绍：Mach-O文件是OS X与iOS系统上的可执行文件格式。
                MachOView 查看，支持的Mach-O文件有：
                1、Executable：应用的主要二进制 也就是我们常说的app！
                2、Dylib Library：动态链接库（又称DSO或DLL）
                3、Static Library：静态链接库
                4、Bundle：不能被链接的Dylib，只能在运行时使用dlopen()加载，可当做macOS的插件
                5、Relocatable Object File ：可重定向文件类型
        Mach-O文件用Mach-OView打开后的结构3层：
        Header：该文件运行的平台、文件类型、LoadCommands的个数等
        LoadCommands：加载各种命令：程序所需的dyld的文件路径(dyld的路径在LC_LOAD_DYLINKER命令里，一般都是在/usr/lib/dyld路径下)，以及相关依赖库的文件路径（动态库和静态库），main函数的加载地址。
        Data：具体的代码和数据

    B、如何优化：
        iOS 中用到的所有系统framework都是动态，类比成插头和插排，静态链接的代码在编译后的静态链接过程就将插头和插排一个个插好，这时候需要链接好
        代码越少越好啊

        如何获取一个工程所有的动态库（dylib、系统framework等）？
            1、Build Phases-> Link Library With Libraries
            2、隐含的动态库：活动检测器 -> 搜到该app，打开文件和端口,取样获取app的路径 -> 通过otool -L 项目名称
        动态库：代码共用（内存和硬盘都只有1份） 、 易于维护（执行时才link，容易更新） 和 执行体积小（动态链接编译时不需要打包）

        如何查看dyld（动态链接器）的执行过程？
        dyld 是开源的，可以对照源码 https://github.com/opensource-apple/dyld 查看不同函数
        给项目添加符号断点：_objc_init 运行项目就ok
        结果：在栈底的dyldbootstrap::start()方法，继而调用了dyld::_main()方法

        如何给mach-o插入动态库？
        获取插入的库：在项目中设置环境变量 DYLD_PRINT_ENV为1，来打印该sEnv的值，搜索：DYLD_INSERT_LIBRARIES 可获取插入的库
        那我们想要插入对应的动态库，只需要修改：DYLD_INSERT_LIBRARIES，就可以实现代码注入，hook












    main函数之后：

'''
