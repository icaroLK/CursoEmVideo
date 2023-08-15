#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    float n1, n2, m;
    printf("Insira a 1° nota: ");
    scanf("%f", &n1);
    printf("Insira a 2° nota: ");
    scanf("%f", &n2);
    m = (n1 + n2) / 2;
    printf("-----------------\n");
    if (m>=8){
        printf("Meus parabéns!!!\n");
    }
    printf("Média final: %.2f", m);
    printf("\n-----------------");

}
