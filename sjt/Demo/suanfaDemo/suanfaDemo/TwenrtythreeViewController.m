//
//  TwenrtythreeViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/25.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
 American keyboard
 示例1:
 输入: ["Hello", "Alaska", "Dad", "Peace"]
 输出: ["Alaska", "Dad"]
 注意:
 
 你可以重复使用键盘上同一字符。
 你可以假设输入的字符串将只包含字母。
 qwertyuiop
 asdfghjkl
 zxcvbnm
 */

#import "TwenrtythreeViewController.h"

@interface TwenrtythreeViewController ()
@property (nonatomic ,strong)NSArray * zimuArray;
@end

@implementation TwenrtythreeViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    NSMutableArray * tenpArray=[self sendArray:@[@"Hello", @"Alaska", @"Dad", @"Peace"]];
    NSLog(@"%@",[tenpArray description]);
}

- (NSMutableArray *)sendArray:(NSArray *)array{
    NSMutableArray * tempArray=[NSMutableArray arrayWithCapacity:0];
    char temp;
    NSString * charStr=@"";
    for (NSInteger i=0; i<array.count; i++) {
        NSString * str=array[i];
        NSInteger index = 4;
        for (NSInteger j=0; j<str.length; j++) {
            temp=[str characterAtIndex:j];
            if ([str characterAtIndex:j]>='A'&[str characterAtIndex:j]<='Z') {
                temp=temp+32;
            }
            charStr =[NSString stringWithFormat:@"%c",temp];
            
            NSInteger local=[self zifuislocal:charStr];
            if (index==4) {
                index=local;
            }else{
                if (index!=local) {
                    break;
                }else{
                    if (j==str.length-1) {
                        [tempArray addObject:str];
                    }
                }
            }
        }
    }
    return tempArray;
}

- (NSInteger)zifuislocal:(NSString *)str{
    NSInteger local = 0;
    for (NSInteger i=0; i<self.zimuArray.count; i++) {
        NSArray * array=self.zimuArray[i];
        if ([array containsObject:str]) {
            local=i;
            break;
        }
    }
    return local;
}

- (NSArray *)zimuArray
{
    if (!_zimuArray) {
        _zimuArray=@[@[@"q",@"w",@"e",@"r",@"t",@"y",@"u",@"i",@"o",@"p"]
                     ,@[@"a",@"s",@"d",@"f",@"g",@"h",@"j",@"k",@"l"]
                     ,@[@"z",@"x",@"c",@"v",@"b",@"n",@"m"]];
    }
    return _zimuArray;
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
