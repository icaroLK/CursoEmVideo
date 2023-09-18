#include <stdio.h>

void main(){

    int qtd = 1;
    float med, soma, resp = 0;


    while(resp != -1000){
        printf("Insira um numero (-1000 para parar): ");
        scanf("%f", &resp);

        if(resp == -1000){
            break;
        }
        else if(resp > 0){
            qtd++;
            soma += resp;
        }
    }

    med = soma / qtd;

    printf("\nForam digitados %i numeros positivos", qtd);
    printf("\nA media dos numeros positivos u: %.1f\n\n", med);



return 0;

}
