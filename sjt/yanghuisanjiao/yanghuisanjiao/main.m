//
//  main.m
//  yanghuisanjiao
//
//  Created by sjt on 2018/9/17.
//  Copyright © 2018年 sjt. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <objc/runtime.h>
#import <stdlib.h>

void zifuchuan(int num , int max){
    
    unsigned long numLenth= 0;
    
    if (num>0) {
         printf("%d",num);
        while (num != 0)
        {
            numLenth++;
            num /= 10;
        }
       
    }else{
        numLenth=0;
    }
    
    while (numLenth<max) {
        printf(" ");
        numLenth++;
    }
}

void sendNum(int num){
    num =5;
    int n[num][num];
    int count = num*num;
    int i,j;//old坐标
    int ii,jj;
    if (num%2==1) {
        i=1;j=num/2+1;
        n[i][j]=1;
        for (int k =2; k<=count; k++) {
            ii=i-1;
            jj=j+1;
            if (ii<1) {
                ii=num;
            }
            if (jj>num) {
                jj=1;
            }
            if (0<n[ii][jj]&&n[ii][jj]<=count) {
                ii=i+1;
                jj=j;
                if (ii<0) {
                    ii=num;
                }
            }
            n[ii][jj]=k;
            i=ii;
            j=jj;
            
        }
    }else{
        
    }
    for (i = 1; i <= num; i++) {
        for (j = 1; j <= num; j++)
            printf("%d\t",n[i][j]);
        printf("\n");
    }
    
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        int count = 9;
        int sum = 0;
        int n[count+1][2*count+1];
        int maxNum= pow(2, count-1);
        int maxcount=0;
        while (maxNum != 0)
        {
            maxcount++;
            maxNum /= 10;
        }
        
        for (int i = 0; i<count+1; i++) {
            for (int j =0 ; j<2*count+1; j++) {
                if ((j==count-i)||(j==count+i)) {
                    n[i][j]=1;
                    zifuchuan(1, maxcount);
                }else{
                    if (i-1>0) {
                        sum =0;
                        if (j-1>=0) {
                            sum = n[i-1][j-1];
                        }
                        
                        if (j+1<(2*count+1)) {
                            sum+= n[i-1][j+1];
                        }
                        n[i][j]=sum;
                        zifuchuan(sum, maxcount);
                    }else
                    {
                        n[i][j]=0;
                        zifuchuan(0, maxcount);
                    }
                }
            }
            printf("\n");
            
        }
       
        sendNum(5);
        
    }
    return 0;
}






