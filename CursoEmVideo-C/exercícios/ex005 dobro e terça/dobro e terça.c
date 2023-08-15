#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    printf("Insira um número: ");
    int num;
    scanf("%i", &num);

    float t = 3;
    float eta = num/t;

    printf("\nAnalisando o número \"%i\"\nSeu dobro é %i\nSua terça parte é %.2f", num, num*2, eta);


}
