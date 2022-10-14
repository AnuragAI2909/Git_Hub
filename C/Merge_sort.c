#include<stdio.h>
#include<conio.h>
void merge_sort(int ar1[], int ar2[], int s1,int s2)
{
    int ar3[100];
    int s3=s1+s2;
    int i=0,j=0,k=0;
    while(i<s3 && (j!=s1 || k!=s2))
    {
        if(ar1[j]<=ar2[k])
            ar3[i++]=ar1[j++];
        else 
            ar3[i++]=ar2[k++];
    }
    for(;j<s1;)
      {
         ar3[i++]=ar1[j++];
      }
    for(;k<s2;)
      {
         ar3[i++]=ar1[k++];
      }
    printf("Merged array elements is:");
    for(i=0;i<s3;i++)
    {
        printf("%d",ar3[i]);
    }
    printf("\n\n");
   
}
void main()
{
    int ar1[100],ar2[100];
    int s1,s2;
    int ar3[100];
    printf("Enter the size of  First array  :");
    scanf("%d",&s1);
    printf("Enter the first array elements :");
    for(int i=0;i<s1;i++)
    {
        scanf("%d",&ar1[i]);
    }
    printf("Enter the size of  Second  array  :");
    scanf("%d",&s2);
    int s3=s1+s2;
    printf("Enter the second array elements:");
    for(int i=0;i<s2;i++)
    {
        scanf("%d",&ar2[i]);
    }
    merge_sort(ar1,ar2,s1,s2);
}