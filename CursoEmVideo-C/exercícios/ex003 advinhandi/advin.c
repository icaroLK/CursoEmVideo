#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <time.h>

void main(){
    setlocale(LC_ALL, "Portuguese");
    printf("Vou pensar num n�mero entre 1 e 5. Tente adivinhar!\n");
    printf("Qual seu papite? ");
    unsigned int pal;
    scanf("%u", &pal);
    srand(time(NULL));
    unsigned int n = rand() % 5 + 1;

    printf("Eu pensei no n�mero %u e voc� pensou no %u", n, pal);

}
