#include<stdio.h>
#include<conio.h>
int ar[100],choice,n,top,x,i;
void push();
void(pop);
void display();
int main()
{
    top=-1;
    printf("Enter the size of the array:")
    scanf("%d",&n)
    printf("\n\t 1.PUSH \n\t 2.POP\n\t ");
    do 
    {
        printf("Enter the choice:")
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:
            {
                push();
                display();
                break;
            }
            case 2:
            {
                pop();
                display();
                break;
            }
            default:
            {
                printf("Please enter the valid choice:")
            }
        }
    }
    while(choice!=2);
    return 0;
}
void push()
{
    if(top>=n-1)
    {printf("\n Stack is overflow")}
}