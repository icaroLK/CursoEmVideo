#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int and, or, xor, n1, n2;
    printf("Insira o 1° valor: ");
    scanf("%i", &n1);
    printf("Insira o 2° valor: ");
    scanf("%i", &n2);
    and = n1 & n2;
    or = n1 | n2;
    xor = n1 ^ n2;
    printf("\n----- OPERAÇÕES BITWISE -----");
    printf("\n%i & %i = %i", n1, n2, and);
    printf("\n%i | %i = %i", n1, n2, or);
    printf("\n%i ^ %i = %i", n1, n2, xor);

}
