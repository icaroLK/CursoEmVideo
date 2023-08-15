#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int num;
    printf("Insira um número: ");
    fflush(stdin);
    scanf("%i", &num);
    switch(num){
        case 1:
            printf("Um");
            break;

        case 2:
            printf("Dois");
            break;

        case 3:
            printf("Três");
            break;

        case 4:
            printf("Quatro");
            break;

        default:
            printf("Outro");
            break;
    }
}
