#include<stdio.h>
#include<conio.h>

float sum(float a,float b)
{
    return (a+b);
}
float sub(float a,float b)
{
    return (a-b);
}
float mul(float a,float b)
{
    return (a*b);
}
float div(float a,float b)
{
    return (a/b);
}

int main()
{
    float (*pt2fun[ops])(float, float)=(sum,sub,mul,div);
    int ch;
    floate a,b;
    printf("Enter 0 for sum ,1 for sub,2 for mul,3 for div");
    scanf("%d",&ch);
    printf("Enter the number :");
    scanf("%f %f" ,&a,&b);
    printf("f", ptr2fun[ch](a,b));
    return 0;
}
