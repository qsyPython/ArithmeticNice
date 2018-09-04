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
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    if ([self isDuichengArray:@[@"1",@"2",@"2",@"3",@"4",@"",@"3"]]) {
        NSLog(@"对称");
    }else{
        NSLog(@"不对称");
    }
}

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
