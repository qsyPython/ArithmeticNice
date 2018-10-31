
//
//  ViewController.m
//  图片缓存练习
//
//  Created by 辛忠志 on 2017/9/1.
//  Copyright © 2017年 辛忠志. All rights reserved.
//
#define kSCREEN_WIDTH  [UIScreen mainScreen].bounds.size.width
#define kSCREEN_HEIGHT [UIScreen mainScreen].bounds.size.height


#import "ViewController.h"
#import "UIImageView+WebCache.h"
@interface ViewController ()
/*
 所展示的四张图片
 */
@property (weak, nonatomic) IBOutlet UIImageView *firstImage;
@property (weak, nonatomic) IBOutlet UIImageView *secondImage;
@property (weak, nonatomic) IBOutlet UIImageView *thirdImage;
@property (weak, nonatomic) IBOutlet UIImageView *fourthImage;

/*
 当前缓存大小
 */
@property (weak, nonatomic) IBOutlet UILabel *acheSize;

@end

@implementation ViewController



static NSString * firstURL = @"http://img.pconline.com.cn/images/upload/upc/tx/photoblog/1510/14/c16/13960684_1444828487538.jpg";
static NSString * secondURL = @"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1504497579654&di=8216d01feec023deb165ef77564e4756&imgtype=0&src=http%3A%2F%2Fimg.pconline.com.cn%2Fimages%2Fupload%2Fupc%2Ftx%2Fphotoblog%2F1404%2F09%2Fc1%2F32928837_1397005965583.jpg";
static NSString * thirdURL = @"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1504497742352&di=1d930dcfad527fb80f62e696e4cbd54b&imgtype=0&src=http%3A%2F%2Fpic15.nipic.com%2F20110730%2F7689559_151457143162_2.jpg";
static NSString * fouthURL = @"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1504497742352&di=1d930dcfad527fb80f62e696e4cbd54b&imgtype=0&src=http%3A%2F%2Fpic15.nipic.com%2F20110730%2F7689559_151457143162_.jpg";




#pragma mark - ---------- Lazy Loading（懒加载） ----------

#pragma mark - ----------   Lifecycle（生命周期） ----------
- (void)viewDidLoad {
    [super viewDidLoad];
}
#pragma mark - ---------- Private Methods（私有方法） ----------

#pragma mark initliaze data(初始化数据)

#pragma mark config control（布局控件）

#pragma mark networkRequest (网络请求)



