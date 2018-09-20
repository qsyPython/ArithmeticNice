//
//  Twentyone1ViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/20.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
 
 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
 
 示例 1:
 
 给定数组 nums = [1,1,2],
 
 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
 
 你不需要考虑数组中超出新长度后面的元素。
 示例 2:
 
 给定 nums = [0,0,1,1,1,2,2,3,3,4],
 
 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
 
 你不需要考虑数组中超出新长度后面的元素。
 */

#import "Twentyone1ViewController.h"

@interface Twentyone1ViewController ()

@end

@implementation Twentyone1ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSMutableArray * array=[NSMutableArray arrayWithObjects:@"1",@"1",@"2",@"2",@"3",@"3",@"4",@"5",@"6", nil];
    NSLog(@"原来数组:%@\n",[array description]);
    [self changeArray:array];
    NSLog(@"修改后:%@-----%ld",[array description],array.count);
}

- (void)changeArray:(NSMutableArray *)array{
    
    NSInteger num =0;
    NSString * current=@"";
    NSString * next=@"";
    while (num<array.count) {
        current =array[num];
        if (num+1<array.count) {
            next =array[num+1];
            if ([current isEqualToString:next]) {
                [array removeObjectAtIndex:num];
            }else{
                num++;
            }
        }else{
            num++;
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
