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
@property (nonatomic ,strong)NSMutableArray * array;
@property (nonatomic ,assign)NSInteger num;
@property (nonatomic ,strong)ThreeModel * rootModel;
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSArray * array=@[@"1",@"2",@"3",@"4",@"5",@"6",@"7",@"3",@"1",@"4"];
    [self sendArray:array];
}


- (void)sendArray:(NSArray *)array{
    NSInteger maxindex=[self findMaxZuobiaoindex:array];
    NSArray * arrayleft=[array subarrayWithRange:NSMakeRange(0, maxindex)];
    NSArray * arryright=[array subarrayWithRange:NSMakeRange(maxindex+1, array.count-maxindex-1)];
    
    self.rootModel=[[ThreeModel alloc]initwithJiedian:array[maxindex]];
    self.rootModel.leftJiedian=[self addTreeModelwithArray:arrayleft];
    self.rootModel.rightJiedian=[self addTreeModelwithArray:arryright];
    
    
    
}

- (ThreeModel *)addTreeModelwithArray:(NSArray *)array{
    ThreeModel * model=[[ThreeModel alloc]initwithJiedian:array[0]];
    for (NSInteger i=1; i<array.count; i++) {
        [self addJiedian:array[i] withThreeModel:model];
    }
    return model;
}

- (void)addJiedian:(NSString *)str withThreeModel:(ThreeModel *)model{
    ThreeModel * addModel=[[ThreeModel alloc]initwithJiedian:str];
    
    NSMutableArray * array=[NSMutableArray arrayWithCapacity:0];
    [array addObject:model];
    while (array.count) {
        ThreeModel * tempModel=[array firstObject];
        [array removeObjectAtIndex:0];
        if (!tempModel.leftJiedian) {
            tempModel.leftJiedian=addModel;
            break;
        }else{
            [array addObject:tempModel.leftJiedian];
        }
    }
}



- (NSInteger)findMaxZuobiaoindex:(NSArray *)array{
    NSInteger index=0;
    NSInteger maxnum=[array[0] integerValue];
    for (NSInteger i=1; i<array.count; i++) {
        if ([array[i] integerValue]>maxnum) {
            maxnum=[array[i] integerValue];
            index=i;
        }
    }
    
    return index;
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
