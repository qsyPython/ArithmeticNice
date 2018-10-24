
//
//  ThityS ThityEightViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/10/24.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 今天看下数据结构题：
 Employee 表包含所有员工，他们的经理也属于员工。每个员工都有一个 Id，此外还有一列对应员工的经理的 Id。
 
 +----+-------+--------+-----------+
 | Id | Name  | Salary | ManagerId |
 +----+-------+--------+-----------+
 | 1  | Joe   | 70000  | 3         |
 | 2  | Henry | 80000  | 4         |
 | 3  | Sam   | 60000  | NULL      |
 | 4  | Max   | 90000  | NULL      |
 +----+-------+--------+-----------+
 给定 Employee 表，编写一个 SQL 查询，该查询可以获取收入超过他们经理的员工的姓名。在上面的表格中，Joe 是唯一一个收入超过他的经理的员工。
 
 +----------+
 | Employee |
 +----------+
 | Joe      |
 +----------+
 */

#import "ThityS ThityEightViewController.h"

@interface ThityS_ThityEightViewController ()

@end

@implementation ThityS_ThityEightViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSLog(@"select e1.name as Employee from Employee as e1, Employee as e2 where e1.managerId == e2.Id and e1.Salary>e2.Salary");
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
