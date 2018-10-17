//
//  ThityThreeViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/10/17.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 今天看个叉树的题：给定一个 N 叉树，找到其最大深度。
 
 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
 
 例如，给定一个 3叉树 :

 我们应返回其最大深度，3。
 
 说明:
 
 树的深度不会超过 1000。
 树的节点总不会超过 5000。
 */

#import "ThityThreeViewController.h"
#import "TernaryTreeModel.h"
@interface ThityThreeViewController ()
@property (nonatomic ,strong)TernaryTreeModel * rootModel;
@end

@implementation ThityThreeViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    [self createThreeModel:@[@"1",@"2",@"",@"3",@"4",@"5",@"6",@"",@"7"]];
}

- (void)createThreeModel:(NSArray *)array{
    for (NSString * str in array) {
        [self addJieDian:str];
    }
    NSInteger cunt = 0;
    [self jisuanLeft:self.rootModel.leftJiedian wiftMidder:self.rootModel.midderJiedian withRight:self.rootModel.rightJiedian withIndex:cunt];
    
}


- (NSInteger)loadMaxLength{
    NSInteger index = 0;
    NSInteger i =0;
    
    
    
    return index;
}

- (void)jisuanLeft:(TernaryTreeModel *)left wiftMidder:(TernaryTreeModel *)midder withRight:(TernaryTreeModel *)right withIndex:(NSInteger)index{
    if ((left&&left.title.length>0)||(midder&&midder.title.length>0)||(right&&right.title.length>0)) {
        index++;//存在下一个 则++
        if (left&&left.title.length>0) {
            [self jisuanLeft:left.leftJiedian wiftMidder:left.midderJiedian withRight:left.rightJiedian withIndex:index];
        }
        
        if (midder&&midder.title.length>0) {
            [self jisuanLeft:midder.leftJiedian wiftMidder:midder.midderJiedian withRight:midder.rightJiedian withIndex:index];
        }
        
        if (right&&right.title.length>0) {
            [self jisuanLeft:right.leftJiedian wiftMidder:right.midderJiedian withRight:right.rightJiedian withIndex:index];
        }
        
    }
    
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
