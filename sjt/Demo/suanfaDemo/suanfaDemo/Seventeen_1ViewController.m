//
//  Seventeen_1ViewController.m
//  suanfaDemo
//
//  Created by sjt on 2018/9/13.
//  Copyright © 2018年 sjt. All rights reserved.

/**
 
 一维数组的应用:
 如给定的[27000,32000,32500,27500,30000,29000,31000,32500,30000,26000]
 
 交互1、
 用户输入1：表示 Display employee salary显示员工的薪水
 用户输入2：表示 Modify employee salary 修改员工的薪水
 用户输入3：表示 Quit 退出
 
 交互2、
 若交互1中输入的为1：用户还需要输入上面一维列表的位数，如输入1，对应着输出32000
 若交互1中输入的为2：用户还需要输入上面一维列表的位数，如输入1，则再次增加输入交互3：新的薪水如38000，替换掉一维列表中的32000，返回
 若交互1中输入的为3：直接返回
 */

#import "Seventeen_1ViewController.h"

typedef enum : NSUInteger {
    Nomal_type = 0,//请选择交互1
    ShowType =1,//交互1 的选择
    ChangeType = 2,//交互1 的选择
    Quit = 3,//交互1 的选择
    ChangeType_SelectNum = 4,//交互 2的2的位数
} selectStatus;

@interface Seventeen_1ViewController ()<UITextFieldDelegate>
{
    NSInteger  lastnum;
}
@property (nonatomic ,strong)NSMutableArray *salaryArray;
@property (nonatomic ,assign)selectStatus status;
@property (nonatomic ,strong)UILabel  * tishiLab;
@property (nonatomic ,strong)UITextField * textFeild;
@end

@implementation Seventeen_1ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.salaryArray=[NSMutableArray arrayWithArray:@[@"2700",@"3200",@"7500",@"2900",@"32500",@"20000"]];
    
    self.tishiLab=[[UILabel alloc]initWithFrame:CGRectMake(0, 64, 320, 20)];
    self.tishiLab.textColor=[UIColor grayColor];
    self.tishiLab.font=[UIFont systemFontOfSize:14.0f];
    self.tishiLab.textAlignment=NSTextAlignmentCenter;
    [self.view addSubview:self.tishiLab];
    
    self.textFeild=[[UITextField alloc]initWithFrame:CGRectMake(16, 64+20, 100, 30)];
    self.textFeild.textColor=[UIColor blackColor];
    self.textFeild.font=[UIFont systemFontOfSize:18.0f];
    self.textFeild.delegate=self;
    self.textFeild.returnKeyType = UIReturnKeyDone;
    [self.view addSubview:self.textFeild];
    
    _status=Nomal_type;
    [self refresh];
}

- (void)refresh{
    if (_status==Nomal_type) {
        self.tishiLab.text=@"请输入选择项：1 显示薪水  2 修改薪水 3 退出";
        self.textFeild.placeholder=@"请输入";
        self.textFeild.text=@"";
        [self.textFeild becomeFirstResponder];
    }else if (_status==ShowType){
        self.tishiLab.text=@"请输入第几位工号的薪水";
        self.textFeild.placeholder=@"请输入";
        self.textFeild.text=@"";
    }else if (_status==ChangeType){
        self.tishiLab.text=@"请输入要修改员工的工号";
        self.textFeild.placeholder=@"请输入";
        self.textFeild.text=@"";
    }else if (_status==Quit){
        _status = Nomal_type;
        [self refresh];
    }else if (_status==ChangeType_SelectNum){
        self.tishiLab.text=[NSString stringWithFormat:@"请输入要修改%ld号员工的薪水",lastnum];
        self.textFeild.placeholder=@"请输入";
        self.textFeild.text=@"";
    }
}


- (BOOL)textFieldShouldReturn:(UITextField *)textField
{
    NSInteger index=[textField.text integerValue];
    if (index>=0) {
        if (_status==Nomal_type) {
            if (index>=1&&index<=3) {
                _status=index;
                [self refresh];
            }else{
                self.tishiLab.text=@"请重新输入";
            }
        }else if (_status==ShowType){
            if (index<self.salaryArray.count) {
                self.tishiLab.text=[NSString stringWithFormat:@"您选择了显示第%ld位员工的薪水，薪水为:%@",index,self.salaryArray[index]];
                _status=Nomal_type;
                [self performSelector:@selector(refresh) withObject:nil afterDelay:4.0f];
            }else{
                self.tishiLab.text=@"请重新输入";
            }
        }else if (_status==ChangeType){
            if (index<self.salaryArray.count) {
                lastnum=index;
                self.tishiLab.text=[NSString stringWithFormat:@"您选择了修改第%ld位员工的薪水",index];
                _status=ChangeType_SelectNum;
                [self refresh];
            }else{
                self.tishiLab.text=@"请重新输入";
            }
        }else if (_status==ChangeType_SelectNum){
            self.tishiLab.text=[NSString stringWithFormat:@"已将%ld号员工的薪水由%@换成%@",lastnum,_salaryArray[lastnum],textField.text];
            _salaryArray[lastnum]=textField.text;
            _status=Nomal_type;
            [self performSelector:@selector(refresh) withObject:nil afterDelay:4.0f];
        }
        return YES;
    }
    return NO;

}

- (BOOL)textField:(UITextField *)textField shouldChangeCharactersInRange:(NSRange)range replacementString:(NSString *)string
{
    
//    NSString *text = [textField text];
    // 只能输入数字
    NSCharacterSet *characterSet = [NSCharacterSet characterSetWithCharactersInString:@"0123456789\b"];
    string = [string stringByReplacingOccurrencesOfString:@" "withString:@""];
    if ([string rangeOfCharacterFromSet:[characterSet invertedSet]].location !=NSNotFound)
    {
        return NO;
    }
    
    return YES;
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
