#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int n;
    printf("Insira um número: ");
    scanf("%i", &n);
    if (n%2==0){
        printf("O número %i é par", n);
    } else{
    printf("O número %i é ímpar", n);
    }
}
