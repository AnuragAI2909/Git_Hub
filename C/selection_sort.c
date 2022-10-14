#include<stdio.h>
void selection_sort(int arr[], int size)
{
    int temp=0;
    for(int i=0;i<size-1;i++)
    {
        for(int j=i+1;j<size;j++)
        {
            if(arr[i]>arr[j])
            {
                temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
}
void display(int arr[],int size)
{
    printf("The  sorted array elements are \n :");
    for(int i=0;i<size;i++)
    {
        printf("%d, ",arr[i]);
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
    selection_sort(arr,size);
    display(arr, size);
}