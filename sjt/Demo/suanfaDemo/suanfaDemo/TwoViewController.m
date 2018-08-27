//
//  TwoViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/8/24.
//  Copyright © 2018年 sjt. All rights reserved.
/***
 # 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
 #
 # 示例 1:
 #
 # 输入: [1,2,3,4,5,6,7] 和 k = 3
 # 输出: [5,6,7,1,2,3,4]
 # 解释:
 # 向右旋转 1 步: [7,1,2,3,4,5,6]
 # 向右旋转 2 步: [6,7,1,2,3,4,5]
 # 向右旋转 3 步: [5,6,7,1,2,3,4]
 # 说明:
 # 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
 # 要求使用空间复杂度为 O(1) 的原地算法。
 # 空间复杂度O(1)：为常量。即不随被处理数据量n的大小而改变！
 # 原地算法:一种使用小的，空固定数量的额外之间来转换资料的算法。
 ***/

#import "TwoViewController.h"

@interface TwoViewController ()

@end

@implementation TwoViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSArray * array=@[@"6",@"2",@"8",@"56",@"33",@"3",@"5",@"6",@"2",@"8",@"56",@"33",@"3",@"5"];
    NSInteger k = 3;
    NSMutableArray * sumArray=[self sendNumsArray:array withTarget:k];
    NSLog(@"%@",[sumArray description]);
}



- (NSMutableArray *)sendNumsArray:(NSArray *)numArray withTarget:(NSInteger)index{
    NSMutableArray * tempArray=[NSMutableArray arrayWithCapacity:0];
    [tempArray addObjectsFromArray:numArray];
    NSInteger zuizhongIndex;//得到最终的前进位数
    if (numArray.count<index) {
        zuizhongIndex=index%numArray.count;//取余数
    }else if (numArray.count==index){
        zuizhongIndex=0;
        return tempArray;//直接返回原数组
    }else{
        zuizhongIndex=index;
    }
    NSArray * array=[numArray subarrayWithRange:NSMakeRange(0, zuizhongIndex)];
    [tempArray removeObjectsInArray:array];
    [tempArray addObjectsFromArray:array];
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
