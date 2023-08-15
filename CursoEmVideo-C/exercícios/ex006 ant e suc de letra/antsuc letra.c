#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    printf("Insira um letra: ");
    char let;
    let = getchar();

    char ant = let - 1;
    char suc = let + 1;
    printf("\nLETRA %c\nAntecessor: %c\nSucessor: %c", let, ant, suc);

}
