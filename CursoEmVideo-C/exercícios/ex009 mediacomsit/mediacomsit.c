#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    float n1, n2;
    printf("Nota 1: ");
    scanf("%f", &n1);
  //  fflush(stdin);
    printf("Nota 2: ");
    scanf("%f", &n2);
    float media = (n1 + n2)/2;
    printf("\nM�dia: %.2f", media);

    char *sit = (media>=7)?"Aprovado":"Reprovado";

    printf("\nSitua��o: %s", sit);


}
