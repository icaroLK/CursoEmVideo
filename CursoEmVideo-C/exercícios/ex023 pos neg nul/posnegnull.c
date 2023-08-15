#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int num;
    printf("Insira um número: ");
    scanf("%i", &num);
    if (num>0) printf("Positivo");
    else if (num<0)printf("Negativo");
    else printf("Nulo");



}
