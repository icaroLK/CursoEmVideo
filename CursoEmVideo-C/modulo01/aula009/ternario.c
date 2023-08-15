#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int a = 4, b = 8;

    int c = (a>b)?1:2;

    printf("O resultado é %i", c);


}
