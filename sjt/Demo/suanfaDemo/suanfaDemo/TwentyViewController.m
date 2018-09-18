//
//  TwentyViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/18.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。
 
 你可以返回满足此条件的任何数组作为答案。
 
 示例：
 
 输入：[3,1,2,4]
 输出：[2,4,3,1]
 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
 
 提示：
 1 <= A.length <= 5000
 0 <= A[i] <= 5000
 */

#import "TwentyViewController.h"

@interface TwentyViewController ()

@end

@implementation TwentyViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    NSLog(@"%@",[[self sendArray:[NSMutableArray arrayWithObjects:@"1",@"3",@"5",@"6",@"10",@"2",@"5",@"11", nil]] description]);
}

- (NSMutableArray *)sendArray:(NSMutableArray *)array{
    NSInteger num =0;
    NSInteger i = 0;
    while (num<array.count) {
        NSString * str=array[i];
        NSInteger index = [str integerValue];
        if (index%2==0) {
            [array removeObject:str];
            [array insertObject:str atIndex:0];
            i++;
        }else{
            [array removeObject:str];
            [array addObject:str];
        }
        num++;
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
