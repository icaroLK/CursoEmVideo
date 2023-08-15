#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    printf("O %s tem %i anos\n", "Ícaro", 18);
    printf("Seu peso atual é de %.2fKg\n", 83.9);
    printf("Seu sexo é %c", 'M');


}
