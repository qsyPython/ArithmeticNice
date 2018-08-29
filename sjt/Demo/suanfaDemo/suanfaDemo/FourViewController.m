//
//  FourViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/8/28.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 今天的作业
 宝石与石头：
 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
 
 J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。
 
 示例 1:
 
 输入: J = "aA", S = "aAAbbbb"
 输出: 3
 示例 2:
 
 输入: J = "z", S = "ZZ"
 输出: 0
 注意:
 
 S 和 J 最多含有50个字母。
 J 中的字符不重复。
 
 
 作业2
 这里有张 World 表
 
 +-----------------+------------+------------+--------------+---------------+
 | name            | continent  | area       | population   | gdp           |
 +-----------------+------------+------------+--------------+---------------+
 | Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
 | Albania         | Europe     | 28748      | 2831741      | 12960000      |
 | Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
 | Andorra         | Europe     | 468        | 78115        | 3712000       |
 | Angola          | Africa     | 1246700    | 20609294     | 100990000     |
 +-----------------+------------+------------+--------------+---------------+
 如果一个国家的面积超过300万平方公里，或者人口超过2500万，那么这个国家就是大国家。
 
 编写一个SQL查询，输出表中所有大国家的名称、人口和面积。
 
 例如，根据上表，我们应该输出:
 
 +--------------+-------------+--------------+
 | name         | population  | area         |
 +--------------+-------------+--------------+
 | Afghanistan  | 25500100    | 652230       |
 | Algeria      | 37100000    | 2381741      |
 +--------------+-------------+--------------+
 */
//

#import "FourViewController.h"

@interface FourViewController ()

@end

@implementation FourViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSString * str=@"AaHHSJSJjdksdhsldlks";
    NSString * strJJ=@"As";
    NSString * response=[self loadCountAllStr:str withAllStr:strJJ];
    NSLog(@"%@",response);
    [self wordMysql];
}

- (NSString *)loadCountAllStr:(NSString *)allStr withAllStr:(NSString *)str {
    NSInteger index=0;
    for (int i=0; i<allStr.length; i++) {
        NSString * charStr= [allStr substringWithRange:NSMakeRange(i, 1)];
        if ([str containsString:charStr]) {
            index++;
        }
    }
    return [NSString stringWithFormat:@"str == %ld个",index];
}

- (void)wordMysql{
   NSString *some=@"SELECT name,population,area  FROM resultT WHERE area >300000 or population >25000000";
    NSLog(@"%@",some);
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
