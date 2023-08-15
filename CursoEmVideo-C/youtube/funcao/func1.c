#include <stdio.h>
#include <locale.h>
#include <math.h>
int main(){
    setlocale(LC_ALL, "Portuguese");
    titulo("contas");

    int v1, v2, res;
    v1 = 3;
    v2 = 9;

    res = mult(v1, v2);
    printf("\nResultado: %i", res);



printf("\n\n");
return 0;
}

void titulo(msg){
    printf("------------------------\n");
    printf("---------%s---------", msg);
    printf("\n------------------------");

}

int mult(int n1, int n2){
    int res;
    res = n1 * n2;
    return (res);


}
