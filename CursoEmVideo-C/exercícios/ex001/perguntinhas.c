#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    printf("Insira seu nome: ");
    char nome[30];
    gets(nome);

    printf("Insira sua idade: ");
    unsigned int idade;
    scanf("%u", &idade);

    printf("Insira seu peso: ");
    float peso;
    scanf("%f", &peso);

    printf("Muito prazer, %s. Você tem %u anos e pesa %.1fKg", nome, idade, peso);





}
