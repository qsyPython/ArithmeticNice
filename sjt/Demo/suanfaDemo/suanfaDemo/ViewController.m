//
//  ViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/8/23.
//  Copyright © 2018年 sjt. All rights reserved.
//



#import "ViewController.h"
#import "TwoViewController.h"
@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSString * str=@"AaHHSJSJjdksdhsldlks";
    NSString * strJJ=@"As";
    NSString * response=[self loadCountAllStr:str withAllStr:strJJ];
    NSLog(@"%@",response);
}

- (NSString *)loadCountAllStr:(NSString *)allStr withAllStr:(NSString *)str {
    NSInteger index=0;
    for (int i=0; i<allStr.length; i++) {
        NSString * charStr= [allStr substringWithRange:NSMakeRange(i, 1)];
        if ([str containsString:charStr]) {
            index++;
        }
    }
    return [NSString stringWithFormat:@"str == %ld个",index];
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
