#include<stdio.h>
#include<string.h>
char a[1000000+3] ={'0', '0' };
int main()
{
    scanf("%s",a+2);
    
    int alen = strlen(a);
 
    for(int i=alen%3; i<alen; i=i+3)
    {
        printf("%d", (a[i]-'0')*4 + (a[i+1]-'0')*2 + (a[i+2]-'0')) ;
    }
 
}
