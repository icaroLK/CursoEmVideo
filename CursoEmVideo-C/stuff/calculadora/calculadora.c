#include <stdio.h>
#include <locale.h>
#include <math.h>




float soma(float v1, float v2){
    float r = v1 + v2;
    return r;
}

float sub(float v1, float v2){
    float r = v1 - v2;
    return r;
}

float mult(float v1, float v2){
    float r = v1 * v2;
    return r;
}

float div(float v1, float v2){
    float r = v1 / v2;
    return r;
}

int menu(void){
    while (1){
        float opc;
        printf("\n--------------------");
        printf("\n1 - Soma");
        printf("\n2 - Subtração");
        printf("\n3 - Multiplicação");
        printf("\n4 - Divisão");
        printf("\n5 - Sair");
        printf("\n--------------------");
        printf("\n\nSua opção: ");
        scanf("%f", &opc);
        fflush(stdin);
        if(opc==1 || opc==2 || opc==3 || opc==4 || opc==5){
            return opc;
        }
        else{
            printf("\nDados inválidos!\nTente novamente");
        }
    }
}


int main(){
    setlocale(LC_ALL, "Portuguese");
    float v1, v2, res, opc;

    while(opc!=5){

    opc = menu();
    if(opc==5) break;
    printf("\nValor 1: ");
    scanf("%f", &v1);
    fflush(stdin);
    printf("Valor 2: ");
    scanf("%f", &v2);
    fflush(stdin);
    if(opc==1) printf("Resultado: %.2f",soma(v1, v2));
    else if(opc==2) printf("Resultado: %.2f", sub(v1,v2));
    else if(opc==3) printf("Resultado: %.2f", mult(v1,v2));
    else if(opc==4) printf("Resultado: %.2f", div(v1,v2));
    printf("\n\n");
}

    printf("Obrigado :)");









printf("\n\n");
return 0;
}

