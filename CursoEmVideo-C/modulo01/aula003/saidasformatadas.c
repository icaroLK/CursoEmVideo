#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    printf("O %s tem %i anos\n", "�caro", 18);
    printf("Seu peso atual � de %.2fKg\n", 83.9);
    printf("Seu sexo � %c", 'M');


}
