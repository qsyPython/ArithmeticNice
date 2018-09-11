//
//  Thirteen ViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/10.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
 
 二叉树的根是数组中的最大元素。
 左子树是通过数组中最大值左边部分构造出的最大二叉树。
 右子树是通过数组中最大值右边部分构造出的最大二叉树。
 通过给定的数组构建最大二叉树，并且输出这个树的根节点。
 
 Example 1:
 
 输入: [3,2,1,6,0,5]
 输入: 返回下面这棵树的根节点：
 
   6
 /   \
 3     5
 \    /
 2    0
 \
 1
 注意:
 
 给定的数组的大小在 [1, 1000] 之间。
 */

#import "Thirteen ViewController.h"
#import "ThreeModel.h"
@interface Thirteen_ViewController ()
@property (nonatomic ,strong)ThreeModel * rootModel;
@end

@implementation Thirteen_ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
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
