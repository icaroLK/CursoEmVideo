#include <stdio.h>

int main(int argc, char *argv[]){
    if(argc > 1){
        printf("Foram inseridos %d argumentos: ", argc);
        for(int i=0; i<argc; i++){
            printf("\n%s", argv[i]);
        }
    } else {
        printf("Não foram inseridos argumentos");
    }









printf("\n\n\n");
return 0;
}
