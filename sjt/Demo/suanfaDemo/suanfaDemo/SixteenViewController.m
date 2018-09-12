//
//  SixteenViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/12.
//  Copyright © 2018年 sjt. All rights reserved.
//
/**
1维数组倒置
 [@"1",@"2",@"3",@"4",@"5"]
 变为
 [@"5",@"4",@"3",@"2",@"1"]
 
 */
#import "SixteenViewController.h"

@interface SixteenViewController ()

@end

@implementation SixteenViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSMutableArray *originArr = @[@"1",@"2",@"3",@"4",@"5"].mutableCopy;
    NSArray *desArr = [self inverstArr:originArr start:0 end:(originArr.count-1)];
    NSLog(@"%@",desArr);
    // Do any additional setup after loading the view.
}

- (NSArray *)inverstArr:(NSMutableArray *)array start:(long)start end:(long)end {
    while (start<end) {
        NSString *tempStr = [array objectAtIndex:start];
        [array replaceObjectAtIndex:start withObject:[array objectAtIndex:end]];
        [array replaceObjectAtIndex:end withObject:tempStr];
        start++;
        end--;
    }
    return array;
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
