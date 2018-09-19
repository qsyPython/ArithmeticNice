//
//  Twenty_1ViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/19.
//  Copyright © 2018年 sjt. All rights reserved.
/*****
 给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。
 
 注意:
 
 给定的整数保证在32位带符号整数的范围内。
 你可以假定二进制数不包含前导零位。
 示例 1:
 
 输入: 5
 输出: 2
 解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。
 示例 2:
 
 输入: 1
 输出: 0
 解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。
 
 算法加餐：
 3维数组的表示
 输入：给定2个3维数组，按照对应位置获取拿到对应和的值，不同位置的补零处理，并输出一个新的3维数组


 */

#import "Twenty_1ViewController.h"

@interface Twenty_1ViewController ()

@end

@implementation Twenty_1ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSInteger index=1;
    NSMutableArray * array=[NSMutableArray arrayWithCapacity:0];
    [self loadNumber:index withArray:array];//得到倒数
    NSLog(@"\n作业1：\n输入:%ld\n输出:%ld",index,[self loadBushuNumWithArray:array]);
    NSArray * threeArray1=@[@[@[@"1"],@[@"2"],@[@"3"]],
                          @[@[@"4"],@[@"5"],@[@"6"]],
                          @[@[@"7"],@[@"8"],@[@"9"]]];
    NSArray * threeArray2=@[@[@[@"9"],@[@"8"]],@[@[@"6"],@[@"5"]]];
    
    NSMutableArray * threeArray=[self sendThreeArray1:threeArray1 withArray2:threeArray2];
    NSLog(@"结果:%@\n",[threeArray description]);
}

- (NSInteger)loadBushuNumWithArray:(NSMutableArray *)array{
    NSInteger sum = 0;
    NSInteger zhishu = 0;
    NSInteger num = 0;
    for (NSInteger i = array.count-1; i>=0; i--) {
        num = [array[i] integerValue]*pow(2, zhishu);
        sum+=num;
        zhishu++;
    }
    return sum;
}

- (void)loadNumber:(NSInteger)index withArray:(NSMutableArray *)array{
    if (index==0) {
        return;
    }
    NSInteger shang = index/2;
    NSInteger yushu = index%2;
    if (yushu==1) {
        yushu=0;
    }else{
        yushu=1;
    }
    [array addObject:[NSString stringWithFormat:@"%ld",yushu]];
    [self loadNumber:shang withArray:array];
}

- (NSMutableArray *)sendThreeArray1:(NSArray *)array1 withArray2:(NSArray *)array2{
    NSMutableArray * tempArray=[NSMutableArray arrayWithCapacity:0];
    NSInteger max = array1.count>array2.count?array1.count:array2.count;
    NSInteger twoMax = 0;
    NSInteger threeMax =0;
    NSInteger num = 0;
    for (NSInteger i=0; i<max; i++) {
        NSMutableArray * twoTempArray=[NSMutableArray arrayWithCapacity:0];
        NSMutableArray * twoarray1=nil;
        NSMutableArray * twoarray2=nil;
        twoMax=0;
        if (array1&&i<array1.count) {
            twoarray1=array1[i];
            twoMax=twoarray1.count;
        }
        
        if (array2&&i<array2.count) {
            twoarray2=array2[i];
            if (twoarray2.count>twoMax) {
                twoMax=twoarray2.count;
            }
        }
        
        for (NSInteger j =0; j<twoMax; j++) {
            threeMax=0;
            NSMutableArray * threeTempArray=[NSMutableArray arrayWithCapacity:0];
            NSMutableArray * threearray1=nil;
            NSMutableArray * threearray2=nil;
            if (twoarray1!=nil&&j<twoarray1.count) {
                threearray1=twoarray1[j];
                threeMax=threearray1.count;
            }
            
            if (twoarray2!=nil&&j<twoarray2.count) {
                threearray2=twoarray2[j];
                if (threearray2.count>threeMax) {
                    threeMax=threearray2.count;
                }
            }
            for (NSInteger k = 0; k<threeMax; k++) {
                num =0;
                if (threearray1!=nil&&k<threearray1.count) {
                    num=[threearray1[k] integerValue];
                }
                if (threearray2!=nil&&k<threearray2.count) {
                     num+=[threearray2[k] integerValue];
                }
                [threeTempArray addObject:[NSString stringWithFormat:@"%ld",num]];
            }
            if (threeTempArray.count>0) {
                [twoTempArray addObject:threeTempArray];
            }
           
        }
        if (twoTempArray.count>0) {
           [tempArray addObject:twoTempArray];
        }
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
