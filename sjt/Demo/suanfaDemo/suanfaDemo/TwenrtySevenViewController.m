//
//  TwenrtySevenViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/10/9.
//  Copyright © 2018年 sjt. All rights reserved.
//
/**
 编写一个程序，找到两个单链表相交的起始节点。
 
 
 
 例如，下面的两个链表：
 
 A:          a1 → a2
                    ↘
                     c1 → c2 → c3
                     ↗
 B:     b1 → b2 → b3
 在节点 c1 开始相交。
 
 
 
 注意：
 
 如果两个链表没有交点，返回 null.
 在返回结果后，两个链表仍须保持原有的结构。
 可假定整个链表结构中没有循环。
 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
 */
#import "TwenrtySevenViewController.h"
#import "ChainModel.h"
@interface TwenrtySevenViewController ()

@end

@implementation TwenrtySevenViewController

- (void)viewDidLoad {
    [super viewDidLoad];

    [self createChainModel];
    
}

- (void)createChainModel{

    NSArray * name1=@[@"a1",@"a2",@"a3",@"a4"];
    NSArray * name2=@[@"b1",@"b2",@"b3",@"b4",@"b5",@"b6",@"b7"];
    NSArray * commen=@[@"c1",@"c2",@"c3",@"c4"];
    ChainModel * modelc= [[ChainModel alloc]init];
    modelc.title=commen[0];
    [self createModelWithArray:commen withModel:modelc withNextModel:nil];
    
    ChainModel *model1=[[ChainModel alloc]init];
    model1.title=name1[0];
    [self createModelWithArray:name1 withModel:model1 withNextModel:modelc];
    
    ChainModel *model2=[[ChainModel alloc]init];
    model2.title=name2[0];
    [self createModelWithArray:name2 withModel:model2 withNextModel:modelc];
    
    NSLog(@"是否有交点:%d",[self isjiaodianModel:model1 model2:model2]);
}

- (void)createModelWithArray:(NSArray *)array withModel:(ChainModel *)model withNextModel:(ChainModel *)nextModelC{
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
    
    if (nextModelC) {
        nextModel.nextModel=nextModelC;
    }
}


- (BOOL)isjiaodianModel:(ChainModel *)model1 model2:(ChainModel *)model2{
    
    NSInteger model1lenth = [self loadModelLenth:model1];
    NSInteger model2lenth = [self loadModelLenth:model2];
    NSInteger mylen= model1lenth-model2lenth;
    
    ChainModel * link1 = model1;
    ChainModel * link2 = model2;
    if (mylen<0) {
        link2 = model1;
        link1 = model2;
        mylen =0-mylen;
    }
    
    for (NSInteger i=0; i<mylen; i++) {
        link1=link1.nextModel;
    }
    
    while (link1!=nil&&link2!=nil && link1!=link2) {
        link1=link1.nextModel;
        link2=link2.nextModel;
    }
    
    if (link1==link2) {
        return YES;
    }
    
    return NO;
}

- (NSInteger)loadModelLenth:(ChainModel *)model{
    ChainModel * current = model;
    NSInteger i = 0;
    while (current.nextModel) {
        current= current.nextModel;
        i++;
    }
    return i;
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
