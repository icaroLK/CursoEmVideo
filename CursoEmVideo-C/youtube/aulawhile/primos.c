#include <stdio.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "Portuguese");
 /*   int qtd;
    printf("Insira a quantidade: ");
    scanf("%i", &qtd);
*/

/*
    int i = 1;
    while(i<=10){
        printf("%i\n",i);
        i++;
    }
*/
/*
    int i = 1;
    do {
        printf("%i ", i);
        i++;
    }while(i<=10);
*/
/*
    int i;
    for(i=1; i<=10; i++){
        printf("%i ", i);
    }
*/

    int i;
    for(i=1; i<=10; i++){
        printf("%i ", i);
        if(i==5){
            printf("Ih ala kkkk");
        }


    }


}
