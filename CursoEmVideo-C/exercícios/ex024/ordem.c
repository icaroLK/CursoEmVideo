#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int n1, n2;
    printf("1� n�mero: ");
    fflush(stdin);
    scanf("%i", &n1);
    printf("2� n�mero: ");
    fflush(stdin);
    scanf("%i", &n2);

    if(n1>n2) printf("Os n�meros em ordem crescente ficam: %i -> %i", n2, n1);
    else if (n1<n2) printf("Os n�meros em ordem crescente ficam: %i -> %i", n1, n2);
    else printf("Os n�meros s�o igual, ent�o n�o h� ordem crescente");
}
