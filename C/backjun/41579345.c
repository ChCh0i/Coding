#include <stdio.h>
int main()
{
	int a;
	int str[1000001]={};
	scanf("%d",&a);
	for(int i=0; i<a; i++){
		scanf("%d",&str[i]);
	}
	int min=str[0];
	int max=str[0];
	for(int i=0; i<a; i++){
		if(min > str[i]){
			min = str[i];
		}
		if(max < str[i]){
			max = str[i];
		}
	}
	printf("%d %d",min,max);
}
