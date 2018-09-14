//
//  Eighteen_1ViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/14.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 明天数据结构和算法的加餐：
 一维数组的高级应用
 设计一个可容纳40位数的求n!
 输入：某个数字n
 输出：该数字的n!,
 并要求n!的结果在40位以内
 
 例如：
 输入：12
 输出：
 1!= 1
 2!= 2
 3!= 6
 4!= 24
 5!= 120
 6!= 720
 7!= 5040
 8!= 40320
 9!= 362880
 10!= 3628800
 11!= 39916800
 12!= 479001600
 */

#import "Eighteen_1ViewController.h"

@interface Eighteen_1ViewController ()

@end

@implementation Eighteen_1ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    [self sendNumber:20];
}

- (void)sendNumber:(NSInteger )num{
   
    for (NSInteger i = 1; i<=num; i++) {
        NSInteger idx = [self jiecheng:i];
        NSString * str=[NSString stringWithFormat:@"%ld",idx];
        if (str.length>40) {
            break;
        }
        NSLog(@"%ld!=%@",i,str);
    }
    
}

- (long long)jiecheng:(long long)index{
    if (index==1) {
        return 1;
    }else{
        return index*[self jiecheng:index-1];
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
