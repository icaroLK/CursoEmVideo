#include <stdio.h>
#include <locale.h>
int main(){
    setlocale(LC_ALL, "Portuguese");
    float base, alt, per;

    printf("PER�METRO DO RET�NGULO");
    printf("\nBase: ");
    scanf("%f", &base);
    printf("Altura: ");
    scanf("%f", &alt);
    per = (2*base + 2*alt);
    printf("O per�metro � %f", per);

return 0;
}
