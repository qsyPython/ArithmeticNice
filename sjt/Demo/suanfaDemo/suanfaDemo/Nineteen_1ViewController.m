//
//  Nineteen_1ViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/17.
//  Copyright © 2018年 sjt. All rights reserved.
//
/**
 杨辉三角
 
 杨辉三角，是二项式系数在三角形中的一种几何排列。
 前提：每行端点与结尾的数为1.
 每个数等于它上方两数之和。
 每行数字左右对称，由1开始逐渐变大。
 第n行的数字有n项。
 第n行数字和为2n-1。
 第n行的m个数可表示为 C(n-1，m-1)，即为从n-1个不同元素中取m-1个元素的组合数。
 第n行的第m个数和第n-m+1个数相等 ，为组合数性质之一。
 每个数字等于上一行的左右两个数字之和。可用此性质写出整个杨辉三角。即第n+1行的第i个数等于第n行的第i-1个数和第i个数之和，这也是组合数的性质之一。即 C(n+1,i)=C(n,i)+C(n,i-1)。
 (a+b)n的展开式中的各项系数依次对应杨辉三角的第(n+1)行中的每一项。
 将第2n+1行第1个数，跟第2n+2行第3个数、第2n+3行第5个数……连成一线，这些数的和是第4n+1个斐波那契数；将第2n行第2个数(n>1)，跟第2n-1行第4个数、第2n-2行第6个数……这些数之和是第4n-2个斐波那契数。
 将各行数字相排列，可得11的n-1（n为行数）次方：1=11^0; 11=11^1; 121=11^2……当n>5时会不符合这一条性质，此时应把第n行的最右面的数字"1"放在个位，然后把左面的一个数字的个位对齐到十位... ...，以此类推，把空位用“0”补齐，然后把所有的数加起来，得到的数正好是11的n-1次方。以n=11为例，第十一行的数为：1,10,45,120,210,252,210,120,45,10,1，结果为 25937424601=1110。
 8  17
 9  19   2n+1
 
 */

/**
       0  1  2  3  4  5  6  7  8  9  10 11 12 13
 
       *  *  *  *  *  *  1  *  *  *  *  *  *    1
       *  *  *  *  *  1  *  1  *  *  *  *  *    2
       *  *  *  *  1  *  2  *  1  *  *  *  *    3
       *  *  *  1  *  3  *  3  *  1  *  *  *    4
       *  *  1  *  4  *  6  *  4  *  1  *  *    5
       *  1  *  5  * 10  * 10  *  5  *  1  *    6
       1  *  6  * 15  * 20  * 15  *  6  *  1    7
 */
#import "Nineteen_1ViewController.h"

@interface Nineteen_1ViewController ()

@end

@implementation Nineteen_1ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    NSMutableArray * array =[self sendNumber:9];
    NSLog(@"%@",[array description]);
}

- (NSMutableArray *)sendNumber:(NSInteger)num{
    NSMutableArray * tempArray=[NSMutableArray arrayWithCapacity:0];
    for (NSInteger i = 0; i<num+1; i++) {//行
        NSMutableArray * hangArray=[NSMutableArray arrayWithCapacity:0];
        for (NSInteger j = 0; j<(2*num+1); j++) {//列
            if (j == (num - i)||(j == (num + i))) {//先加上1的
                [hangArray addObject:@"1"];
            }else{
                if (tempArray.count>0&&tempArray.count>i-1) {//根据上一行计算下一行
                    NSArray * topArray=tempArray[i-1];
                    NSInteger left = 0;
                    NSInteger right = 0;
                    if (j-1>=0) {//防止越界
                        left =  [[topArray objectAtIndex:j-1] integerValue];
                    }
                    
                    if (j+1<topArray.count) {//防止越界
                        right = [[topArray objectAtIndex:j+1] integerValue];
                    }
                   
                    NSInteger  sum = left+right;
                    if (sum>0) {
                         [hangArray addObject:[NSString stringWithFormat:@"%ld",sum]];
                    }else{
                       [hangArray addObject:@" "];
                    }
                }else{
                    [hangArray addObject:@" "];
                }
            }
        }
        [tempArray addObject:hangArray];
    }
    return tempArray;
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
