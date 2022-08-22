#include<stdio.h>
int main(){
    int x;
    printf("What is your choice? :\n 1) Addition of two numbers\n 2) Subtraction of two numbers\n 3) Alternate Sum and DIfference of 9 numbers\n 4) Division of two numbers\n 5) Average of 7 numbers\n 6) Multiplication of two numbers\n 7)Area and Perimeter of a rectangle or a square:\n");
    scanf("%d", &x);
    if(x==1){

        int a, b;
        scanf("%d", &a);
        scanf("%d", &b);
        printf("%d\n", a+b);

    }

    if(x==2){

        int a, b;
        scanf("%d", &a);
        scanf("%d", &b);
        printf("%d", a-b);

    }
    if(x==3){

        int a, b, c, d, e, f, g, h, i;
        scanf("%d", &a);
        scanf("%d", &b);
        scanf("%d", &c);
        scanf("%d", &d);
        scanf("%d", &e);
        scanf("%d", &f);
        scanf("%d", &g);
        scanf("%d", &h);
        scanf("%d", &i);
        
        
        printf("%d\n", a-b+c-d+e-f+g-h+i);

    }
    if(x==4){
        int a, b;
        scanf("%d", &a);
        scanf("%d", &b);
        printf("%d\n", a/b);


    }

    if(x==5){

        int a, b, c, d, e, f, g;
        scanf("%d", &a);
        scanf("%d", &b);
        scanf("%d", &c);
        scanf("%d", &d);
        scanf("%d", &e);
        scanf("%d", &f);
        scanf("%d", &g);
        
        
        
        printf("%d\n", (a+b+c+d+e+f+g)/7);

    }

    if(x==6){
        int a, b;
        scanf("%d", &a);
        scanf("%d", &b);
        printf("%d\n", a*b);


    }
    if(x==7){
        int a, b;
        scanf("%d", &a);
        scanf("%d", &b);
        printf("%d\n", a*b);
        printf("%d\n", 2*(a+b));


    }

}
