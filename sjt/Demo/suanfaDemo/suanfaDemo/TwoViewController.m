//
//  TwoViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/8/24.
//  Copyright © 2018年 sjt. All rights reserved.
//

#import "TwoViewController.h"

@interface TwoViewController ()

@end

@implementation TwoViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSArray * array=@[@"6",@"2",@"8",@"56",@"33",@"3",@"5",@"6",@"2",@"8",@"56",@"33",@"3",@"5"];
    NSInteger k = 3;
    NSMutableArray * sumArray=[self sendNumsArray:array withTarget:k];
    NSLog(@"%@",[sumArray description]);
}




- (NSMutableArray *)sendNumsArray:(NSArray *)numArray withTarget:(NSInteger)index{
    NSMutableArray * tempArray=[NSMutableArray arrayWithCapacity:0];
    NSInteger tempIndex= numArray.count%index;//取余数 得到最终的前进位数
    
    for (int i=0; i<tempArray.count; i++) {
        
    }
    return tempArray;
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
