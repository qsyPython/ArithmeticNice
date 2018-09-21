//
//  TwenrtytwoViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/21.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 编写一个函数，其作用是将输入的字符串反转过来。
 
 示例 1:
 
 输入: "hello"
 输出: "olleh"
 示例 2:
 
 输入: "A man, a plan, a canal: Panama"
 输出: "amanaP :lanac a ,nalp a ,nam A"
 
 
 某城市开了一家新的电影院，吸引了很多人过来看电影。该电影院特别注意用户体验，专门有个 LED显示板做电影推荐，上面公布着影评和相关电影描述。
 
 作为该电影院的信息部主管，您需要编写一个 SQL查询，找出所有影片描述为非 boring (不无聊) 的并且 id 为奇数 的影片，结果请按等级 rating 排列。
 
 
 
 例如，下表 cinema:
 
 +---------+-----------+--------------+-----------+
 |   id    | movie     |  description |  rating   |
 +---------+-----------+--------------+-----------+
 |   1     | War       |   great 3D   |   8.9     |
 |   2     | Science   |   fiction    |   8.5     |
 |   3     | irish     |   boring     |   6.2     |
 |   4     | Ice song  |   Fantacy    |   8.6     |
 |   5     | House card|   Interesting|   9.1     |
 +---------+-----------+--------------+-----------+
 对于上面的例子，则正确的输出是为：
 
 +---------+-----------+--------------+-----------+
 |   id    | movie     |  description |  rating   |
 +---------+-----------+--------------+-----------+
 |   5     | House card|   Interesting|   9.1     |
 |   1     | War       |   great 3D   |   8.9     |
 +---------+-----------+--------------+-----------+
 */

#import "TwenrtytwoViewController.h"

@interface TwenrtytwoViewController ()

@end

@implementation TwenrtytwoViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self sendString:[NSMutableString stringWithFormat:@"abcdefghijk%@",@"1"]];
}

- (void)sendString:(NSMutableString *)str{
    NSLog(@"%@\n",str);
    for (NSInteger i=0; i<str.length/2; i++) {
        NSString * left = [str substringWithRange:NSMakeRange(i, 1)];
        NSString * right =[str substringWithRange:NSMakeRange(str.length-1-i, 1)];
        [str replaceCharactersInRange:NSMakeRange(i, 1) withString:right];
        [str replaceCharactersInRange:NSMakeRange(str.length-1-i, 1) withString:left];
    }
    NSLog(@"%@",str);
    
    NSString * str1=[NSString stringWithFormat:@"SELECT * FROM cinema WHERE description!=%@ or id%2==1 ORDER BY rating DESC",@"boring"];
    NSLog(@"数据库:%@",str1);
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
