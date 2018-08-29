//
//  FiveViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/8/29.
//  Copyright © 2018年 sjt. All rights reserved.
//
/**
 TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，它将返回一个简化的URL http://tinyurl.com/4e9iAk.
 
 要求：设计一个 TinyURL 的加密 encode 和解密 encode 的方法。你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。
 */

#import "FiveViewController.h"

#define LastUrlCount 6
@interface FiveViewController ()
@property (nonatomic ,copy)NSString * headStr;
@property (nonatomic ,strong)NSMutableDictionary * dic;
@property (nonatomic ,strong)NSMutableArray * suijiArray;
@end

@implementation FiveViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    self.headStr=@"http://tinyurl.com/";
    NSString * tostr=@"https://leetcode.com/problems/design-tinyurl";
    NSString * returnStr=[self toEncode:tostr];
    NSString * endStr=[self toDencode:returnStr];
    NSLog(@"%@ - %@",returnStr,endStr);
    
}

- (NSMutableArray *)suijiArray {
    if (!_suijiArray) {
        _suijiArray=[NSMutableArray arrayWithCapacity:0];
        
        for (NSInteger i=0; i<26; i++) {
            char hh='A'+i;
            char zz = 'a'+i;
            NSInteger index= i;
            [_suijiArray addObject:[NSString stringWithFormat:@"%c",hh]];
            [_suijiArray addObject:[NSString stringWithFormat:@"%c",zz]];
            if (i<10) {
                [_suijiArray addObject:[NSString stringWithFormat:@"%ld",index]];
            }
        }
    }
    return _suijiArray;
}

- (NSMutableDictionary *)dic
{
    if (!_dic) {
        _dic=[NSMutableDictionary dictionaryWithCapacity:0];
    }
    return _dic;
}

- (NSString *)toEncode:(NSString *)str{
    //先判断 str 是否存在
    if([[self.dic allKeys] containsObject:str]) {
        return [self.dic objectForKey:str];
    }else{
        NSString * someStr=[self retbitString];
        NSString * end = [NSString stringWithFormat:@"%@%@",self.headStr,someStr];
        [self.dic setObject:someStr forKey:str];
        return end;
    }
}

// 此方法随机字符串， 修改代码红色数字可以改变 随机产生的位数。
- (NSString *)retbitString
{
    NSString *string = [[NSString alloc]init];
    for (int i =0; i<LastUrlCount; i++) {
        int x =arc4random() % self.suijiArray.count;
        NSString *tempString = [NSString stringWithFormat:@"%@", self.suijiArray[x]];
        string = [string stringByAppendingString:tempString];
        
    }
    return string;
}

- (NSString *)toDencode:(NSString *)str{
    
    NSString * end = [str substringWithRange:NSMakeRange(str.length-LastUrlCount, LastUrlCount)];
    //得到数据
    
    for (NSString * key in [self.dic allKeys]) {
        NSString * value=[self.dic objectForKey:key];
        if ([value isEqualToString:end]) {
            return key;
        }
    }
    return @"";
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
