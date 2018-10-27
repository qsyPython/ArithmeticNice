'''
   图片的缓存策略：分别对比下afn和sd的图片缓存策略，最后设计1套比较完备可行的图片缓存策略

   1、afn的图片缓存策略：1级缓存，只做了内存缓存。根据NSUrlcache,key为url，value为图片

   2、sd的图片缓存策略：采用2级缓存 -> NSCache 做内存缓存; 然后是本地缓存
      NSCache 是一个类似于可变字典的集合类。
      AutoPurgeCache是其子类。在初始化时，监听UIApplicationDidReceiveMemoryWarningNotification 通知，在收到内存警告时，会自动移除其中的所有对象，缓解内存压力。

   3、图片缓存策略：
      经常变动：无需缓存
      几乎不变：果断缓存
      偶尔变化：设置时限缓存，定期缓存和清除

'''