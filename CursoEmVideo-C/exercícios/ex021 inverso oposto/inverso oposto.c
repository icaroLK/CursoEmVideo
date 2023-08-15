#include <stdio.h>
#include <locale.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    float res, num;
    printf("Insira um número: ");
    fflush(stdin);
    scanf("%f", &num);
    if (num>0){
        res = (float)1/num;
        printf("O inverso de %.0f é igual a %.4f\n\n", num, res);
    }else{
        res = num * (-1);
        printf("O oposto de %.0f é igual a %.0f\n\n",num, res);
    }


}
