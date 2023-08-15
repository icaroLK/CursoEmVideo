#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");

    char nome1[20], nome2[20], nome3[20];
    char sex1, sex2, sex3;
    float nota1, nota2, nota3;

    printf("Cadastrando a primeira pessoa:\n");
    printf("------------------------------\n");
    printf("Nome: ");
    gets(nome1);

    printf("Sexo [M/F]: ");
    sex1 = getchar();
    fflush(stdin);

    printf("Nota: ");
    scanf("%f", &nota1);

    printf("\nCadastrando a segunda pessoa:\n");
    printf("-------------------------------\n");
    fflush(stdin);

    printf("Nome: ");
    gets(nome2);

    printf("Sexo [M/F]: ");
    sex2 = getchar();

    printf("Nota: ");
    scanf("%f", &nota2);
    fflush(stdin);

    printf("\nCadastrando a terceira pessoa:\n");
    printf("-----------------------------\n");
    fflush(stdin);

    printf("Nome: ");
    gets(nome3);

    printf("Sexo [M/F]: ");
    sex3 = getchar();

    printf("Nota: ");
    scanf("%f", &nota3);


    printf("\n-----------------------------\n");
    printf("NOME\t\tSexo\tNota\n");
    printf("%s\t\t%4c\t%.2f\n", nome1, sex1, nota1);
    printf("%s\t\t%4c\t%5.2f\n", nome2, sex2, nota2);
    printf("%s\t\t%4c\t%5.2f\n", nome3, sex3, nota3);
    printf("-----------------------------\n\n\n");



}
