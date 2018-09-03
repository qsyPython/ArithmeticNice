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
    
    NSMutableArray * array=[self toHangshu:4];
    
    NSLog(@"%@",[array description]);
}


/**                                    midder
 行数         列数   相当于所有节点      中间位置         左子节点       右子节点
  m           n    2^m-1             n/2+1          midder/2      n-midder/2+1
 hang 2    shu 3   2^2-1              2             1   2^0       3
 hang 3    shu 7   2^3-1              4             2   2^1       6
 hang 4    shu 15  2^4-1              8             4   2^2       12
 hang 5    shu 31  2^5-1              16            8   2^3
 */

- (NSMutableArray *)toHangshu:(NSInteger)m{
    NSInteger n =pow(2, m)-1;
    NSMutableArray * array=[NSMutableArray arrayWithCapacity:0];
    NSInteger midder = n/2+1;
    NSInteger leftMidder = 0;
    NSInteger rightMidder = 0;
    for (NSInteger i = 1; i<=m; i++) {//行
        NSMutableArray * tempArray=[NSMutableArray arrayWithCapacity:0];
        if (i!=1) {
            leftMidder= leftMidder/2;
            rightMidder= n - leftMidder + 1;
        }
        for (NSInteger j = 1; j<=n; j++) {//列
            if (i==1) {
                if (j==midder) {
                    [tempArray addObject:@"X"];
                    leftMidder = midder;
                }else{
                    [tempArray addObject:@" "];
                }
            }else{
                if (j==leftMidder) {
                     [tempArray addObject:@"X"];
                }else if(j==rightMidder){
                     [tempArray addObject:@"X"];
                }else{
                    [tempArray addObject:@" "];
                }
            }
        }
        [array addObject:tempArray];
    }

    return array;
}
@end




