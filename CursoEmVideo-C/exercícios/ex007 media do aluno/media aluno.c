#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    printf("---------------------\n");
    printf("   Média de notas");
    printf("\n---------------------\n");
    printf("Nome: ");
    char nome[30];
    gets(nome);
    printf("Nota 1: ");
    float n1;
    scanf("%f", &n1);
    printf("Nota 2: ");
    float n2;
    scanf("%f", &n2);
    float media = (n1 + n2) / 2;
    printf("\nMédia do aluno \"%s\": %.2f", nome, media);

    char *sit = (media>=7)?"Aprovado":"Reprovado";
    printf("\nSituação: %s", sit);


}
