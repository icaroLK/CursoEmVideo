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


    printf("\nInsira o hor�rio do filme: ");
    fflush(stdin);
    scanf("%i", &hora);


    printf("\nHor�rio do filme: %ih - Pre�o do ingresso: R$20", hora);
    printf("\n-----------------------------------------------");
    printf("\nInsira seu saldo: R$");
    fflush(stdin);
    scanf("%f", &sald);

    printf("Hor�rio atual:   %i:%i", h, m);
    if (sald>=20 && hora>h){
        printf("\nVoc� consegue comprar o ingresso\n\n");
    }else {
        printf("\nVoc� n�o consegue comprar o ingresso\n\n");
    }


}
