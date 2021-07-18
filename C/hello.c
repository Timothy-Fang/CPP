#include <stdio.h>

int main()
{
    int a;
    a = 6;
    printf("sizeof(int)=%ld\n",sizeof(a));
    printf("sizeof(a)=%ld\n",sizeof(a+1.0));
    printf("a=%d\n", a);
    return 0;
}
