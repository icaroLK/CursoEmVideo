#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int ano;
    printf("Insira um ano qualquer: ");
    scanf("%i", &ano);
    if(ano%4==0){
        if(ano%100==0 && ano%400!=0){
            printf("Não é ano bissexto");
        }else{
        printf("Ano bissexto");
        }
    }else{
        printf("Não é ano bissexto");
    }


}
