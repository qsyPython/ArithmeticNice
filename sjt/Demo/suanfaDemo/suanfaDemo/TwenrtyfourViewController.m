//
//  TwenrtyfourViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/26.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 自除数 是指可以被它包含的每一位数除尽的数。
 
 例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
 
 还有，自除数不允许包含 0 。
 
 给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。
 
 示例 1：
 
 输入：
 上边界left = 1, 下边界right = 22
 输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
 注意：
 
 每个输入参数的边界满足 1 <= left <= right <= 10000。
 
 
 
 作业2
 
 你和你的朋友，两个人一起玩 Nim游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。
 
 你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。
 
 示例:
 
 输入: 4
 输出: false
 解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
 因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。
 1 2 3 5 6 7
 4 8
 
  1 1 1 1 1 1
 */

#import "TwenrtyfourViewController.h"

@interface TwenrtyfourViewController ()

@end

@implementation TwenrtyfourViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSLog(@"作业1：%@",[[self sednMinNum:1 withMaxNum:22] description]);
    NSLog(@"作业2(yes为1 no为0)：%d",[self isCanOurNazou:6]);
}

- (NSMutableArray *)sednMinNum:(NSInteger)min withMaxNum:(NSInteger)max{
    NSMutableArray * array=[NSMutableArray arrayWithCapacity:0];
    for (NSInteger i = min; i<max; i++) {
        NSString * str =[NSString stringWithFormat:@"%ld",min];
        if ([self isZiChuShu:str]) {
            [array addObject:str];
        }
    }
    
    return array;
}

- (BOOL)isZiChuShu:(NSString *)str{
    BOOL ISZICHUSHU =YES;
    NSInteger strNum=[str integerValue];
    if (strNum==0) {
        ISZICHUSHU =NO;
    }else{
        for (NSInteger i = 0; i<str.length; i++) {
            NSString * sxx =[str substringWithRange:NSMakeRange(i, 1)];
            NSInteger num = [sxx integerValue];
            if (strNum%num!=0) {
                ISZICHUSHU=NO;
                break;
            }
        }
    }
    return ISZICHUSHU;
}



- (BOOL)isCanOurNazou:(NSInteger)count{
    BOOL isCan=NO;
    if (count%4!=0) {
        isCan=YES;
    }
    return isCan;
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
