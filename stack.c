#include<stdio.h>


int stack[5],top=-1,i;
int size = sizeof(stack);


int main(){




   for(i=1;i<=5;i++)
    push() ;

    //five elements are inserted in stack1


    for (i=1;i<=4;i++)
     pop();
    
    //  four elements are removed from stack
    

return 0;

}

 push()
{
  if(top==size -1 ){

    printf("overflow\n");
  }

  else{
     int x;
    printf("Enter the number\n");
    scanf("%d",&x);
     
     top+=1;
     stack[top]=x;
     
  }
}


 pop(){

    if(top==-1){
        printf("underflow\n");
    }


    else{

        printf("%d \n",stack[top]);
        top-=1;
        printf("element in stack now are\n",stack[top]);
    }
}