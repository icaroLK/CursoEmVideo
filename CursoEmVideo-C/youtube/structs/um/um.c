#include <stdio.h>
#include <string.h>
#include <locale.h>

#define TAM 50


struct tipo_pessoa{
    int idade;
    float peso;
    char nome[TAM];
};


typedef struct tipo_pessoa pers;




int main(){
    setlocale(LC_ALL, "Portuguese");

    pers pes = {18, 85.7, "ícaro"};



    printf("Insira sua idade: ");
    scanf("%d", &pes.idade);
    fflush(stdin);
    printf("Insira seu peso: ");
    scanf("%f", &pes.peso);
    fflush(stdin);
    printf("Insira seu nome: ");
    gets(pes.nome);







    printf("======Início======");
    printf("\n posição 1: %d", pes.idade);
    printf("\n posição 2: %.2f", pes.peso);
    printf("\n posição 3: %s", pes.nome);
    printf("\n==================");


printf("\n\n\n");
return 0;
}
