#include <stdio.h>
#include <locale.h>
int main(){
    setlocale(LC_ALL, "Portuguese");

    int mat[3][3]; //linha / coluna

    mat[0][0] = '1';
    mat[0][1] = 2;
    mat[0][2] = 3;

    mat[1][0] = 4;
    mat[1][1] = 5;
    mat[1][2] = 6;

    mat[2][0] = 7;
    mat[2][1] = 8;
    mat[2][2] = 9;


    int l,c;
    for(l=0; l<3; l++){
        for(c=0; c<3; c++){
            printf(" %c ", mat[l][c]);
        }
        printf("\n");
    }
}
