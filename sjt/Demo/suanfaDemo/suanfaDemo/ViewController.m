//
//  ViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/8/23.
//  Copyright © 2018年 sjt. All rights reserved.
//



#import "ViewController.h"
#import "TwoViewController.h"
#import "ThreeModel.h"
@interface ViewController ()
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    NSMutableArray * array=[self sendToJiedian:5];
    
    NSLog(@"%@",[array description]);
}


/**                                    midder
 行数         列数   相当于所有节点      中间位置         左子节点       右子节点
  m           n    2^m-1             n/2+1          midder/2      n-midder/2+1
 hang 2    shu 3   2^2-1              2             1   2^0       3
 hang 3    shu 7   2^3-1              4             2   2^1       6
 hang 4    shu 15  2^4-1              8             4   2^2       12
 hang 5    shu 31  2^5-1              16            8   2^3
 
 
 1 hang 1   2^(n-1)
 2      2
 3      4
 4      8
 5      16
 
 */

- (NSMutableArray *)sendToJiedian:(NSInteger)m{
    NSInteger n =pow(2, m)-1;
    NSInteger midder = n/2+1;
    NSMutableArray * allArray=[NSMutableArray arrayWithCapacity:0];
    ThreeModel * model =[[ThreeModel alloc]init];
    model.currentJiedian=midder;
    model.father=0;
    NSMutableArray * jiedianNumberArray=[NSMutableArray arrayWithCapacity:0];
    NSMutableArray * currentArray=[NSMutableArray arrayWithObjects:model, nil];
    NSMutableArray * nextJiedianArray=[NSMutableArray arrayWithCapacity:0];
  
    for (NSInteger i =1; i<=m; i++) {
        NSMutableArray * hangArray=[NSMutableArray arrayWithCapacity:0];
        jiedianNumberArray=[self loadJiedianmodelToArray:currentArray];//江modelarray 变成numArray
        for (NSInteger j = 1; j<=n; j++) {//列
            NSString * jStr=[NSString stringWithFormat:@"%ld",j];
            if ([jiedianNumberArray containsObject:jStr]) {
                [hangArray addObject:@"X"];
            }else{
                [hangArray addObject:@" "];
            }
        }
         [allArray addObject:hangArray];
         [nextJiedianArray removeAllObjects];
        
        for (ThreeModel * model in currentArray) {//得到下一页的所有节点
            [nextJiedianArray addObjectsFromArray:[self loadNextshuWithDic:model]];
        }
        [currentArray removeAllObjects];
        currentArray = [NSMutableArray arrayWithArray:nextJiedianArray];
    }
    return allArray;
}

- (NSMutableArray *)loadNextshuWithDic:(ThreeModel *)threeModel{
    NSInteger leftJiedian = 0;
    NSInteger rightJiedian = 0;
    
    if (threeModel.currentJiedian>threeModel.father) {
        leftJiedian =threeModel.currentJiedian - (threeModel.currentJiedian-threeModel.father)/2;
        rightJiedian = threeModel.currentJiedian +(threeModel.currentJiedian-threeModel.father)/2;
    }else{
        leftJiedian = threeModel.currentJiedian - (threeModel.father-threeModel.currentJiedian)/2;
        rightJiedian = threeModel.currentJiedian +(threeModel.father-threeModel.currentJiedian)/2;
    }
    
    ThreeModel * left=[[ThreeModel alloc]init];
    left.currentJiedian=leftJiedian;
    left.father=threeModel.currentJiedian;
    
    ThreeModel * right=[[ThreeModel alloc]init];
    right.currentJiedian=rightJiedian;
    right.father=threeModel.currentJiedian;
   
    NSMutableArray * array=[NSMutableArray arrayWithCapacity:0];
    [array addObject:left];
    [array addObject:right];
    return array;
}

- (NSMutableArray *)loadJiedianmodelToArray:(NSMutableArray *)array{
    NSMutableArray * tempArray=[NSMutableArray arrayWithCapacity:0];
    for (ThreeModel * model in array) {
        [tempArray addObject:[NSString stringWithFormat:@"%ld",model.currentJiedian]];
    }
    return tempArray;
}
@end




