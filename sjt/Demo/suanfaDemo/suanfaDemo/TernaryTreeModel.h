//
//  TernaryTreeModel.h
//  suanfaDemo
//
//  Created by sjt on 2018/10/17.
//  Copyright © 2018年 sjt. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface TernaryTreeModel : NSObject
@property (nonatomic, strong)TernaryTreeModel * leftJiedian;
@property (nonatomic, strong)TernaryTreeModel * midderJiedian;
@property (nonatomic, strong)TernaryTreeModel * rightJiedian;
@property (nonatomic ,copy) NSString * title;
@end
