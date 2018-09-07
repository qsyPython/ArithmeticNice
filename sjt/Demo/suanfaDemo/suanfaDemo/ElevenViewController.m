//
//  ElevenViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/6.
//  Copyright © 2018年 sjt. All rights reserved.
/***
 *
 给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。
 
 返回移除了所有不包含 1 的子树的原二叉树。
 
 ( 节点 X 的子树为 X 本身，以及所有 X 的后代。)
 
 示例1:
 输入: [1,null,0,0,1]
 输出: [1,null,0,null,1]
 
 解释:
 只有红色节点满足条件“所有不包含 1 的子树”。
 右图为返回的答案。
 
 
 示例2:
 输入: [1,0,1,0,0,0,1]
 输出: [1,null,1,null,1]
 
 
 
 示例3:
 输入: [1,1,0,1,1,0,1,0]
 输出: [1,1,0,1,1,null,1]
        1
      1      0
   1    1   0   1

 
 
 说明:
 
 给定的二叉树最多有 100 个节点。
 每个节点的值只会为 0 或 1 。
 */

#import "ElevenViewController.h"
#import "ThreeModel.h"
@interface ElevenViewController ()
@property (nonatomic , strong)ThreeModel * rootModel;
@property (nonatomic , strong)NSMutableArray * array;
@end

@implementation ElevenViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.array=[NSMutableArray arrayWithCapacity:0];
    [self sendArray:@[@"1",@"1",@"0",@"1",@"1",@"0",@"1",@"0"]];
}


- (void)sendArray:(NSArray *)array{
    
    for (NSString * str in array) {
        [self addJiedian:str];
    }
    
    if (self.rootModel) {//root 存在
        [self shanxuan:self.rootModel];
        [self changeThreeModel:self.rootModel];
        NSLog(@"%@",[self.array description]);
    }
}


- (void)changeThreeModel:(ThreeModel *)model{
    NSMutableArray * tempArray=[NSMutableArray arrayWithCapacity:0];
    [tempArray addObject:self.rootModel];
    NSMutableArray * nextCengArray=[NSMutableArray arrayWithCapacity:0];
    
    while (tempArray.count) {
        [nextCengArray removeAllObjects];
        for (NSInteger i=0; i<tempArray.count; i++) {
            ThreeModel * model=tempArray[i];
            
            [self.array addObject:model.jiedian];
            if (model.isKong==YES) {
                continue;
            }
            
            if (model.leftJiedian) {
                if (!(model.leftJiedian.isKong==YES&&(model.rightJiedian==nil||(model.rightJiedian&&model.rightJiedian.isKong==YES)))) {
                    [nextCengArray addObject:model.leftJiedian];
                }
            }
            
            if (model.rightJiedian) {
                if (!(model.rightJiedian.isKong==YES&&(model.leftJiedian==nil||(model.leftJiedian&&model.leftJiedian.isKong==YES)))) {
                    [nextCengArray addObject:model.rightJiedian];
                }
            }
        }
        [tempArray removeAllObjects];
        [tempArray addObjectsFromArray:nextCengArray];
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


- (void)shanxuan:(ThreeModel *)model{
    if (model==nil) {
        return;
    }
    ThreeModel * leftJiedian=model.leftJiedian;
    ThreeModel * rightJiedian = model.rightJiedian;
    
    if (leftJiedian==nil&&rightJiedian==nil) {
        if (![model.jiedian isEqualToString:@"1"]) {//如果当前model没有子节点 且本身不为"1",那么本节点为 "";
            model.jiedian=@"";
            model.isKong=YES;
        }
    }else{
        [self shanxuan:leftJiedian];
        [self shanxuan:rightJiedian];
        BOOL isleftKong=NO;
        BOOL isrightKong=NO;
        if (leftJiedian) {
            if (leftJiedian.isKong==YES) {
                isleftKong=YES;
            }
        }else{
            isleftKong=YES;
        }
        
        if (rightJiedian) {
            if (rightJiedian.isKong==YES) {
                isrightKong=YES;
            }
        }else{
            isrightKong=YES;
        }
        
        if (isleftKong&&isrightKong) {//同时为空
            if (![model.jiedian isEqualToString:@"1"]) {//如果当前model没有子节点 且本身不为"1",那么本节点为 "";
                model.jiedian=@"";
                model.isKong=YES;
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
