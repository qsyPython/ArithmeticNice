//
//  FortyOneViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/10/29.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 求2个数的最小公倍数 和 最大公约
 */

#import "FortyOneViewController.h"

@interface FortyOneViewController ()

@end

@implementation FortyOneViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}

- (void)sendNum:(NSInteger)num withOtherNum:(NSInteger)otherNum{
    
    CGFloat maxYueshu = 0;
    CGFloat minbeishu = 0;
    NSInteger max=num>otherNum?num:otherNum;
    for (NSInteger i = 1; i<max; i++) {
        if (num%i==0&&otherNum/i) {
            maxYueshu =i;
            minbeishu =i;
        }
    }
    
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
