//
//  SixViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/8/30.
//  Copyright © 2018年 sjt. All rights reserved.
/***
 *对下列数据进行升序排序：[12,34,7,9,1,90,27,46,93,61,52,40]
 要求：写5种以上的排序算法，并写出对应的时间和空间复杂度，（5种排序算法必须包含：快排排序法）
 */

#import "SixViewController.h"

@interface SixViewController ()
@property (nonatomic ,copy)NSString * headStr;
@property (nonatomic ,strong)NSMutableDictionary * dic;
@property (nonatomic ,strong)NSMutableArray * shujuArray;

@end

@implementation SixViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.shujuArray = [NSMutableArray arrayWithArray:@[@"12",@"34",@"1",@"9",@"11",@"53",@"22",@"40"]];
    //    NSArray * class1=[self class1:self.shujuArray];
    //    NSLog(@"%@",class1);
    
    //    NSArray * class2=[self class2:self.shujuArray];
    //    NSLog(@"%@",class2);
    
    //    NSArray * class3=[self class3:self.shujuArray];
    //    NSLog(@"%@",class3);
    
        NSArray * class4=[self class4:self.shujuArray];
        NSLog(@"%@",class4);
    
    
    NSArray * class5=[self class5:self.shujuArray];
    NSLog(@"%@",class5);

    
}

//O(n^n)
- (NSArray *)class1:(NSMutableArray *)array{
    for (int i=0; i<array.count-1; i++) {
        for (NSInteger j = 0; j<array.count -1 -i; j++) {
            NSString * temp;
            if ([array[j] integerValue]>[array[j+1] integerValue]) {
                temp=array[j];
                array[j]=array[j+1];
                array[j+1]=temp;
            }
        }
    }
    return array;
}

//O(n^n)
- (NSArray *)class2:(NSMutableArray *)array
{
    NSString * temp;
    for(int i=0; i<array.count-1; i++){
        for(int j=i+1; j>0; j--){
            if([array[j] integerValue] < [array[j-1] integerValue]){
                temp = array[j-1];
                array[j-1] = array[j];
                array[j] = temp;
            }else{  //不需要交换
                break;
            }
        }
    }
    return array;
}

- (NSArray *)class3:(NSMutableArray *)array{
    for(int i=0;i<array.count-1;i++){
        
        int minIndex = i; //假设最小的数为i
        for(int j=i+1;j<self.shujuArray.count;j++){
            if([array[j] integerValue]< [array[minIndex] integerValue]){//如果遇到更小的
                minIndex = j;
            }
        }
        
        if(minIndex != i){//得到最小的交换
            NSString * temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
    }
    return array;
}

- (NSArray *)class4:(NSMutableArray *)array{
    self.shujuArray=[NSMutableArray arrayWithArray:array];
    [self changePaixu:0 withEnd:self.shujuArray.count-1];
    return self.shujuArray;
}

- (void)changePaixu:(NSInteger)start withEnd:(NSInteger)end{
    if (start>= end) {
        return;
    }
    NSInteger a = start;
    NSInteger b = end;
    NSString * c;
    
    c =self.shujuArray[start];
    while (a!=b) {
        
        while (([self.shujuArray[b] integerValue]>=[c integerValue])&&a<b) {
            b--;//从右边向左找到小于的那位
        }
        
        if (b>a) {
            self.shujuArray[a]=self.shujuArray[b];
        }
        
        while (([self.shujuArray[a] integerValue]<=[c integerValue])&&a<b) {
            a++;//从左边向右找到大于的那位
        }
        
        if (a<b) {
            self.shujuArray[b]=self.shujuArray[a];
        }
    }
    
    self.shujuArray[a]=c;
    //得到之后还要把两边的找到
    [self changePaixu:start withEnd:a-1];//左边
    [self changePaixu:a+1 withEnd:end];//右边
}


- (NSArray *)class5:(NSMutableArray *)array{
    NSInteger j;
    NSString * c;
    for (NSInteger i=1; i< array.count; i++) {
        //如果第i个元素小于第j个，则第j个向后移动
        for (c=array[i],j=i-1; j>=0&&([c integerValue]<[array[j] integerValue]); j--){
            array[j+1]=array[j];
        }
        array[j+1]=c;
    }
    return array;
}


@end




