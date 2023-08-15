#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    float peso;
    int resp;
    printf("Seu peso na terra (Kg): ");
    fflush(stdin);
    scanf("%f", &peso);

    printf("\t  ESCOLHA UM PLANETA");
    printf("\n\t======================");
    printf("\n\t1\tMercúrio");
    printf("\n\t2\tVênus");
    printf("\n\t3\tMarte");
    printf("\n\t4\tJúpiter");
    printf("\n\t5\tSaturno");
    printf("\n\t6\tUrano");
    printf("\n\t======================");
    printf("\nR: ");
    scanf("%i", &resp);


    switch(resp){
    case 1:
        printf("Em Mercúrio, seu peso seria %.1f Kg",peso*0.37);
        break;
    case 2:
        printf("Em Vênus, seu peso seria %.1f Kg",peso*0.88);
        break;
    case 3:
        printf("Em Marte, seu peso seria %.1f Kg",peso*0.38);
        break;
    case 4:
        printf("Em Júpiter, seu peso seria %.1f Kg",peso*2.64);
        break;
    case 5:
        printf("Em Saturno, seu peso seria %.1f Kg",peso*1.15);
        break;
    case 6:
        printf("Em Urano, seu peso seria %.1f Kg",peso*1.17);
        break;
    default:
        printf("Erro");
        break;
    }


}
