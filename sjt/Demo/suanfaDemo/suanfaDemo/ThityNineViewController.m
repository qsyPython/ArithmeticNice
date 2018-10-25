//
//  ThityNineViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/10/25.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 今天算法题：给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
 
 说明：解集不能包含重复的子集。
 
 示例:
 
 输入: nums = [1,2,3]
 输出:
 [
 [3],
 [1],
 [2],
 [1,2,3],
 [1,3],
 [2,3],
 [1,2],
 []
 ]
 */

/**
 1 2 3 4 5
 
 1
 2
 3
 4
 5
 
 1 2
 1 3
 1 4
 1 5
 1 2 3
 
 1 2 4
 1 2 5
 1 3 4
 1 3 5
 1 4 5
 
 1 2 3 4
 1 2 3 5
 1 2 4 5
 1 3 4 5
 1 2 3 4 5

 2 3
 2 4
 2 5
 3 4
 3 5
 
 4 5
 2 3 4
 2 3 5
 2 4 5
 3 4 5
 
 2 3 4 5
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 */

#import "ThityNineViewController.h"

@interface ThityNineViewController ()
@property (nonatomic ,strong)NSMutableArray * numsArray;
@property (nonatomic ,strong)NSArray * allArray;
@end

@implementation ThityNineViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    _allArray=@[@"1",@"2",@"3",@"4",@"5",@"6",@"7"];
    _numsArray =[NSMutableArray arrayWithCapacity:0];
    NSLog(@"%@",[self sendArray:_allArray]);
}

- (NSMutableArray *)sendArray:(NSArray *)array{

    for (NSInteger i =0; i<array.count; i++) {
        NSMutableArray * array11 =[NSMutableArray arrayWithCapacity:0];
        [array11 addObject:array[i]];
        [self.numsArray addObject:[NSMutableArray arrayWithArray:array11]];
        [self sendArray:array11 withI:i+1];
    }

    
    return self.numsArray;
}

- (void)sendArray:(NSMutableArray *)array withI:(NSInteger)i{
    if (i > self.allArray.count-1) {
        return;
    }
    
    for (NSInteger s =i; s<self.allArray.count; s++) {
        NSMutableArray * linshiArray =[NSMutableArray arrayWithArray:array];
        if (![linshiArray containsObject:self.allArray[s]]) {
           [linshiArray addObject:self.allArray[s]];
           [self.numsArray addObject:linshiArray];
            if (s<self.allArray.count-1) {
                [self sendArray:linshiArray withI:s+1];
            }
        }
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
