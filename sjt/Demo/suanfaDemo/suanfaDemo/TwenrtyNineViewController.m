//
//  TwenrtyNineViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/10/11.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
 
 示例:
 
 输入: 38
 输出: 2
 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
 */

#import "TwenrtyNineViewController.h"

@interface TwenrtyNineViewController ()

@end

@implementation TwenrtyNineViewController

- (void)viewDidLoad {
    [super viewDidLoad];  //ddd
    NSLog(@"%@ ==== %ld",@"12345",[self sendStr:@"12345"]);
}

- (NSInteger)sendStr:(NSString *)str{
    NSInteger num = 0;
    for (NSInteger i = 0; i<str.length; i++) {
        NSString * tempStr=[str substringWithRange:NSMakeRange(i, 1)];
        num = num + [tempStr integerValue];
    }
    if (num>9) {
        return [self sendStr:[NSString stringWithFormat:@"%ld",num]];
    }else{
        
        
        
        return num;
    }
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
