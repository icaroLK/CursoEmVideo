#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int n1, n2;
    printf("Digite o 1° número: ");
    scanf("%i", &n1);
    printf("Digite o 2° número: ");
    scanf("%i", &n2);
    int maior = (n1>=n2)?n1:n2;
    printf("\nMaior valor digitado: %i", maior);


}
