//
//  ThreeViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/8/27.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 转换成小写字母 ：
 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
 
 示例 1：
 
 输入: "Hello"
 输出: "hello"
 示例 2：
 
 输入: "here"
 输出: "here"
 
 示例 3：
 
 输入: "LOVELY"
 输出: "lovely"
 
 */

#import "ThreeViewController.h"

@interface ThreeViewController ()

@end

@implementation ThreeViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSLog(@"大->小%@",[self toLowerCase:@"Hello My Some Peple  hah"]);
    NSLog(@"小->大%@",[self toUpperCase:@"Hello My Some Peple  HH "]);
}


//将小写转为大写  type
- (NSString *)toLowerCase:(NSString *)str{
    for (NSInteger i=0; i<str.length; i++) {
        if ([str characterAtIndex:i]>='a'&[str characterAtIndex:i]<='z') {
            //A  65  a  97
            char  temp=[str characterAtIndex:i]-32;
            NSRange range=NSMakeRange(i, 1);
            str=[str stringByReplacingCharactersInRange:range withString:[NSString stringWithFormat:@"%c",temp]];
        }
    }
    return str;
}

//将大写转为小写
- (NSString *)toUpperCase:(NSString *)str{
    for (NSInteger i=0; i<str.length; i++) {
        if ([str characterAtIndex:i]>='A'&[str characterAtIndex:i]<='Z') {
            //A  65  a  97
            char  temp=[str characterAtIndex:i]+32;
            NSRange range=NSMakeRange(i, 1);
            str=[str stringByReplacingCharactersInRange:range withString:[NSString stringWithFormat:@"%c",temp]];
        }
    }
    return str;
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
