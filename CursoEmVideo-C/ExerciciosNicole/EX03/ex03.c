#include <stdio.h>
#include <locale.h>
int main(){
    setlocale(LC_ALL, "Portuguese");
    float base, alt, per;

    printf("PERÍMETRO DO RETÂNGULO");
    printf("\nBase: ");
    scanf("%f", &base);
    printf("Altura: ");
    scanf("%f", &alt);
    per = (2*base + 2*alt);
    printf("O perímetro é %f", per);

return 0;
}
