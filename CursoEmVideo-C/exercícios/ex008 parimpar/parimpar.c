#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int num;
    printf("Digite o um n�mero: ");
    scanf("%i", &num);

    char *res = (num%2==0)?"par":"�mpar";
    printf("O n�mero %i � %s.\n\n", num, res);





}
