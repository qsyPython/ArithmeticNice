//
//  number.m
//  SharkORMTests
//
//  Created by 柴志勇 on 2018/8/23.
//  Copyright © 2018年 Adrian Herridge. All rights reserved.
//

#import "number.h"

@implementation number

-(NSArray*)checkSumInTwoNumberEquWithArray:(NSArray*)numArray target:(NSInteger)target
{
    NSMutableArray* array = [NSMutableArray arrayWithCapacity:2];
    if (numArray.count > 2) {
        for(int i = 0;i < numArray.count;i++){
            NSString* head = [numArray objectAtIndex:i];
            for(int k = i+1;k < numArray.count;k++){
                NSString*  next = [numArray objectAtIndex:k];
                if (target == [head intValue] + [next intValue]) {
                    [array addObject:head];
                    [array addObject:next];
                }
            }
        }
    }
    return array;
}

- (void)test_handle
{
    NSArray* sumArray = [NSArray arrayWithObjects:@"2",@"4",@"12",@"25",@"21",@"22",@"10", nil];
    NSArray* relArray =  [self checkSumInTwoNumberEquWithArray:sumArray target:6];
    
}
@end
