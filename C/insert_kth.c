#include<stdio.h>
#include<conio.h>
void main()
{
    int arr[100];
    int i,n,k,x;
    printf("ENter the number of terms: \n");
    scanf("%d", &n);
    printf("ENter the number in sorted order :");
    for(i=1;i<=n;i++)
    {
    scanf("%d", &arr[i]);
    }
    printf("ENter the number to be inserted \n: ");
    scanf("%d ",&x);
    printf("ENter the position of number \n : ");
    scanf("%d ",&k);
    for(i=n;i>=k;i--)
    {
        arr[i]=arr[i-1];
        arr[k-1]=x;
    }
    printf("After insertion  array elements are :\n ");
    for(i=0;i<=n;i++)
    {
        printf("%d, ", arr[i]);
    }
}