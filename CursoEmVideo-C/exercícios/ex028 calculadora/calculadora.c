#include <stdio.h>
#include <locale.h>
#include <string.h>

void main(){
    setlocale(LC_ALL, "Portuguese");
    float n1, n2;
    char resp;
    printf("1° número: ");
    fflush(stdin);
    scanf("%f", &n1);
    printf("2° número: ");
    fflush(stdin);
    scanf("%f", &n2);
    printf("=====================");
    printf("\n+\tAdição\n-\tSubtração\n*\tMultiplicação\n/\tDivisão");
    printf("\n=====================");
    printf("\nR: ");
    fflush(stdin);
    resp = getchar();


    switch(resp){
    case '+':
        printf("O resultado de %.1f + %.1f é igual a %.1f", n1, n2, n1 + n2);
        break;
    case '-':
        printf("O resultado de %.1f - %.1f é igual a %.1f", n1, n2, n1 - n2);
        break;
    case '*':
        printf("O resultado de %.1f * %.1f é igual a %.1f", n1, n2, n1 * n2);
        break;
    case '/':
        printf("O resultado de %.1f / %.1f é igual a %.1f", n1, n2, n1 / n2);
        break;
    }





/*******************************************************************************
    if (resp == '+') {
        printf("O resultado de %.1f + %.1f é igual a %.1f", n1, n2, n1 + n2);
    } else if (resp == '-') {
        printf("O resultado de %.1f - %.1f é igual a %.1f", n1, n2, n1 - n2);
    } else if (resp == '*') {
        printf("O resultado de %.1f * %.1f é igual a %.1f", n1, n2, n1 * n2);
    } else if (resp == '/') {
        printf("O resultado de %.1f / %.1f é igual a %.2f", n1, n2, n1 / n2);
    } else {
        printf("Opção inválida.");
    }
********************************************************************************/

}

