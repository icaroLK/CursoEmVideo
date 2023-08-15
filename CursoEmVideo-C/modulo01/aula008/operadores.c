#include <stdio.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "Portuguese");
    int a = 3;
    int b = 2;
    int r = a + b;
    printf("A soma de %i com %i é igual a %i", a, b, r);



    char letra1 = 'A';
    char letranew = letra1 + 1;
    printf("A primeira letra foi %c e a segunda foi %c", letra1, letranew);

}
