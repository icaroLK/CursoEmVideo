#include <stdio.h>
#include <stdlib.h>

int main(){
    int input;
    int cinq = 0, dez = 0, cinc = 0, um = 0;

    printf("Insira um valor a ser sacado: R$");
    scanf("%i", &input);

    while (input > 0){
        if (input % 50 == 0 && input >= 50){
            input -= 50;
            cinq += 1;
            continue;

        }
        else if (input % 10 == 0 && input >= 10){
            input -= 10;
            dez += 1;
            continue;

        }
        else if (input % 5 == 0 && input >= 5){
            input -= 5;
            cinc += 1;
            continue;

        }
        else if (input % 1 == 0 && input >= 1){
            input -= 1;
            um += 1;

        }

    }
    printf("Foram necessarias as seguintes notas:\n");
    printf("R$ 50: %i notas\n", cinq);
    printf("R$ 10: %i notas\n", dez);
    printf("R$ 5: %i notas\n", cinc);
    printf("R$ 1: %i notas\n", um);

return 0;
}
