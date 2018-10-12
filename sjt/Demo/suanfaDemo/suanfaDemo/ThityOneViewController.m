//
//  ThityOneViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/10/12.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 给定一个矩阵 A， 返回 A 的转置矩阵。
 
 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
 
 
 
 示例 1：
 
 输入：
 [[1,2,3],
 [4,5,6],
 [7,8,9]]
 输出：
 [[1,4,7],
 [2,5,8],
 [3,6,9]]
 示例 2：
 
 输入：
 [[1,2,3],
 [4,5,6]]
 输出：
 [[1,4],
 [2,5],
 [3,6]]
 
 
 提示：
 
 1 <= A.length <= 1000
 1 <= A[0].length <= 1000
 */

#import "ThityOneViewController.h"

@interface ThityOneViewController ()

@end

@implementation ThityOneViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSArray * array =@[@[@"1",@"2",@"3"],@[@"4",@"5",@"6"]];
    [self changeView:array];
}

- (void)changeView:(NSArray *)array{

    
    NSInteger x = array.count;
    NSInteger y = [array[0] count];
    NSMutableArray * tempsarray =[NSMutableArray arrayWithCapacity:0];
    for (NSInteger i = 0; i<y; i++) { //分配内存空间
        NSMutableArray * temparray=[NSMutableArray arrayWithCapacity:0];
        for(NSInteger j = 0; j<x; j++) {
            [temparray addObject:@""];
        }
        [tempsarray addObject:temparray];
    }
    //赋值
    for (NSInteger i = 0; i<x; i++) {
        for (NSInteger j = 0; j<y; j++) {
            NSString * some = array[i][j];
            tempsarray[j][i] = some;
        }
    }
    
    NSLog(@"old:%@\n  new:%@",[array description],[tempsarray description]);
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
