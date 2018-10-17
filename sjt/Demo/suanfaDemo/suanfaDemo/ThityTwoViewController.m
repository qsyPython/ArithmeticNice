//
//  ThityTwoViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/10/16.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
 
 现有一个链表 -- head = [4,5,1,9]，它可以表示为:
 
 4 -> 5 -> 1 -> 9
 示例 1:
 
 输入: head = [4,5,1,9], node = 5
 输出: [4,1,9]
 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
 示例 2:
 
 输入: head = [4,5,1,9], node = 1
 输出: [4,5,9]
 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 说明:
 
 链表至少包含两个节点。
 链表中所有节点的值都是唯一的。
 给定的节点为非末尾节点并且一定是链表中的一个有效节点。
 不要从你的函数中返回任何结果。
 */

#import "ThityTwoViewController.h"
#import "ChainModel.h"
@interface ThityTwoViewController ()

@end

@implementation ThityTwoViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    [self createChainModel];
    
}

- (void)createChainModel{
    
    NSArray * name1=@[@"1",@"2",@"3",@"4",@"5"];
    ChainModel * modelc= [[ChainModel alloc]init];
    modelc.title=name1[0];
    [self createModelWithArray:name1 withModel:modelc];
    
   ChainModel * newModel = [self sendNode:@"5" withModel:modelc];
    ChainModel * newModelIndex = [self sendNodeIndex:1 withModel:modelc];
   NSLog(@"%@%@",newModel,newModelIndex);
}

- (ChainModel *)sendNode:(NSString *)node withModel:(ChainModel *)chainModel{
    
    ChainModel * supperModel = nil;
    ChainModel * currentModel = chainModel;
    while (currentModel!=nil) {
        if ([currentModel.title isEqualToString:node]) {
            ChainModel * nextModel = currentModel.nextModel;
            if (supperModel!=nil) {
                supperModel.nextModel = nextModel;
            }else{
                return currentModel.nextModel;
            }
            break;
        }else{
            supperModel = currentModel;
            currentModel = currentModel.nextModel;
        }
    }
    return chainModel;
}

- (ChainModel *)sendNodeIndex:(NSInteger)index withModel:(ChainModel *)chainModel{
    
    ChainModel * supperModel = nil;
    ChainModel * currentModel = chainModel;
    NSInteger i =0;
    while (currentModel!=nil) {
        if (i == index) {
            ChainModel * nextModel = currentModel.nextModel;
            if (supperModel!=nil) {
                supperModel.nextModel = nextModel;
            }else{
                return currentModel.nextModel;
            }
            break;
        }else{
            supperModel = currentModel;
            currentModel = currentModel.nextModel;
        }
        i++;
    }
    return chainModel;
}

- (void)createModelWithArray:(NSArray *)array withModel:(ChainModel *)model{
    NSInteger i = 1;
    ChainModel * nextModel=model;
    while (i<array.count) {
        ChainModel * model = [[ChainModel alloc]init];
        NSString * str = array[i];
        model.title=str;
        nextModel.nextModel=model;
        
        nextModel=model;
        i++;
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
