#include <stdio.h>
#include <locale.h>


float varia(int *vetor,int qtd){
    float soma = 0, somatoria = 0, media, dif, variancia;

    // soma todos os valores do vetor
    for(int i=0; i < qtd; i++){
        soma += vetor[i];
    }
    media = soma/qtd;

    //somatória do quadrado da diferença entre o valor e a média
    for(int c=0; c < qtd; c++){
        dif = (vetor[c]-media);
        somatoria += dif * dif;
    }
    variancia = somatoria/qtd;

    return variancia;
}

int main(){
    setlocale(LC_ALL, "Portuguese");

    int vet[13] = {90,94,53,68,79,84,87,72,70,69,65,89,85};
    int qtd = sizeof(vet) / sizeof(vet[0]); //calcula o tamanho, quantos elementos tem o vetor
    printf("%f", varia(vet, qtd));



return 0;
}
