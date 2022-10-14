#include<stdio.h>
#include<stdio.h>
#include<conio.h>
void search(int arr[], int n, int x)
{
    int temp=0;
    for(int i=0;i<n; i++)
    {
    if(arr[i]==x) 
    {
        temp=i;
    }
    }
if(temp==0)
{
    printf("Element %d is not found ",x);
}
else
{
  printf("Element %d is found at %d  ",x,temp+1);
}
}
void main()
{
    int arr[100];
    int x,i,n;
    printf("Enter the size of the array: \n");
    scanf("%d",&n);
    printf("Enter the array elements: \n");
    for(i=0;i<n;i++)
    {
      scanf("%d",&arr[i]);
    }
    printf("Enter the search elemnt: \n");
    scanf("%d",&x);
    search(arr,n,x);
}


