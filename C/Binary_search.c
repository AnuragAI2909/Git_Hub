#include<stdio.h>
int binary_search(int arr[],int r, int n) 
{
    int f=0;
    int l=r-1;
    int mid=(f+l)/2;
    while(f<=l)
    {
        if(arr[mid]==n)
        {
            printf("Element %d is found at index %d",n,mid+1);
            return mid;
        }
        else if(arr[mid]<n)
        {
            f=mid+1;
             break;
        }
        else
        {
            l=mid-1;
            mid=(f+l)/2;
        }
    }
}
void main()
{
    int arr[100];
    int r,n;
    printf("Enter the size of array :");
    scanf("%d",&r);
    printf("ENter the elements in the array :");
    for(int i=0;i<r;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("Enter the elements to be search :");
    scanf("%d",&n);
    int result=binary_search(arr,r,n);
}