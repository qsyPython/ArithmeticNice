
//
//  ThitySevenViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/10/23.
//  Copyright © 2018年 sjt. All rights reserved.
/***
 给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。
 
 示例 1:
 
 输入: candies = [1,1,2,2,3,3]
 输出: 3
 解析: 一共有三种种类的糖果，每一种都有两个。
 最优分配方案：妹妹获得[1,2,3],弟弟也获得[1,2,3]。这样使妹妹获得糖果的种类数最多。
 示例 2 :
 
 输入: candies = [1,1,2,3]
 输出: 2
 解析: 妹妹获得糖果[2,3],弟弟获得糖果[1,1]，妹妹有两种不同的糖果，弟弟只有一种。这样使得妹妹可以获得的糖果种类数最多。
 注意:
 
 数组的长度为[2, 10,000]，并且确定为偶数。
 数组中数字的大小在范围[-100,000, 100,000]内。
 */

#import "ThitySevenViewController.h"

@interface ThitySevenViewController ()

@end

@implementation ThitySevenViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSArray * candies = @[@"1",@"1",@"2",@"3",@"4",@"4",@"4",@"4"];
    NSLog(@"%@ 妹妹可得数量%ld",candies,[self loadMaxCandies:candies]);
}

- (NSInteger)loadMaxCandies:(NSArray *)array{
    NSInteger maxZhonglei = 0;//总共的种类数
    NSArray * newArray = [self class5:[NSMutableArray arrayWithArray:array]];
    NSString * temp = @"";
    NSInteger i =0;
    while (i<newArray.count) {
        if (![temp isEqualToString:newArray[i]]) {
             maxZhonglei++;
        }
        temp = newArray[i];
        i++;
    }
    
    if (maxZhonglei>=newArray.count/2) {
        return newArray.count/2;
    }else{
        return maxZhonglei;
    }
}


//先排序

- (NSArray *)class5:(NSMutableArray *)array{
    NSInteger j;
    NSString * c;
    for (NSInteger i=1; i< array.count; i++) {
        //如果第i个元素小于第j个，则第j个向后移动
        for (c=array[i],j=i-1; j>=0&&([c integerValue]<[array[j] integerValue]); j--){
            array[j+1]=array[j];
        }
        array[j+1]=c;
    }
    return array;
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
