#include <stdio.h>
#include <locale.h>
#include <time.h>

void main(){
    setlocale(LC_ALL,"Portuguese");

    time_t t;
    time(&t);
    struct tm *data;
    data = localtime(&t);
    int h = data->tm_hour;
    int m = data->tm_min;




    float sald;
    int hora;
    printf("================ KUCHA'S FILMS ================");


    printf("\nInsira o horário do filme: ");
    fflush(stdin);
    scanf("%i", &hora);


    printf("\nHorário do filme: %ih - Preço do ingresso: R$20", hora);
    printf("\n-----------------------------------------------");
    printf("\nInsira seu saldo: R$");
    fflush(stdin);
    scanf("%f", &sald);

    printf("Horário atual:   %i:%i", h, m);
    if (sald>=20 && hora>h){
        printf("\nVocê consegue comprar o ingresso\n\n");
    }else {
        printf("\nVocê não consegue comprar o ingresso\n\n");
    }


}
