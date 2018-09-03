//
//  SevenViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/8/31.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 *
 编写一个 SQL 查询，查找 Person 表中所有重复的电子邮箱。
 
 示例：
 
 +----+---------+
 | Id | Email   |
 +----+---------+
 | 1  | a@b.com |
 | 2  | c@d.com |
 | 3  | a@b.com |
 +----+---------+
 根据以上输入，你的查询应返回以下结果：
 
 +---------+
 | Email   |
 +---------+
 | a@b.com |
 +---------+
 说明：所有电子邮箱都是小写字母。
 */

#import "SevenViewController.h"

@interface SevenViewController ()

@end

@implementation SevenViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSString * str= @"select Email from biao group by Email having count(*)>1";//找出表中Email字段重复值>1的字段值
    NSLog(@"%@",str);
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
