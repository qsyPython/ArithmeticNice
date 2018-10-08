//
//  TwenrtySixViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/10/8.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
 
 给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
 
 重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
 
 如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
 
 示例 1:
 
 输入:
 nums =
 [[1,2],
 [3,4]]
 r = 1, c = 4
 输出:
 [[1,2,3,4]]
 解释:
 行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
 示例 2:
 
 输入:
 nums =
 [[1,2],
 [3,4]]
 r = 2, c = 4
 输出:
 [[1,2],
 [3,4]]
 解释:
 没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
 注意：
 
 给定矩阵的宽和高范围在 [1, 100]。
 给定的 r 和 c 都是正数。
 
 分别实现多项式求值的四种运算，若针对不同规模的输入值a
 ，各算法的运行时间，问题规模n
 分别取10，50，100，150，200，300，400，500，10000，20000，50000，100000时绘制四种算法运行时间的比较图。
 */

#import "TwenrtySixViewController.h"

@interface TwenrtySixViewController ()

@end

@implementation TwenrtySixViewController

- (void)viewDidLoad {
    [super viewDidLoad];

    NSMutableArray * arr=[self sendArray:@[@[@1,@2,@3],@[@4,@5,@6],@[@7,@8,@9],@[@11,@12,@13],@[@14,@15,@16]] withR:3 withC:5];
    NSLog(@"%@",arr.description);
}

//[[1,2,3],
// [2,4,3],
// [5,6,7]]

- (NSMutableArray *)sendArray:(NSArray *)array withR:(NSInteger)r withC:(NSInteger)c{
    
    NSMutableArray * tempArray=[NSMutableArray arrayWithCapacity:0];
    NSInteger i =0;
    while (i<array.count) {
        NSArray * currentArray=array[i];
        [tempArray addObjectsFromArray:currentArray];
        i++;
    }
    
    NSMutableArray * newArray= [NSMutableArray arrayWithCapacity:0];
    if (tempArray.count==r*c) {
          NSInteger index= 0;
        while (index<r*c) {
            [newArray addObject:[tempArray subarrayWithRange:NSMakeRange(index, c)]];
            index=index+c;
        };
        return newArray;
    }
    return [NSMutableArray arrayWithArray:array];
}

- (void)sendMathArray:(NSArray *)array {
    for (NSString * ele in array) {
         
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
