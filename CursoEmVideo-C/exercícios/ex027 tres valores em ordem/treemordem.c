#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int n1,n2,n3,maior,menor,mid;
    printf("1° número: ");
    scanf("%i", &n1);


    printf("2° número: ");
    scanf("%i", &n2);


    printf("3° número: ");
    scanf("%i", &n3);




    if(n1>=n2 && n1>=n3){ //n1 maior de tudo
        maior = n1;
        if(n2>=n3){
            mid = n2;
            menor = n3;
        }else{
            mid = n3;
            menor = n2;
        }
    }

    if(n2>=n1 && n2>=n3){
        maior = n2;
        if(n1>=n3){
            mid = n1;
            menor = n3;
        }else{
            mid = n3;
            menor = n1;
        }
    }

    if(n3>=n1 && n3>=n2){
        maior = n3;
        if(n1>=n2){
            mid = n1;
            menor = n2;
        }else{
            mid = n2;
            menor = n1;
        }
    }




    printf("Ordem crescente: %i -> %i -> %i",menor,mid,maior);










}