#pragma mark IBActions （点击事件xib）
/*没有有占位图的加载方式*/
- (IBAction)noPlaceholder:(UIButton *)sender {
    [self.firstImage sd_setImageWithURL:[NSURL URLWithString:[NSString stringWithFormat:@"%@",firstURL]]];
}
/*有占位图的加载方式*/
- (IBAction)placeholderImage:(UIButton *)sender {
    //给一张默认图片，先使用默认图片，当图片加载完成后再替换
    [self.secondImage sd_setImageWithURL:[NSURL URLWithString:[NSString stringWithFormat:@"%@",secondURL]] placeholderImage:[UIImage imageNamed:@"占位350-350"]];
}
/*有占位图的加载方式 并且实现回调Block完成下一步任务*/
- (IBAction)placeholderBlock:(UIButton *)sender {
    [self.thirdImage sd_setImageWithURL:[NSURL URLWithString:[NSString stringWithFormat:@"%@",thirdURL]] placeholderImage:[UIImage imageNamed:@"占位350-350"] completed:^(UIImage *image, NSError *error, SDImageCacheType cacheType, NSURL *imageURL) {
        NSLog(@"图片加载完成后做的事情");
    }];
}
/*使用可更换optionsType的加载方式
 
                    -------------Options 枚举下的加载方式-----------
 SDWebImageRetryFailed 默认情况下，当URL无法下载时，URL就会被列入黑名单，这样库就不会继续尝试了。此标记禁用此黑名单。
 SDWebImageLowPriority  默认情况下，图像下载是在UI交互过程中启动的，这标志禁用该特性，导致在UIScrollView减速方面延迟下载。
 SDWebImageCacheMemoryOnly  此标记禁用磁盘缓存
 SDWebImageProgressiveDownload 此标志可以进行渐进式下载，在下载过程中，图像会逐步显示，就像浏览器所做的那样。默认情况下，图像只显示一次完全下载。
 SDWebImageRefreshCached  即使缓存了映像，也要尊重HTTP响应缓存控制，并在需要的情况下从远程位置刷新映像。磁盘缓存将由NSURLCache来处理，而不是使用SDWebImage，这会导致轻微的性能下降。这个选项有助于处理在同一个请求URL后面更改的图像，例如Facebook图形api概要图。如果刷新了缓存的图像，那么完成块就会被缓存的图像和最后的图像再次调用一次。只有当你不能用嵌入的缓存破坏参数使你的url静态时，才使用这个标志。
 SDWebImageContinueInBackground  在iOS 4+中，如果应用程序进入后台，可以继续下载图片。这是通过请求系统在后台获得额外的时间来完成请求完成的。如果后台任务过期，操作将被取消。
 SDWebImageHandleCookies 通过设置NSMutableURLRequest来处理存储在NSHTTPCookieStore中的cookie。HTTPShouldHandleCookies =是的;
 SDWebImageAllowInvalidSSLCertificates  启用不受信任的SSL证书。用于测试目的。在生产中使用谨慎。
 SDWebImageHighPriority 默认情况下，图像按顺序装载在队列中。这个标志把它们移到队列的前面。
 SDWebImageDelayPlaceholder  默认情况下，在图像加载时加载占位符图像。此标志将延迟加载占位符图像，直到图像完成加载。
 SDWebImageTransformAnimatedImage   我们通常不会在动画图像上调用transformdownloade昏暗委托方法，因为大多数转换代码会把它搞砸。无论如何，使用这个标志来转换它们。* /
 SDWebImageAvoidAutoSetImage  默认情况下，图像会在下载后添加到imageView中。但是在某些情况下，我们想要在设置图像之前有手(例如，应用一个过滤器或将它添加到交叉衰减动画中)使用这个标记如果你想在成功完成时手工设置图像
 SDWebImageScaleDownLargeImages  默认情况下，图像会被解码，以尊重它们原来的大小。在iOS上，这一标志将把图像缩小到与设备受限内存兼容的大小。*如果“SDWebImageProgressiveDownload”标志设置禁用缩减。
 */
- (IBAction)optionsType:(UIButton *)sender {
    /*  
     注：这里我用这个加载方式的时候特意试了下如果两张图片的流是一样的SDImage会做什么判断，结果如我所料，如果两个URL流是一致的话那么图片缓存的大小是不会增加
     */
    [self.fourthImage sd_setImageWithURL:[NSURL URLWithString:[NSString stringWithFormat:@"%@",fouthURL]] placeholderImage:[UIImage imageNamed:@"占位350-350"] options:SDWebImageRetryFailed];
}
/*清理图片缓存按钮*/
- (IBAction)clearAche:(UIButton *)sender {
    /*
     异步清除所有磁盘缓存映像。非阻塞方法-立即返回。@param完成一个应该在缓存过期后执行的块(可选)
     
     注意:这里要注意[[SDImageCache sharedImageCache] clearDisk];方法会报错，下面clearDiskOnCompletion的方法会替代上面的方法
     */
    [[SDImageCache sharedImageCache] clearDiskOnCompletion:^{
        
    }];
    
    /*
     Clear all memory cached images --->清除所有缓存镜像
     */
    [[SDImageCache sharedImageCache] clearMemory];
    
    /*
     异步将所有过期的缓存映像从磁盘中删除。非阻塞方法-立即返回。@param completionBlock在缓存过期后执行(可选)--->故名思义他是不能删除你当前缓存的大小的
     */
    [[SDImageCache sharedImageCache] deleteOldFilesWithCompletionBlock:^{
        
    }];
}
/*计算当前缓存大小*/
- (IBAction)acheSize:(UIButton *)sender {
    
    CGFloat size = [[SDImageCache sharedImageCache] getSize];
    NSLog(@"%f",size);
    NSString *message = [NSString stringWithFormat:@"SDImage size %.2fB。", size];
    NSLog(@"%@",message);
    if (size > (1024 * 1024))
    {
        size = size / (1024 * 1024);
        message = [NSString stringWithFormat:@"SDImage size %.2fM。", size];
    }
    else if (size > 1024)
    {
        size = size / 1024;
        message = [NSString stringWithFormat:@"SDImage size %.2fKB。", size];
    }
    self.acheSize.text = message;
    [[[UIAlertView alloc] initWithTitle:nil message:message delegate:nil cancelButtonTitle:nil otherButtonTitles:@"知道了", nil] show];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
