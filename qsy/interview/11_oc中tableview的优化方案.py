'''
    tableview的优化方案都有哪些？

1、cell重用：
    # 创建复用标识
    static NSString *reuseID = “reuseCellID”;
    // 缓存池中取已经创建的cell
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:reuseID];
    if(!cell) {
        cell = [[UITableViewCell alloc] init];
    }
   若能够查询到，否则，返回nil；而且需要判断if（cell == nil），才会创建Cell。
   所以：不推荐上述方式

   优化方案：
   建议使用：先注册cell，若注册失败会从模型中
   - (void)registerNib:(nullable UINib *)nib forCellReuseIdentifier:(NSString *)identifier NS_AVAILABLE_IOS(5_0);
   - (void)registerClass:(nullable Class)cellClass forCellReuseIdentifier:(NSString *)identifier NS_AVAILABLE_IOS(6_0);
   再使用：
   -(__kindof UITableViewCell *)dequeueReusableCellWithIdentifier:(NSString *)identifier forIndexPath:(NSIndexPath *)indexPath NS_AVAILABLE_IOS(6_0);



2、定义一种(尽量少)类型的Cell及善用hidden隐藏(显示)subviews，而不是创建后手动添加subview
    把所有不同类型的view都定义好，放在cell里面，通过hidden显示、隐藏，来显示不同类型的内容。
    毕竟，在用户快速滑动中，只是单纯的显示、隐藏subview比实时创建要快得多

3、提前计算并缓存Cell的高度：
    可以创建一个frame模型，提前计算每个Cell的高度，并放到数据源中。
    cell创建中只负责赋值；
    - (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
        ContacterTableCell *cell = [tableView dequeueReusableCellWithIdentifier:@"ContacterTableCell"];
        if (!cell) {
            cell = (ContacterTableCell *)[[[NSBundle mainBundle] loadNibNamed:@"ContacterTableCell" owner:self options:nil] lastObject];
        }
        FrameModel *model = self.dataList[indexPath.row];
        [cell setContentInfo:model];
        return cell;
    }

    heightForRowAtIndexPath 只负责cell高度计算；
    - (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath {
        FrameModel *model = self.dataList[indexPath.row];
        return model.height;
    }

4、异步绘制（自定义Cell绘制）：适用于复杂点如朋友圈、微博的图文混排
    // 重写drawRect方法就不需要用GCD异步线程了，因为drawRect本来就是异步绘制的
        - (UIView *)drawRect {
                    //异步绘制
            dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
                    CGRect rect = [_data[@"frame"] CGRectValue];
                    UIGraphicsBeginImageContextWithOptions(rect.size, YES, 0);
                    CGContextRef context = UIGraphicsGetCurrentContext();
            //整个内容的背景
                    [[UIColor colorWithRed:250/255.0 green:250/255.0 blue:250/255.0 alpha:1] set];
                    CGContextFillRect(context, rect);
            //转发内容的背景
                    if ([_data valueForKey:@"subData"]) {
                        [[UIColor colorWithRed:243/255.0 green:243/255.0 blue:243/255.0 alpha:1] set];
                        CGRect subFrame = [_data[@"subData"][@"frame"] CGRectValue];
                        CGContextFillRect(context, subFrame);
                        [[UIColor colorWithRed:200/255.0 green:200/255.0 blue:200/255.0 alpha:1] set];
                        CGContextFillRect(context, CGRectMake(0, subFrame.origin.y, rect.size.width, .5));
                    }

                    {
                //名字
                        float leftX = SIZE_GAP_LEFT+SIZE_AVATAR+SIZE_GAP_BIG;
                        float x = leftX;
                        float y = (SIZE_AVATAR-(SIZE_FONT_NAME+SIZE_FONT_SUBTITLE+6))/2-2+SIZE_GAP_TOP+SIZE_GAP_SMALL-5;
                        [_data[@"name"] drawInContext:context withPosition:CGPointMake(x, y) andFont:FontWithSize(SIZE_FONT_NAME)
                                         andTextColor:[UIColor colorWithRed:106/255.0 green:140/255.0 blue:181/255.0 alpha:1]
                                            andHeight:rect.size.height];
                //时间+设备
                        y += SIZE_FONT_NAME+5;
                        float fromX = leftX;
                        float size = [UIScreen screenWidth]-leftX;
                        NSString *from = [NSString stringWithFormat:@"%@  %@", _data[@"time"], _data[@"from"]];
                        [from drawInContext:context withPosition:CGPointMake(fromX, y) andFont:FontWithSize(SIZE_FONT_SUBTITLE)
                               andTextColor:[UIColor colorWithRed:178/255.0 green:178/255.0 blue:178/255.0 alpha:1]
                                  andHeight:rect.size.height andWidth:size];
                    }
            //将绘制的内容以图片的形式返回，并调主线程显示
            UIImage *temp = UIGraphicsGetImageFromCurrentImageContext();
                    UIGraphicsEndImageContext();
                    dispatch_async(dispatch_get_main_queue(), ^{
                        if (flag==drawColorFlag) {
                            postBGView.frame = rect;
                            postBGView.image = nil;
                            postBGView.image = temp;
                        }
            }
            //内容如果是图文混排，就添加View，用CoreText绘制
            [self drawText];
            }}

        }

5、滑动时，按需加载：
    - (void)scrollViewDidEndDragging:(UIScrollView *)scrollView willDecelerate:(BOOL)decelerate

    - (void)scrollViewDidEndDecelerating:(UIScrollView *)scrollView {
    //获取可见部分的Cell
    NSArray *visiblePaths = [self.tableView indexPathsForVisibleRows];
            for (NSIndexPath *indexPath in visiblePaths)
            {
            //获取的dataSource里面的对象，并且判断加载完成的不需要再次异步加载
                 <code>
            }
    }
    // tableView 停止滑动的时候异步加载图片
    - (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath

             if (self.tableView.dragging == NO && self.tableView.decelerating == NO)
                {
                   // 开始异步加载图片
                    <code>
             }

6、尽量少用或不用透明图层

7、减少subviews的数量

8、在heightForRowAtIndexPath:中尽量不使用cellForRowAtIndexPath:


9、cell中异步线程加载的图片，随滑动时，异步操作过多时：
# 在scrollerView的代理方法中，didEndDragging,didEndDeceleratiing方法中去完成图片异步加载的操作，tableView滑动的时候不做加载。
# didReceiveMemoryWarning方法中释放掉所有的子线程
# 在dealloc方法中将所有的delegate手动设置nil

10、iOS中cell图片圆角处理改成CPU：操作执行 ---> 一般图片处理都是在CGPU完成，GPU会在当前的在屏幕缓冲区外新开辟一个缓冲区
imageView.layer.cornerRadius = 10;
imageView.layer.masksToBounds = YES;

方案是：改为CPU完成切圆角工作（如下）或 imageview控件重载drawRect:方法

CGSize size = self.bounds.size;

CGFloat scale = [UIScreen mainScreen].scale;

CGSize cornerRadii = CGSizeMake(cornerRadius, cornerRadius);

UIGraphicsBeginImageContextWithOptions(size, NO, scale);

if(nil == UIGraphicsGetCurrentContext()) {

return;

}

UIBezierPath *cornerPath = [UIBezierPath bezierPathWithRoundedRect:self.bounds byRoundingCorners:rectCornerType cornerRadii:cornerRadii];

[cornerPath addClip];

[image drawInRect:self.bounds];

self.image = UIGraphicsGetImageFromCurrentImageContext();

UIGraphicsEndImageContext();

}

10、尽量使用代码，而不是xib

11、不透明的控件设定opaque = YES，这样子可以避免无用的alpha通道合成，降低GPU负载

'''