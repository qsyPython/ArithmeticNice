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
    NSInteger k = 2;
    NSMutableArray * sumArray=[self sendNumsArray:array withTarget:k];
    NSLog(@"%@",[sumArray description]);
    
    NSMutableArray * sumArray2=[self sendNumsArray2:array withTarget:k];
    NSLog(@"%@",[sumArray2 description]);
}



////a b c d e f g h
//  0 1 2 3 4 5 6 7
//
//
//  g h a b c d e f
//  6 7 0 1 2 3 4 5




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

- (NSMutableArray *)sendNumsArray2:(NSArray *)numArray withTarget:(NSInteger)index{
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
    
    [self sendArray:tempArray startIndex:0 withEnd:zuizhongIndex-1];//0-k对折
    [self sendArray:tempArray startIndex:zuizhongIndex withEnd:numArray.count-1];//k-count 对折
    [self sendArray:tempArray startIndex:0 withEnd:numArray.count-1];//整体对折
    return tempArray;
}

//翻转数据
- (void)sendArray:(NSMutableArray *)array startIndex:(NSInteger)start withEnd:(NSInteger)end{
    NSString * temp=nil;
    while (start<end) {
        temp=array[start];
        array[start]=array[end];
        array[end]=temp;
        start++;
        end--;
    }
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
