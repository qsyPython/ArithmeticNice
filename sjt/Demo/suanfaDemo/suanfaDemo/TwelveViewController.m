//
//  TwelveViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/7.
//  Copyright © 2018年 sjt. All rights reserved.
/***
 *两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
 
 给出两个整数 x 和 y，计算它们之间的汉明距离。
 
 注意：
 0 ≤ x, y < 231.
 
 示例:
 
 输入: x = 1, y = 4
 
 输出: 2
 
 解释:
 1   (0 0 0 1)
 4   (0 1 0 0)
        ↑   ↑
 
 上面的箭头指出了对应二进制位不同的位置。
 */

#import "TwelveViewController.h"

@interface TwelveViewController ()
@property (nonatomic ,strong)NSMutableArray * array;
@property (nonatomic ,assign)NSInteger num;
@end

@implementation TwelveViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.array=[NSMutableArray arrayWithCapacity:0];
    _num=0;
    [self sendNumberx:1 widthY:4];
}

- (void)sendNumberx:(NSInteger)x widthY:(NSInteger)y{
    //得到x的二进制
    [self loadNumber:x];
    NSMutableArray * xarray=[NSMutableArray arrayWithArray:self.array];
    [self.array removeAllObjects];
    //得到y的二进制
    [self loadNumber:y];
    NSMutableArray * yArray=[NSMutableArray arrayWithArray:self.array];
    [self.array removeAllObjects];
    //得到两个二进制的最大长度
    NSInteger maxCount = xarray.count>=yArray.count?xarray.count:yArray.count;
    
    xarray=[self loadMaxArray:xarray withMax:maxCount];
    yArray=[self loadMaxArray:yArray withMax:maxCount];
    
    for (NSInteger i=0; i<maxCount; i++) {
        NSString * xstr=xarray[i];
        NSString * ystr=yArray[i];
        if (![ystr isEqualToString:xstr]) {
            _num++;
        }
    }
    NSLog(@"%ld****%ld****距离:%ld",x,y,_num);
}

- (NSMutableArray *)loadMaxArray:(NSMutableArray *)array withMax:(NSInteger)max{
    NSInteger tempIndex = max-array.count;
    if (tempIndex==0) {
        return array;
    }
    
    for (NSInteger i =0; i<tempIndex; i++) {
        [array addObject:@"0"];
    }
    
    return array;
}

- (void)loadNumber:(NSInteger)index{
    if (index==0) {
        return;
    }
    NSInteger shang = index/2;
    NSInteger yushu = index%2;
    [self.array addObject:[NSString stringWithFormat:@"%ld",yushu]];
    [self loadNumber:shang];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
