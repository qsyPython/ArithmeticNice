//
//  ThreeModel.h
//  suanfaDemo
//
//  Created by sjt on 2018/9/3.
//  Copyright © 2018年 sjt. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface ThreeModel : NSObject
@property (nonatomic, assign)NSInteger currentJiedian;
@property (nonatomic, assign)NSInteger father;
@property (nonatomic, strong)ThreeModel * left;
@end
