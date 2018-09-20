//
//  Twenty-oneViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/20.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
 
 示例 1:
 
 输入:
 1
 / \
 0   2
 
 L = 1
 R = 2
 
 输出:
 1
 \
 2
 示例 2:
 
 输入:
 3
 / \
 0  4
 \
 2
 /
 1
 
 L = 1
 R = 3
 
 输出:
 3
 /
 2
 /
 1
 */

#import "TwentyoneViewController.h"
#import "ThreeModel.h"
@interface TwentyoneViewController ()
@property (nonatomic , strong)ThreeModel * rootModel;
@property (nonatomic , assign)NSInteger min;
@property (nonatomic , assign)NSInteger max;
@end

@implementation TwentyoneViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    [self sendMinNum:1 maxNum:3 withArray:@[@"3",@"0",@"4",@"2",@"",@"",@"",@"1"]];
    
}

- (void)sendMinNum:(NSInteger)min maxNum:(NSInteger)max withArray:(NSArray *)array{
    self.min=min;
    self.max=max;
    for (NSInteger i=0; i<array.count; i++) {
        [self addJiedian:array[i]];
    }
    [self changeWith:self.rootModel.leftJiedian withRightModel:self.rootModel.rightJiedian withModel:self.rootModel];
    
}

- (void)changeWith:(ThreeModel *)leftModel withRightModel:(ThreeModel *)rightModel withModel:(ThreeModel *)superModel{
    if (leftModel&&leftModel.jiedian.length>0) {
        NSInteger num = [leftModel.jiedian integerValue];
        ThreeModel * leftsonModel=leftModel.leftJiedian;
        ThreeModel * rightsonModel=leftModel.rightJiedian;
        if (num>=_min &&num<=_max) {//说明满足条件不需要改变继续遍历
            superModel.leftJiedian=leftModel;
            [self changeWith:leftsonModel withRightModel:rightsonModel withModel:leftModel];
        }else{
            superModel.leftJiedian=nil;
            [self changeWith:leftsonModel withRightModel:rightsonModel withModel:superModel];
        }
    }
    
    if (rightModel&&rightModel.jiedian.length) {
        NSInteger num = [rightModel.jiedian integerValue];
        ThreeModel * leftsonModel=rightModel.leftJiedian;
        ThreeModel * rightsonModel=rightModel.rightJiedian;
        if (num>=_min&&num<=_max) {
            superModel.rightJiedian=rightModel;
            [self changeWith:leftsonModel withRightModel:rightsonModel withModel:rightModel];
        }else{
            superModel.rightJiedian=nil;
            [self changeWith:leftsonModel withRightModel:rightsonModel withModel:superModel];
        }
    }
    
}

- (void)addJiedian:(NSString *)str{
    ThreeModel * model=[[ThreeModel alloc]initwithJiedian:str];
    if (str.length==0) {
        model.isStop=YES;
    }
    
    if (self.rootModel==nil) {
        self.rootModel=model;
    }else{
        NSMutableArray * array=[NSMutableArray arrayWithCapacity:0];
        [array addObject:self.rootModel];
        while (array.count) {
            ThreeModel * tempModel=[array firstObject];
            [array removeObjectAtIndex:0];
            
            if (tempModel.isStop==YES) {
                continue;
            }
            
            if (!tempModel.leftJiedian) {
                tempModel.leftJiedian=model;
                break;
            }else if (!tempModel.rightJiedian){
                tempModel.rightJiedian=model;
                break;
            }else{
                [array addObject:tempModel.leftJiedian];
                [array addObject:tempModel.rightJiedian];
            }
        }
    }
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
