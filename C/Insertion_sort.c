#include<stdio.h>
void insertion_sort(int arr[], int size)
{
    int k,temp=0;
    for(int i=1;i<size;i++)
    {
        for(int j=0;j<i;j++)
        {
            if(arr[j]>arr[i])
            {
                temp=arr[j];
                arr[j]=arr[i];
                for(k=i;k>j;k--)
                {
                    arr[k]=arr[k-1];
                }
                arr[k+1]=temp;
            }
        }
    }
}
void display(int arr[],int size)
{
    printf("The  sorted array elements are \n :");
    for(int i=0;i<size;i++)
    {
        printf("%d ,",arr[i]);
    }
}
void main()
{
    int arr[100];
    int size;
    printf("Enter the size of array  :");
    scanf("%d",&size);
    printf("Enter the array elements :");
    for(int i=0;i<size;i++)
    {
        scanf("%d",&arr[i]);
    }
    insertion_sort(arr,size);
    display(arr, size);
}