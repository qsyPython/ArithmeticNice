//
//  ThreeModel.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/3.
//  Copyright © 2018年 sjt. All rights reserved.
//

#import "ThreeModel.h"

@implementation ThreeModel

- (instancetype)init{
    if (self=[super init]) {
        self.father=0;
    }
    return self;
}

- (instancetype)initwithJiedian:(NSString *)jiedian{
    if (self==[super init]) {
        self.jiedian=jiedian;
        
    }
    return self;
}

@end
