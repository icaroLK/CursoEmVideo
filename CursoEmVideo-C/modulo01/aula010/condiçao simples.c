#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    float vel;
    printf("Insira a velocidade: ");
    scanf("%f", &vel);
    if(vel>=80){
        printf("Multado");
    }
    printf("Tenha um bom dia");
}
