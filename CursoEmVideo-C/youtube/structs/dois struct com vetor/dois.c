#include <stdio.h>
#include <string.h>
#include <locale.h>

#define TAM 3


struct tipo_pessoa{
    char nome[50];
    int idade;
    float peso;
};


typedef struct tipo_pessoa tipo_pessoa;




int main(){
    setlocale(LC_ALL, "Portuguese");

    tipo_pessoa lista[TAM];



    for(int i=0; i < TAM; i++){

        printf("\n\nCadastro %d", i+1);
        printf("\nNome: ");
        gets(lista[i].nome);
        fflush(stdin);

        printf("Idade: ");
        scanf("%i", &lista[i].idade);
        fflush(stdin);

        printf("Peso: ");
        scanf("%f", &lista[i].peso);
        fflush(stdin);
    };


    for(int vez=0; vez < TAM; vez++){
        printf("\n\n===CADASTRO %d===", vez+1);
        printf("\nNome: %s", lista[vez].nome);
        printf("\nIdade: %d", lista[vez].idade);
        printf("\nPeso: %.2f", lista[vez].peso);
    }


printf("\n\n\n");
return 0;
}
