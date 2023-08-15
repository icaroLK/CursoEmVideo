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

    printf("\n\nM�dia: %f", media);
    printf("\nQtd: %f", qtd);

// at� aqui fiz a m�dia dos valores

    float somatoria = 0;
    float variancia; // valor final da variancia
    float desviopad; // desvio padrao (raiz da variancia)
    float dif; // diferen�a antes de elevar ao quadrado na somat�ria




    for(int c=0; c < qtd; c++){ //somat�ria do quadrado da diferen�a entre o valor e a m�dia
        dif = (vet[c]-media);
        somatoria += pow(dif, 2);
    }
    variancia = somatoria/qtd;
    desviopad = sqrt(variancia);





    printf("\nSomat�ria: %f", somatoria);
    printf("\nVari�ncia: %f", variancia);
    printf("\nDesvio padr�o: %f", desviopad);











return 0;
}
