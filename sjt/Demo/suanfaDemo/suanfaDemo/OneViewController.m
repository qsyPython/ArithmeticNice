//
//  OneViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/8/24.
//  Copyright © 2018年 sjt. All rights reserved.
//

#import "OneViewController.h"

@interface OneViewController ()

@end

@implementation OneViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSArray * array=@[@"6",@"2",@"8",@"56",@"33",@"3",@"5"];
    NSInteger index = 8;
    NSMutableArray * sumArray=[self sendNumsArray:array withTarget:index];
    NSLog(@"%@",[sumArray description]);
}


- (NSMutableArray *)sendNumsArray:(NSArray *)numArray withTarget:(NSInteger)index{
    NSMutableArray * tempArray=[NSMutableArray arrayWithCapacity:0];
    for (int i=0; i<numArray.count;i++) {
        NSInteger num1=[numArray[i] integerValue];
        if (num1>index) {
            continue;
        }
        NSString * numi=[NSString stringWithFormat:@"%d",i];
        BOOL isbool = [tempArray containsObject: numi];
        if (isbool) {
            continue;
        }
        for (int j=i+1; j<numArray.count; j++) {
            NSInteger num2=[numArray[j] integerValue];
            if (num2>index) {
                continue;
            }
            NSString * numj=[NSString stringWithFormat:@"%d",j];
            BOOL isbool = [tempArray containsObject: numj];
            if (isbool) {
                continue;
            }
            NSInteger sum = num1+num2;
            if (sum==index) {
                [tempArray addObject:[NSString stringWithFormat:@"%d",i]];
                [tempArray addObject:[NSString stringWithFormat:@"%d",j]];
                //得到一组数据 退出本次循环 继续下一循环
                break;
            }
        }
    }
    return tempArray;
}

- (NSMutableArray *)sendNumsArray2:(NSArray *)numArray withTarget:(NSInteger)index{
    NSMutableArray * tempArray=[NSMutableArray arrayWithCapacity:0];
    NSMutableArray * copyNumArray=[NSMutableArray arrayWithArray:numArray];
    
    for (NSString * str in numArray) {//先刨去所有比数字大的数
        if ([str integerValue]>index) {
            [copyNumArray removeObject:str];
        }
    }
    
    for (int i=0; i<numArray.count;i++) {
        NSInteger num1=[numArray[i] integerValue];
        for (int j=i+1; j<numArray.count; j++) {
            NSInteger num2=[numArray[j] integerValue];
            NSInteger sum = num1+num2;
            if (sum==index) {
                [tempArray addObject:numArray[i]];
                [tempArray addObject:numArray[j]];
                return tempArray;
            }
        }
    }
    return nil;
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
