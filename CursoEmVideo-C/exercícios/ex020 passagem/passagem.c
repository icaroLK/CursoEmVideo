#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    float dist, p;
    printf("======= TABELA DE PREÇOS ========");
    printf("\nViagens até 200 Km\tR$0.50/Km");
    printf("\nA partit de 200 Km\tR$0.35/Km");
    printf("\n---------------------------------");
    printf("\nInsira a distância da viagem: ");
    fflush(stdin);
    scanf("%f", &dist);
    if (dist>200){
        p = dist * 0.35;
    } else{
        p = dist * 0.5;
    }
    printf("Uma viagem de %.0f Km vai custar R$%.2f\n\n", dist, p);
}
