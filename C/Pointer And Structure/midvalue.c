#include<stdio.h>
#include<conio.h>
int *Fmid(int ar[], int len)
{
    return &ar[len/2];
}

int main()
{
    int ar[] = {1,2,3,4,56};
    int len=6;
    int *mid = Fmid(ar, len);
    printf("%d ", *mid);
    printf("%p ", mid);                                 //print the address of the pointer
    return 0;
}
