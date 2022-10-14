#include<stdio.h>
#include<conio.h>
void Min_Max(int arr[], int len,int *min, int *max)
{
    *min=*max=arr[0];
    int i;
    for(int i=1;i<len;i++)
    {
        if(arr[i]<*min)
        {
        *min=arr[i];
        }
        if(arr[i]>*max)
            *max=arr[i];
    }
}
int main()
{
    int min,max,len;
    int arr[100];
    printf("Enter the size of array :");
    scanf("%d",&len);
    printf("ENter the elements in the array :");
    for(int i=0;i<len;i++)
    {
        scanf("%d",&arr[i]);
    }
    Min_Max(arr,len,&min,&max);
    printf("Minimum:%d ",min);
    printf("Maximum:%d ",max);
    return 0;
}