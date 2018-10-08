//
//  TwenrtyfiveViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/27.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
 
 示例 1:
 
 输入: "Let's take LeetCode contest"
 输出: "s'teL ekat edoCteeL tsetnoc"
 注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
 
 表1: Person
 
 +-------------+---------+
 | 列名         | 类型     |
 +-------------+---------+
 | PersonId    | int     |
 | FirstName   | varchar |
 | LastName    | varchar |
 +-------------+---------+
 PersonId 是上表主键
 表2: Address
 
 +-------------+---------+
 | 列名         | 类型    |
 +-------------+---------+
 | AddressId   | int     |
 | PersonId    | int     |
 | City        | varchar |
 | State       | varchar |
 +-------------+---------+
 AddressId 是上表主键
 
 
 编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，都需要基于上述两表提供 person 的以下信息：
 FirstName, LastName, City, State
 */

#import "TwenrtyfiveViewController.h"

@interface TwenrtyfiveViewController ()

@end

@implementation TwenrtyfiveViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSLog(@"XXXX:%@",[self sendSomeStr:@"csds sas dssss"]);
    
    NSLog(@"select person.FirstName, person.LastName, address.City, address.State from Person,Address where person.personId == address.personId");
}

- (NSString *)sendSomeStr:(NSString *)str{
    
    NSArray * array=[str componentsSeparatedByString:@" "];
    NSMutableString * someJieguo =[[NSMutableString alloc]init];
    for (NSInteger i=0; i<array.count; i++) {
        NSString * ustr=[self dancinixu:array[i]];
        [someJieguo appendString:ustr];
        if (i!=array.count-1) {
            [someJieguo appendString:@" "];
        }
    }
    return someJieguo;
}

- (NSString *)dancinixu:(NSString *)danci{
    for (NSInteger i=0; i<=danci.length/2; i++) {
        NSString * strleft = [danci substringWithRange:NSMakeRange(i, 1)];
        NSString * strright =[danci substringWithRange:NSMakeRange(danci.length-i-1, 1)];
        [danci stringByReplacingCharactersInRange:NSMakeRange(i, 1) withString:strright];
        [danci stringByReplacingCharactersInRange:NSMakeRange(danci.length-i-1, 1) withString:strleft];
    }
    return danci;
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
