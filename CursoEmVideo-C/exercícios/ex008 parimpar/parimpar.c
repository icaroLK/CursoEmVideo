#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int num;
    printf("Digite o um número: ");
    scanf("%i", &num);

    char *res = (num%2==0)?"par":"ímpar";
    printf("O número %i é %s.\n\n", num, res);





}
