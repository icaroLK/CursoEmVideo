#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int n;
    printf("Insira um n�mero: ");
    scanf("%i", &n);
    if (n%2==0){
        printf("O n�mero %i � par", n);
    } else{
    printf("O n�mero %i � �mpar", n);
    }
}
