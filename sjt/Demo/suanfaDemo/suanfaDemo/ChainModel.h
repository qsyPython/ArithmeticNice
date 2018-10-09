//
//  ChainModel.h
//  suanfaDemo
//
//  Created by sjt on 2018/10/9.
//  Copyright © 2018年 sjt. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface ChainModel : NSObject
@property (nonatomic , strong) ChainModel * nextModel;
@property (nonatomic , strong) NSString * title;
@end
