#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int num, deslc, left, right;
    printf("Insira um n�mero: ");
    scanf("%i", &num);
    printf("Insira um deslocamento: ");
    scanf("%i", &deslc);
    right = num>>deslc;
    left = num<<deslc;
    printf("\n-----OPERA��ES SHIFT-----");
    printf("\n%i >> %i = %i", num, deslc, right);
    printf("\n%i << %i - %i\n\n", num, deslc, left);



}
