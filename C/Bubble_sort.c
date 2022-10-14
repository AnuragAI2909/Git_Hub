#include<stdio.h>
#include<conio.h>
void main()
{
    int arr[100];
    int s,i,temp=0;
    printf("Enter the size of the array: ");
    scanf("%d",&s);
    printf("Enter the  array element: \n");
    for(i=0;i<s;i++)
     {
      scanf("%d",&arr[i]);
     }
    for(i=0;i<s-1;i++)
    {
    for(int j=0;j<s-i-1;j++)
     {
        if(arr[j]>arr[j+1])
        {
            temp=arr[j];
            arr[j]=arr[j+1];
            arr[j+1]=temp;
        }
     }
    }
    
     printf("The sorted array is :");
      for(i=0;i<s;i++)
     {
      printf("%d",arr[i]);
     }
}


    



