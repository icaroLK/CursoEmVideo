#include <stdio.h>
#include <locale.h>
#include <time.h>
void main(){
    setlocale(LC_ALL, "Portuguese");

    time_t t;
    time(&t);
    struct tm *data;
    data = localtime(&t);
    int ano = data->tm_year+1900;

    int nasc, idade;

    printf("Atualmente estamos no ano de %i", ano);
    printf("\nEm que ano você nasceu? ");
    scanf("%i", &nasc);
    idade = ano - nasc;

    if (idade>18){
        printf("Sua idade atual é %i anos", idade);
        printf("\nSeu alistamento foi em %i", nasc+18);
    } else if(idade < 18){
        printf("Sua idade atual é %i anos", idade);
        printf("\nSeu alistamento será em %i. Ainda faltam %i anos", nasc+18, 18-idade);
    }else{
        printf("Você completa 18 anos esse ano!!! Se prepare para se alistar");
    }












}
