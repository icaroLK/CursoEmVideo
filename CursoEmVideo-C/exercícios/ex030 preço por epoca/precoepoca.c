#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    float p;
    int resp;
    printf("Digita o preço  de um produto: R$");
    scanf("%f", &p);

    printf("\t      ESCOLHA UM PERÍODO");
    printf("\n\t==============================");
    printf("\n\t1\tCarnaval [+10]");
    printf("\n\t2\tFérias escolares [+20]");
    printf("\n\t3\tDia das crianças [+5]");
    printf("\n\t4\tBlack Friday [-30]");
    printf("\n\t5\tNatal [-5]");
    printf("\n\t==============================");
    printf("\nR: ");
    scanf("%i", &resp);

    switch(resp){
    case 1:
        printf("No carnaval, seu produto passa a valer R$%.2f\n\n",p+(p*10/100));
        break;
    case 2:
        printf("Nas férias escolares, seu produto passa a valer R$%.2f\n\n",p+(p*20/100));
        break;
    case 3:
        printf("No dia das crianças, seu produto passa a valer R$%.2f\n\n",p+(p*5/100));
        break;
    case 4:
        printf("Na Black Friday, seu produto passa a valer R$%.2f\n\n",p-(p*30/100));
        break;
    case 5:
        printf("No Natal, seu produto passa a valer R$%.2f\n\n",p-(p*50/100));
        break;
    default:
        printf("Você digitou errado\n\n");
        break;
    }

}
