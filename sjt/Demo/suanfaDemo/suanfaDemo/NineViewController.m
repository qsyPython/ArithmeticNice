
//
//  NineViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/4.
//  Copyright © 2018年 sjt. All rights reserved.
//
/***
 给定一个二叉树，检查它是否是镜像对称的。
 
 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
 
 1
 / \
 2   2
 / \ / \
 3  4 4  3
 5 6 7 8 8 7 6 5
 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
 
 1
 / \
 2   2
 \   \
 3    3
 */
#import "ThreeModel.h"

#import "NineViewController.h"

@interface NineViewController ()
@property (nonatomic , strong)ThreeModel * rootModel;
@property (nonatomic , assign)BOOL isDuicheng;
@end

@implementation NineViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    [self sendArray:@[@"1",@"0",@"1",@"1",@"0",@"1",@"0"]];
}

- (void)sendArray:(NSArray *)array{
    
    for (NSString * str in array) {
        [self addJiedian:str];
    }
    
    if (self.rootModel) {//root 存在
        [self isDuicheng:self.rootModel.leftJiedian withRightModel:self.rootModel.rightJiedian];
        if  (_isDuicheng) {
            NSLog(@"对称");
        }else{
            NSLog(@"不对称");
        }
    }
}

- (void)isDuicheng:(ThreeModel *)leftModel withRightModel:(ThreeModel *)rightModel{
    
    
    if (leftModel==nil&&leftModel==nil) {
        return ;//结束
    }else if ((leftModel&&rightModel==nil)||(rightModel&&leftModel==nil)){
        _isDuicheng=NO;
        return;
    }
    
    if ([leftModel.jiedian isEqualToString:rightModel.jiedian]) {
        
    }else{
        _isDuicheng =NO;
    }
    
    
    [self isDuicheng:leftModel.leftJiedian withRightModel:rightModel.rightJiedian];
    [self isDuicheng:leftModel.rightJiedian withRightModel:rightModel.leftJiedian];
    
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





#pragma mark ----ahhahah
- (BOOL)isDuichengArray:(NSArray *)array{
    NSInteger m = log2(array.count+1);//计算2的深度
    if (m<2) {
        return YES;
    }
    NSArray * linshiArray=@[];
    NSInteger star=1;
    NSInteger length =0;
    for (NSInteger i = 2; i<=m; i++) {
        star=star+length;
        length=pow(2, i-1);
        linshiArray = [array subarrayWithRange:NSMakeRange(star, length)];
        if (![self isDuicheng:linshiArray]) {
            
            return NO;
        }
    }
    
    return YES;
}

- (BOOL)isDuicheng:(NSArray *)array{
    for(NSInteger i = 0;i < array.count/2;i++){ //循环数组长度的一半次
        //比较元素
        if([array[i] integerValue]!= [array[(array.count - i - 1)] integerValue]){
            return NO;
            break; //结束循环
        }
    }
    return YES;
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
