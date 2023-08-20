#include <stdio.h>
#include <stdlib.h>

int maxXY(int x, int y);
int minXY(int x, int y);




int main(){
    int a, b, c, maior, menor;
    printf("Insira o valor de A: ");
    scanf("%i", &a);
    printf("Insira o valor de B: ");
    scanf("%i", &b);
    printf("Insira o valor de C: ");
    scanf("%i", &c);

    maior = maxXY(maxXY(maxXY(a,b), maxXY(a,c)), maxXY(b,c));
    printf("O maior numero digitado foi: %i\n", maior);
/*
    menor = minXY(minXY(minXY(a,b), minXY(a,c)), minXY(b,c));
    printf("O menor numero digitado foi: %i", menor);
*/


return 0;
}

int maxXY(int x, int y){
    return (x + y + abs(x - y))/2;
}

int minXY(int x, int y){
    return (x - y + abs(x+y))/2;
}
