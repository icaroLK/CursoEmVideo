#include <stdio.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "Portuguese");
    int num;

    printf("Digite um n�mero: ");
    scanf("%i", &num);


    int ant = num - 1;
    int suc = num + 1;



    printf("\nO n�mero digitado foi: %i\nSeu antecessor � %i\nSeu sucessor � %i\n\n", num, ant, suc);


    printf("Digite uma letra: ");
    fflush(stdin);
    char let;
    let = getchar();

    printf("A letra digitada foi: %c\n", let);
    printf("A letra anterior � %c\n", let-1);
    printf("A pr�xima letra � %c\n\n\n", let+1);
}
