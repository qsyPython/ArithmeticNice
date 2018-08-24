//
//  ViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/8/23.
//  Copyright © 2018年 sjt. All rights reserved.
//

#import "ViewController.h"
#import "TwoViewController.h"
@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSArray * array=@[@"1",@"2",@"3",@"4",@"5",@"6",@"7",@"8",@"9",@"10"];
    NSInteger k = 10;
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


@end
