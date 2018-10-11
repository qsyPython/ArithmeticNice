//
//  TwenrtyEightViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/10/10.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 给定一个Excel表格中的列名称，返回其相应的列序号。
 
 例如，
 
 A -> 1
 B -> 2
 C -> 3
 ...
 Z -> 26
 AA -> 27
 AB -> 28
 ...
 示例 1:
 
 输入: "A"
 输出: 1
 示例 2:
 
 输入: "AB"
 输出: 28
 示例 3:
 
 输入: "ZY"
 输出: 701
 */
// AAA
//   A*(i*26) +A*26 +A

#import "TwenrtyEightViewController.h"

@interface TwenrtyEightViewController ()

@end

@implementation TwenrtyEightViewController

- (void)viewDidLoad {
    [super viewDidLoad];
 
    NSLog(@"daan:%ld",[self sendSomeStr:@"ZY"]);
}


- (NSInteger)sendSomeStr:(NSString *)str{
    NSInteger sum = 0;
    for (NSInteger i =0; i<str.length; i++) {
        char temp=[str characterAtIndex:i]-64;
        sum=sum+temp*pow(26, str.length-i-1);
        
    }
    return sum;
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
