#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    printf("Insira um n�mero: ");
    int num;
    scanf("%i", &num);

    float t = 3;
    float eta = num/t;

    printf("\nAnalisando o n�mero \"%i\"\nSeu dobro � %i\nSua ter�a parte � %.2f", num, num*2, eta);


}
