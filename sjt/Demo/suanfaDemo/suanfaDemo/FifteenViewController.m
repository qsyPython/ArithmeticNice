//
//  FifteenViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/11.
//  Copyright © 2018年 sjt. All rights reserved.
//
/**
 翻转图像：矩阵翻转
 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
 
 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
 
 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
 
 示例 1:
 
 输入: [[1,1,0],[1,0,1],[0,0,0]]
 输出: [[1,0,0],[0,1,0],[1,1,1]]
 解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
 然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
 示例 2:
 
 输入: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
 输出: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 解释: 首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
 然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 说明:
 
 1 <= A.length = A[0].length <= 20
 0 <= A[i][j] <= 1
 
 */
#import "FifteenViewController.h"

@interface FifteenViewController ()

@end

@implementation FifteenViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSMutableArray *arr = @[@[@"1",@"1",@"0"],@[@"1",@"0",@"1"],@[@"0",@"0",@"0"]].mutableCopy;
    NSArray *resArr = [self rotate_pic:arr];
    NSLog(@"%@",resArr);
    // Do any additional setup after loading the view.
}

- (NSArray *)rotate_pic:(NSArray *)originArr {
    NSMutableArray *desArr = @[].mutableCopy;
    for (NSArray *arr in originArr) {
        NSMutableArray *tempArr = arr.mutableCopy;
        NSArray *resultLevelArr = [self levelRotate:tempArr start:0 end:tempArr.count - 1];
        NSArray *resultReveseArr = [self reveseRotate:resultLevelArr.mutableCopy];
        [desArr addObject:resultReveseArr];
    }
    return desArr;
}

- (NSArray *)levelRotate:(NSMutableArray *)array start:(long )start end:(long )end {
    while (start < end) {
        NSString *tempStr = [array objectAtIndex:start];
        [array replaceObjectAtIndex:start withObject:[array objectAtIndex:end]];
        [array replaceObjectAtIndex:end withObject:tempStr];
        start++;
        end--;
    }
    return array;
}

- (NSArray *)reveseRotate:(NSMutableArray *)array {
    for (int i =0; i<array.count; i++) {
        if ([[array objectAtIndex:i] isEqualToString:@"1"]) {
            [array replaceObjectAtIndex:i withObject:@"0"];
        } else {
            [array replaceObjectAtIndex:i withObject:@"1"];
        }
    }
    return array;
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
