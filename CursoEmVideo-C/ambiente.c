#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    int n1, n2;
    n1 = 15;
    n2 = 1;

    printf("O resultado é %i", n1<<n2);

}
