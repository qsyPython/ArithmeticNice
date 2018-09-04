//
//  ThreeModel.h
//  suanfaDemo
//
//  Created by sjt on 2018/9/3.
//  Copyright © 2018年 sjt. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface ThreeModel : NSObject

- (instancetype)initwithJiedian:(NSString *)jiedian;
@property (nonatomic, assign)NSInteger currentJiedian;
@property (nonatomic, assign)NSInteger father;
@property (nonatomic, strong)ThreeModel * leftJiedian;
@property (nonatomic, strong)ThreeModel * rightJiedian;
@property (nonatomic, assign)BOOL isStop;
@property (nonatomic, copy)NSString  * jiedian;

@end
