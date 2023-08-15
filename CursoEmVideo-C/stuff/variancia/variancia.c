#include <stdio.h>
#include <locale.h>
#include <math.h>




int main(){
    setlocale(LC_ALL, "Portuguese");

    int vet[13] = {90,94,53,68,79,84,87,72,70,69,65,89,85};
    float qtd = sizeof(vet) / sizeof(vet[0]); //quantidade de elementos do vetor
    float media;
    float soma = 0;
    for(int i=0; i < qtd; i++){ // soma todos os valores do vetor
        soma += vet[i];
    }
    media = soma/qtd;

    printf("\n\nMédia: %f", media);
    printf("\nQtd: %f", qtd);

// até aqui fiz a média dos valores

    float somatoria = 0;
    float variancia; // valor final da variancia
    float desviopad; // desvio padrao (raiz da variancia)
    float dif; // diferença antes de elevar ao quadrado na somatória




    for(int c=0; c < qtd; c++){ //somatória do quadrado da diferença entre o valor e a média
        dif = (vet[c]-media);
        somatoria += pow(dif, 2);
    }
    variancia = somatoria/qtd;
    desviopad = sqrt(variancia);





    printf("\nSomatória: %f", somatoria);
    printf("\nVariância: %f", variancia);
    printf("\nDesvio padrão: %f", desviopad);











return 0;
}
