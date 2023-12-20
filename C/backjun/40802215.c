#include<stdio.h>
int main()
{
  int scan;
  scanf("%d",&scan);
  int num = scan;
  int x = 0;
  while(true){
    x++;
    scan = (scan%10)*10 + ((scan/10)+(scan%10))%10;
      
    if(num==scan)break;
  }
  printf("%d",x);
}
