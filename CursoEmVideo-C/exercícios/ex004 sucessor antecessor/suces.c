#include <stdio.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "Portuguese");
    int num;

    printf("Digite um número: ");
    scanf("%i", &num);


    int ant = num - 1;
    int suc = num + 1;



    printf("\nO número digitado foi: %i\nSeu antecessor é %i\nSeu sucessor é %i\n\n", num, ant, suc);


    printf("Digite uma letra: ");
    fflush(stdin);
    char let;
    let = getchar();

    printf("A letra digitada foi: %c\n", let);
    printf("A letra anterior é %c\n", let-1);
    printf("A próxima letra é %c\n\n\n", let+1);
}
