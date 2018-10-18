//
//  ThityfourViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/10/18.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 今天的算法题：N叉树的前序遍历
 给定一个 N 叉树，返回其节点值的前序遍历。
 
 例如，给定一个 3叉树 :
 
 
 
 
 
 返回其前序遍历: [1,3,5,6,2,4]。
 */

#import "ThityfourViewController.h"
#import "TernaryTreeModel.h"
@interface ThityfourViewController ()
@property (nonatomic ,strong)TernaryTreeModel * rootModel;
@end

@implementation ThityfourViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self createThreeModel:@[@"1",@"3",@"2",@"4",@"5",@"6"]];
}

- (void)createThreeModel:(NSArray *)array{
    for (NSString * str in array) {
        [self addJieDian:str];
    }
    NSMutableArray * arrayaaaa = [self qianxuBianli];
    NSLog(@"%@",[arrayaaaa description]);
    NSMutableArray * arraybbbb = [self houxuBianli];
    NSLog(@"hou:%@",[arraybbbb description]);
}

- (NSMutableArray *)qianxuBianli{
    NSMutableArray * array=[NSMutableArray arrayWithCapacity:0];
    [array addObject:self.rootModel.title];
    [self bianliLeft:self.rootModel.leftJiedian withRight:self.rootModel.midderJiedian withRight:self.rootModel.rightJiedian withArray:array];
    
    return array;
}

- (void)bianliLeft:(TernaryTreeModel *)left withRight:(TernaryTreeModel *)midder withRight:(TernaryTreeModel *)right withArray:(NSMutableArray *)array{
    if (left&&left.title.length>0) {
        [array addObject:left.title];
        
        [self bianliLeft:left.leftJiedian withRight:left.midderJiedian withRight:left.rightJiedian withArray:array];
    }
    
    if (midder&&midder.title.length>0) {
          [array addObject:midder.title];
        [self bianliLeft:midder.leftJiedian withRight:midder.midderJiedian withRight:midder.rightJiedian withArray:array];
    }
    
    if (right&&right.title.length>0) {
        [array addObject:right.title];
        [self bianliLeft:right.leftJiedian withRight:right.midderJiedian withRight:right.rightJiedian withArray:array];
    }
}

- (NSMutableArray *)houxuBianli{
    NSMutableArray * titieArray = [NSMutableArray arrayWithCapacity:0];

    
    NSMutableArray * array=[NSMutableArray arrayWithCapacity:0];
    [array addObject:self.rootModel];
    while (array.count) {
        TernaryTreeModel * tempModel=[array firstObject];
        [array removeObjectAtIndex:0];
        
        if (tempModel.title.length==0) {
            continue;
        }else{
            [titieArray addObject:tempModel.title];
        }
        
        if (tempModel.leftJiedian) {
            [array addObject:tempModel.leftJiedian];
        }
        
        if (tempModel.midderJiedian){
            [array addObject:tempModel.midderJiedian];
     
        }
        
        if (tempModel.rightJiedian){
            [array addObject:tempModel.rightJiedian];
           
        }
         continue;
    }
    return titieArray;
}



- (void)addJieDian:(NSString *)jiedian{
    TernaryTreeModel * model =[[TernaryTreeModel alloc]init];
    model.title=jiedian;
    if (self.rootModel==nil) {
        self.rootModel=model;
    }else{
        NSMutableArray * array=[NSMutableArray arrayWithCapacity:0];
        [array addObject:self.rootModel];
        while (array.count) {
            TernaryTreeModel * tempModel=[array firstObject];
            [array removeObjectAtIndex:0];
            
            if (tempModel.title.length==0) {
                continue;
            }
            
            if (!tempModel.leftJiedian) {
                tempModel.leftJiedian=model;
                break;
            }else if (!tempModel.midderJiedian){
                tempModel.midderJiedian=model;
                break;
            }else if (!tempModel.rightJiedian){
                tempModel.rightJiedian=model;
                break;
            } else{
                [array addObject:tempModel.leftJiedian];
                [array addObject:tempModel.midderJiedian];
                [array addObject:tempModel.rightJiedian];
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
