//
//  Twenrtythree1ViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/25.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 给定一个 salary表，如下所示，有m=男性 和 f=女性的值 。交换所有的 f 和 m 值(例如，将所有 f 值更改为 m，反之亦然)。要求使用一个更新查询，并且没有中间临时表。
 
 例如:
 
 | id | name | sex | salary |
 |----|------|-----|--------|
 | 1  | A    | m   | 2500   |
 | 2  | B    | f   | 1500   |
 | 3  | C    | m   | 5500   |
 | 4  | D    | f   | 500    |
 运行你所编写的查询语句之后，将会得到以下表:
 
 | id | name | sex | salary |
 |----|------|-----|--------|
 | 1  | A    | f   | 2500   |
 | 2  | B    | m   | 1500   |
 | 3  | C    | f   | 5500   |
 | 4  | D    | m   | 500    |
 */

#import "Twenrtythree1ViewController.h"

@interface Twenrtythree1ViewController ()

@end

@implementation Twenrtythree1ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
  
    NSLog(@"select id,name,sex (case when sex=='m' then 'f' else 'm' end), salary form biao ");
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
