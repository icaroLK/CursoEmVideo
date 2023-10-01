#include <stdio.h>
#include <math.h>

float arredonda(float BUCETA);



int main(){
    float num;
    float arred;
    printf("Insira um valor: ");
    scanf("%f", &num);


    arred = arredonda(num);
    printf("ARRENDONDADO BOSTA: %.0f\n", arred);



return 0;
}

float arredonda(float BUCETA){
    return round(BUCETA);
}
