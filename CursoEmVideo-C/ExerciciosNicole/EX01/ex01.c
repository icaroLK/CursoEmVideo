#include <stdio.h>
#include <locale.h>
int main(){
    setlocale(LC_ALL, "Portuguese");

    float n1, n2, aux;
    printf("Insira o primeiro valor: ");
    scanf("%f", &n1);
    fflush(stdin);
    printf("Insira o segundo valor: ");
    scanf("%f", &n2);
    fflush(stdin);

    aux = n1 + n2;

    printf("%.1f + %.1f = %.2f", n1, n2, aux);



return 0;
}
