//
//  ThreeModel.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/3.
//  Copyright © 2018年 sjt. All rights reserved.
//

#import "ThreeModel.h"

@implementation ThreeModel

- (instancetype)initWithName:(NSString *)name withLeftJiedian:(ThreeModel *)leftJiedian withRightJiedian:(ThreeModel *)rightJiedian
{
    if (self=[super init]) {
        self.name=name;
        self.leftJiedian=leftJiedian;
        self.rightJiedian=rightJiedian;
    }
    return self;
}
@end
