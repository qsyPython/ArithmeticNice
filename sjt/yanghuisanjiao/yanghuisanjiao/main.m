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

void Exchange(int **pj, int tr, int tc, int n) {
    n++;
    if (1 <= tr && tr <= n / 2 && 1 <= tc && tc <= n) {
        pj[tr][tc] += pj[n - tr][n - tc];
        pj[n - tr][n - tc] = pj[tr][tc] - pj[n - tr][n - tc];
        pj[tr][tc] -= pj[n - tr][n - tc];
    }
}

void sendNum(int num){
    int n[num][num];
  
    int count = num*num;
    int i,j;//old坐标
    int x,y;
    if (num%2==1) {
        i=1;j=num/2+1;
        n[i][j]=1;
        for (int k =2; k<=count+1; k++) {
            x=i-1;
            y=j+1;
            if (x<1) {
                x=num;
            }
            
            if (y>num) {
                y=1;
            }
            
            if (0<n[x][y]&&n[x][y]<=count) {
                x=i+1;
                y=j;
                if (x<1) {
                    x=num;
                }
            }
            n[x][y]=k;
            i=x;
            j=y;
            
        }
        for (i = 1; i <= num; i++) {
            for (j = 1; j <= num; j++)
                printf("%d\t",n[i][j]);
            printf("\n");
        }
    }else{
        int **pj;
        pj = (int**)malloc(sizeof(int **) * (num + 1));
        for (i = 0; i < (num + 1); i++)
            pj[i] = (int*)malloc(sizeof(int *) *  (num + 1));
        
        if (num % 4 == 0) {
            i = 1; j = 1;
            // 1.先将数据从上到下，从左到右填入
            for (int k = 1; k <= num * num; k++) {
                pj[i][j++] = k;
                if (j > num) { j = 1; i++; }
            }
            
            // 2.将方阵的所有4*4子方阵中的两对角线上的数
            // 关于大方阵中心作中心对称交换
            
            i = 1; j = 1;
            for (int r = 0; r < num / 4 + 1; r++) {
                for (int c = 0; c < num / 4 + !(r % 2); c++) {
                    
                    x = 2 * r + i;
                    y = 4 * c + r % 2 * 2 + j;
                    
                    Exchange(pj, x, y, num);
                    Exchange(pj, x - 1, y, num);
                    Exchange(pj, x, y - 1, num);
                    Exchange(pj, x - 1, y - 1, num);
                }
            }
            for (i = 1; i <= num; i++) {
                for (j = 1; j <= num; j++)
                    printf("%d\t",pj[i][j]);
                printf("\n");
            }
        }
    }
    
    
}

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

void yanghuisanjiao(int num){
    int count = num;
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
}

void jiaohuanJuzhen(int num){
    int old[2][6]= {{1,2,3,4,5,6},{7,8,9,10,11,12}};
    int hang = sizeof(old[0])/sizeof(int);
    int lie = sizeof(old)/sizeof(int)/hang;
    int new[lie][hang];
    int someNum;

    
    
}


int main(int argc, const char * argv[]) {
    @autoreleasepool {
//        printf("魔方矩阵\n");
//        sendNum(5);
//        printf("杨辉三角\n");
//        yanghuisanjiao(5);
        printf("翻转");
        jiaohuanJuzhen(0);
        
    }
    return 0;
}








