#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    unsigned int idade = 18;
    float peso = 83.9;
    char *nome = "Ícaro";
    char sexo = 'M';
    printf("%s do sexo %c possui %i anos e pesa %.2fKg", nome, sexo, idade, peso);
}
