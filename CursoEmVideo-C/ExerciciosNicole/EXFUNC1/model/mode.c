#include <stdio.h>

int main(){
    int n1, n2, resultado_soma;
    printf("Insira um valor para n1: ");
    scanf("%i", &n1);

    printf("Insira um valor para n2: ");
    scanf("%i", &n2);


    resultado_soma = soma_ai(n1, n2);
    printf("SOMA: %i", resultado_soma);



return 0;
}


int soma_ai(int a, int b){;
    int result = a + b;
    return result;
}
