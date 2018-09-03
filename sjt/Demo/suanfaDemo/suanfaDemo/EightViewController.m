//
//  EightViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/3.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：
 
 行数 m 应当等于给定二叉树的高度。
 列数 n 应当总是奇数。
 根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。
 每个未使用的空间应包含一个空的字符串""。
 使用相同的规则输出子树。
 示例 1:
 
 输入:
 1
 /
 2
 输出:
 [["", "1", ""],
 ["2", "", ""]]
 示例 2:
 
 输入:
 1
 / \
 2   3
 \
 4
 输出:
 [["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
 示例 3:
 
 输入:
 1
 / \
 2   5
 /
 3
 /
 4
 输出:
 [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
 注意: 二叉树的高度在范围 [1, 10] 中。
 
 */

#import "EightViewController.h"
#import "ThreeModel.h"
@interface EightViewController ()
@property (nonatomic,strong)ThreeModel *model;
@end

@implementation EightViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    NSMutableArray * array=[self toHangshu:4];
    NSLog(@"%@",[array description]);
}


/**                                    midder
 行数         列数   相当于所有节点      中间位置         左子节点       右子节点
 m           n     2^m-1             n/2+1          midder/2      n-midder/2+1
 hang 2    shu 3   2^2-1              2             1   2^0       3
 hang 3    shu 7   2^3-1              4             2   2^1       6
 hang 4    shu 15  2^4-1              8             4   2^2       12
 hang 5    shu 31  2^5-1              16            8   2^3
 */

- (NSMutableArray *)toHangshu:(NSInteger)m{
    NSInteger n =pow(2, m)-1;
    NSMutableArray * array=[NSMutableArray arrayWithCapacity:0];
    NSInteger midder = n/2+1;
    NSInteger leftMidder = 0;
    NSInteger rightMidder = 0;
    for (NSInteger i = 1; i<=m; i++) {//行
        NSMutableArray * tempArray=[NSMutableArray arrayWithCapacity:0];
        if (i!=1) {
            leftMidder= leftMidder/2;
            rightMidder= n - leftMidder + 1;
        }
        for (NSInteger j = 1; j<=n; j++) {//列
            if (i==1) {
                if (j==midder) {
                    [tempArray addObject:@"X"];
                    leftMidder = midder;
                }else{
                    [tempArray addObject:@" "];
                }
            }else{
                if (j==leftMidder) {
                    [tempArray addObject:@"X"];
                }else if(j==rightMidder){
                    [tempArray addObject:@"X"];
                }else{
                    [tempArray addObject:@" "];
                }
            }
        }
        [array addObject:tempArray];
    }
    
    return array;
}
@end
