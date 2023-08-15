#include <stdio.h>
#include <locale.h>
#include <time.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int nasc, idade;

    time_t t;
    time(&t);
    struct tm *data;
    data = localtime(&t);
    int atual = data->tm_year+1900;

    printf("Em que ano você nasceu? ");
    fflush(stdin);
    scanf("%i", &nasc);
    idade = atual - nasc;
    printf("Sua idade atual é de %i anos", idade);
    if (idade>= 18){
        printf("\nJa fez 18 anos. Esperamos que tenha se alistado!");
    } else{
        printf("\nAinda não fez 18 anos");
    }


}
