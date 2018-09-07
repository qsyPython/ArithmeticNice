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
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.array=[NSMutableArray arrayWithCapacity:0];
    _num=0;
    [self sendNumberx:1 widthY:4];
}

- (void)sendNumberx:(NSInteger)x widthY:(NSInteger)y{
    if (x>=0&&x<231&&y>=0&&y<231) {
        //得到x的二进制
        [self loadNumber:x];
        NSMutableArray * xarray=[NSMutableArray arrayWithArray:self.array];
        [self.array removeAllObjects];
        //得到y的二进制
        [self loadNumber:y];
        NSMutableArray * yArray=[NSMutableArray arrayWithArray:self.array];
        [self.array removeAllObjects];
        //得到两个二进制的最大长度
        NSInteger maxCount = xarray.count>=yArray.count?xarray.count:yArray.count;
        
        xarray=[self loadMaxArray:xarray withMax:maxCount];
        yArray=[self loadMaxArray:yArray withMax:maxCount];
        
        for (NSInteger i=0; i<maxCount; i++) {
            NSString * xstr=xarray[i];
            NSString * ystr=yArray[i];
            if (![ystr isEqualToString:xstr]) {
                _num++;
            }
        }
        NSLog(@"%ld和%ld****距离:%ld",x,y,_num);
    }else{
        return;
    }
}


- (NSMutableArray *)loadMaxArray:(NSMutableArray *)array withMax:(NSInteger)max{
    NSInteger tempIndex = max-array.count;
    if (tempIndex==0) {
        return array;
    }
    
    for (NSInteger i =0; i<tempIndex; i++) {
        [array insertObject:@"0" atIndex:0];
    }
    
    return array;
}

//得到二进制数组
- (void)loadNumber:(NSInteger)index{
    if (index==0) {
        return;
    }
    NSInteger shang = index/2;
    NSInteger yushu = index%2;
    [self.array insertObject:[NSString stringWithFormat:@"%ld",yushu] atIndex:0];
    [self loadNumber:shang];
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
