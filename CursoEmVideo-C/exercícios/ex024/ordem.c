#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int n1, n2;
    printf("1° número: ");
    fflush(stdin);
    scanf("%i", &n1);
    printf("2° número: ");
    fflush(stdin);
    scanf("%i", &n2);

    if(n1>n2) printf("Os números em ordem crescente ficam: %i -> %i", n2, n1);
    else if (n1<n2) printf("Os números em ordem crescente ficam: %i -> %i", n1, n2);
    else printf("Os números são igual, então não há ordem crescente");
}
