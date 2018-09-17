//
//  EighteenViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/14.
//  Copyright © 2018年 sjt. All rights reserved.
//
/**
 我们把符合下列属性的数组 A 称作山脉：
 
 A.length >= 3
 存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
 给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。
 
 
 
 示例 1：
 
 输入：[0,1,0]
 输出：1
 示例 2：
 
 输入：[0,2,1,0]
 输出：1
 
 
 提示：
 
 3 <= A.length <= 10000
 0 <= A[i] <= 10^6
 A 是如上定义的山脉
 */

#import "EighteenViewController.h"

@interface EighteenViewController ()

@end

@implementation EighteenViewController

- (void)viewDidLoad {
    [super viewDidLoad];

    
    NSArray * array=@[@"0",@"1",@"3",@"4",@"5",@"7",@"4",@"3",@"2",@"1"];
    NSLog(@"这个%@数组的山峰为%ld",[array description],[self loadIndexWithMax:array]);
}

- (NSInteger)loadIndexWithMax:(NSArray *)array{
    NSInteger idx = 0;
    //找出最大的
    for (NSInteger i=1; i<array.count-1; i++) {
        if ([array[i-1] integerValue]<[array[i] integerValue]&&[array[i+1] integerValue]<[array[i] integerValue]) {
            idx=i;
        }
    }
    return idx;
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
