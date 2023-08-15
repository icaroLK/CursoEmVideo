#include <stdio.h>
#include <locale.h>
#include <time.h>
void main(){
    setlocale(LC_ALL, "Portuguese");

    time_t t;
    time(&t);
    struct tm*data;
    data = localtime(&t);
    int ano = data->tm_year+1900;
    int nasc;
    printf("Em que ano você nasceu? ");
    scanf("%i", &nasc);
    int idade = ano - nasc;
    printf("Você tem %i anos", idade);
    if(idade>=60){
        printf("\nPor favor dirija-se a fila preferencial");
    }
    printf("\nSeja bem vindo ao Kucha's Bank!");




}
