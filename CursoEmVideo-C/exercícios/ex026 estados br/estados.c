#include <stdio.h>
#include <locale.h>
#include <string.h>
void main(){
    setlocale(LC_ALL, "Portuguese");
    printf("Em que estado do Brasil você nasceu? ");
    char est[30];
    gets(est);
    if(strcmp(est,"SP")==0) {
        printf("Quem nasceu em %s é Paulista", est);
    }
    if(strcmp(est,"PR")==0) {
        printf("Quem nasceu em %s é Paranaense", est);
    }

}
