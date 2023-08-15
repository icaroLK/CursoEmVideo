#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    printf("Produto: ");
    char prod[20];
    gets(prod);
    printf("Preço de %s: R$", prod);
    float preco;
    scanf("%f", &preco);
    printf("Desconto: (%%) ");
    int desc;
    scanf("%i", &desc);

    float fina;

    fina = preco - (desc * preco / 100);

    printf("\nO produto \"%s\" custava R$%.2f, mas com %i%% de desconto passou a ficar R$%.2f\n\n", prod, preco, desc, fina);


}
