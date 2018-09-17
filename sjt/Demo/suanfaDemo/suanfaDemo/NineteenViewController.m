//
//  NineteenViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/17.
//  Copyright © 2018年 sjt. All rights reserved.
/**
 国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串， 比如: "a" 对应 ".-", "b" 对应 "-...", "c" 对应 "-.-.", 等等。
 
 为了方便，所有26个英文字母对应摩尔斯密码表如下：
 
 [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
 给定一个单词列表，每个单词可以写成每个字母对应摩尔斯密码的组合。例如，"cab" 可以写成 "-.-.-....-"，(即 "-.-." + "-..." + ".-"字符串的结合)。我们将这样一个连接过程称作单词翻译。
 
 返回我们可以获得所有词不同单词翻译的数量。
 
 例如:
 输入: words = ["gin", "zen", "gig", "msg"]
 输出: 2
 解释:
 各单词翻译如下:
 "gin" -> "--...-."
 "zen" -> "--...-."
 "gig" -> "--...--."
 "msg" -> "--...--."
 
 共有 2 种不同翻译, "--...-." 和 "--...--.".
 
 
 注意:
 
 单词列表words 的长度不会超过 100。
 每个单词 words[i]的长度范围为 [1, 12]。
 每个单词 words[i]只包含小写字母。
 */

#import "NineteenViewController.h"

@interface NineteenViewController ()
@property (nonatomic , strong)NSArray * guizeArray;
@end

@implementation NineteenViewController

- (NSArray *)guizeArray{
    if (!_guizeArray) {
        _guizeArray=@[@".-",@"-...",@"-.-.",@"-..",@".",@"..-.",@"--.",@"....",@"..",@".---",@"-.-",@".-..",@"--",@"-.",@"---",@".--.",@"--.-",@".-.",@"...",@"-",@"..-",@"...-",@".--",@"-..-",@"-.--",@"--.."];
    }
    return _guizeArray;
}

- (void)viewDidLoad {
    [super viewDidLoad];
    NSArray * array=@[@"gin",@"zen",@"gig",@"msg"];
    NSLog(@"%@ 有 %ld个",[array description],[self findWordCountWithArray:array]);
    
}

- (NSInteger)findWordCountWithArray:(NSArray *)array{
    if (array.count>100) {
        NSLog(@"words 大于100");
    }else{
        NSMutableArray * countArray=[NSMutableArray arrayWithCapacity:0];
        for (NSString * str in array) {
            if (str.length<12&&str.length>0) {
                NSString * hahha = [self loadDanciFanyi:str];
                if ([countArray containsObject:hahha]) {
                    continue;
                }else{
                    [countArray addObject:hahha];
                }
            }else{
                NSLog(@"单词不能大于12个字符");
            }
        }
        return countArray.count;
    }
    return 0;
}

- (NSString *)loadDanciFanyi:(NSString *)str{
    NSMutableString * tempStr=[NSMutableString string];
    for (NSInteger i=0; i<str.length; i++) {
        unichar tempIndex = [str characterAtIndex:i];
        if (tempIndex>='a' && tempIndex<='z') {
            tempIndex = tempIndex-'a';
            [tempStr appendString:[self.guizeArray objectAtIndex:tempIndex]];
        }else{
            NSLog(@"含有大写哦");
        }
    }
    return tempStr;
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
