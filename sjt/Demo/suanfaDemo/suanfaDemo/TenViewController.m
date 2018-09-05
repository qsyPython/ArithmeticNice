//
//  TenViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/5.
//  Copyright © 2018年 sjt. All rights reserved.
//

#import "TenViewController.h"
#import "ThreeModel.h"

@interface TenViewController ()
@property (nonatomic , strong)ThreeModel * rootModel;
@end

@implementation TenViewController

- (void)viewDidLoad {
    [super viewDidLoad];

    [self sendArray:@[@"1",@"2",@"2",@"3",@"4",@"5",@"6"]];
}


- (void)sendArray:(NSArray *)array{
    
    for (NSString * str in array) {
        [self addJiedian:str];
    }
    
    if (self.rootModel) {//root 存在
        [self isFanzhuan:self.rootModel];
    }
}

- (void)isFanzhuan:(ThreeModel *)model{
    
    if (!model) {
        return;
    }
    ThreeModel * leftModel=model.leftJiedian;
    ThreeModel * rightModel=model.rightJiedian;
    ThreeModel * tempmodel=leftModel;
    model.rightJiedian=tempmodel;
    model.leftJiedian=rightModel;
    
    [self isFanzhuan:model.rightJiedian];
    [self isFanzhuan:model.leftJiedian];
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
                break;
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

/*
 #pragma mark - Navigation
 
 // In a storyboard-based application, you will often want to do a little preparation before navigation
 - (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
 // Get the new view controller using [segue destinationViewController].
 // Pass the selected object to the new view controller.
 }
 */

@end
