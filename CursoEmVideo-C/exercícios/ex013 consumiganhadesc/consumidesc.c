#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    float p, fim;
    printf("Valor total das compras: R$");
    scanf("%f", &p);
    printf("Voc� gastou R$%.2f na nossa loja", p);
    if (p>=500){
        printf("\n=========ATEN��O=========");
        printf("\nAo gastar mais de R$500 em compras, voc� recebe 10%% de desconto!!!");
        fim = p - (p*10/100);
        printf("\nO valor a ser pago � R$%.2f", fim);

    }
    printf("\nVolte sempre!");


}
