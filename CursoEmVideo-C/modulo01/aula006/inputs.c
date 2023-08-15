#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");

    printf("Insira seu nome: ");
    char nome[30];
    gets(nome);
    printf("Insira seu sexo [M/F]: ");
    char sex;
    fflush(stdin);
    scanf("%c", &sex);
    printf("Insira sua idade: ");
    int n;
    scanf("%i",&n);
    printf("Insira seu peso: ");
    float p;
    scanf("%f",&p);
    printf("Nome: %s\nSexo: %c\nIdade: %i\nPeso: %.1f",nome, sex, n, p);
/*********************************************
    printf("Insira seu nome: ");
    char *nome;
    scanf("%s",&nome);
    printf("Prazer em te conhecer, %s", nome);
**********************************************/


}
