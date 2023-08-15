#include <stdio.h>
#include <locale.h>
int main(){
    setlocale(LC_ALL, "Portuguese");

    int mat[3][3] = {{11,22,33}, {44,55,66}, {77,88,99}};


    int l,c;
    for(l=0; l<3; l++){
        for(c=0; c<3; c++){
            printf(" %i ", mat[l][c]);
        }
        printf("\n");
    }
}
