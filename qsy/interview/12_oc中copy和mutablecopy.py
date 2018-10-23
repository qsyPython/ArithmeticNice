'''
   非集合类、可变集合类和不可变集合类的copy和mutablecopy有什么区别？
   如果是集合内容复制的话，里面的元素也会一起复制吗？
   浅拷贝、单层深拷贝、完全深拷贝的区别？

   非集合类：nsstring、nsnumber
   可变集合类：nsmutableDictionary、nsmutableArray、nsmutableSet
   不可变集合类：nsDictionary、nsArray、nsSet
   1、
   非集合类：不可变进行copy是浅复制（指针地址不同，内存地址相同），mutableCopy是深复制，可变的copy，mutableCopy都是深复制（指针地址和内存地址都不同）
   不可变集合类：copy是浅复制，mutableCopy是单层深复制（指针地址不同，内存地址不同，元素地址相同）
   可变集合类：copy，mutableCopy都是单层深复制（指针地址不同，内存地址不同，元素地址相同）


- (void)copyAndMutableCopy{

NSMutableArray *mutableAry = [NSMutableArray arrayWithObjects:@"a",nil];

NSArray *ary = [NSArray arrayWithObjects:@"b",nil];

id copyMutableAry = [mutableAry copy];

id copyAry = [ary copy];

id mutableArymutableCopy = [mutableAry mutableCopy];

id mutableCopyAry = [ary mutableCopy];

NSLog(@"mutableAry:%@ ,内存地址%p -- 指针地址%p",mutableAry,mutableAry,&mutableAry);

NSLog(@"ary:%@ ,内存地址%p -- 指针地址%p",ary,ary,&ary);

NSLog(@"==================这是华丽丽的分割线==================");

NSLog(@"copyMutableAry:%@ ,内存地址%p -- 指针地址%p",copyMutableAry,copyMutableAry,©MutableAry);

NSLog(@"copyAry:%@ ,内存地址%p -- 指针地址%p",copyAry,copyAry,©Ary);

NSLog(@"==================这是华丽丽的分割线==================");

NSLog(@"mutableArymutableCopy:%@ ,内存地址%p -- 指针地址%p",mutableArymutableCopy,mutableArymutableCopy,&mutableArymutableCopy);

NSLog(@"mutableCopyAry:%@ ,内存地址%p -- 指针地址%p",mutableCopyAry,mutableCopyAry,&mutableCopyAry);

}

log

2017-08-10 16:04:40.287 Test[13049:755504] mutableAry:(a) ,内存地址0x61000004ce40 -- 指针地址0x7fff54dbfa58

2017-08-10 16:04:40.287 Test[13049:755504] ary:(b) ,内存地址0x61000000ff50 -- 指针地址0x7fff54dbfa50

2017-08-10 16:04:40.288 Test[13049:755504] ==================这是华丽丽的分割线==================

2017-08-10 16:04:40.288 Test[13049:755504] copyMutableAry:(a) ,内存地址0x61000000ff60 -- 指针地址0x7fff54dbfa48

2017-08-10 16:04:40.288 Test[13049:755504] copyAry:(b) ,内存地址0x61000000ff50 -- 指针地址0x7fff54dbfa40

2017-08-10 16:04:40.288 Test[13049:755504] ==================这是华丽丽的分割线==================

2017-08-10 16:04:40.288 Test[13049:755504] mutableArymutableCopy:(a) ,内存地址0x61000004cd20 -- 指针地址0x7fff54dbfa38

2017-08-10 16:04:40.288 Test[13049:755504] mutableCopyAry:(b) ,内存地址0x61000004ce10 -- 指针地址0x7fff54dbfa30

   2、集合（nsarray、nsdictionary、nsset）内容复制，集合里面的元素不会一起复制。

   3、
   浅复制也就是所说的指针复制，并没有进行对象/内存复制;
   单层深复制，也就是我们经常说的深复制，我这里说的单层深复制是对于集合类所说的(即NSArray,NSDictionary,NSSet)，单层深复制指的是只复制了该集合类的最外层，里边的元素没有复制，(即这两个集合类的地址不一样，但是两个集合里所存储的元素的地址是一样的);
   完全复制，指的是完全复制整个集合类，也就是说两个集合地址不一样，里边所存储的元素地址也不一样;

   4、若实现完全复制：
   集合类型：
   NSArray *copyArray = [[NSArray alloc] initWithArray:array copyItems:YES];  // 完全复制

   自定义对象：单层深复制
   遵守协议，实现协议方法：
   -(id)copyWithZone:(NSZone *)zone {
      CopyObject  *copy = [[[self class] alloc] init];
      copy.name = self.name;
      copy.mobile = self.mobile;
      copy.company = self.company;
      copy.descInfo = self.descInfo;
      return copy;
   }
'''