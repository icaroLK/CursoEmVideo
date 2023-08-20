#include <stdio.h>
#include <locale.h>
int main(){
    setlocale(LC_ALL, "Portuguese");
    int i;
    float f;
    char c;

    printf("Insira um valor inteiro: ");
    scanf("%i", &i);
    fflush(stdin);
    printf("Insira um único caracter: ");
    c = getchar();
    fflush(stdin);
    printf("Insira um valor com decimal: ");
    scanf("%f", &f);
    fflush(stdin);
    printf("I = %i\nF = %f\nC = %c", i, f, c);



return 0;
}
