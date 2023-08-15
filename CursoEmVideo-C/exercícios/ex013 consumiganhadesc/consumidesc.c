#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    float p, fim;
    printf("Valor total das compras: R$");
    scanf("%f", &p);
    printf("Você gastou R$%.2f na nossa loja", p);
    if (p>=500){
        printf("\n=========ATENÇÃO=========");
        printf("\nAo gastar mais de R$500 em compras, você recebe 10%% de desconto!!!");
        fim = p - (p*10/100);
        printf("\nO valor a ser pago é R$%.2f", fim);

    }
    printf("\nVolte sempre!");


}
