#include <stdio.h>
#include <locale.h>
#include <time.h>

void main(){
    setlocale(LC_ALL, "Portuguese");

    time_t t;
    time(&t);
    struct tm *data;
    data = localtime(&t);
    int d = data->tm_mday;
    int m = data->tm_mon+1;  // mes 0 = janeiro
    int y = data->tm_year+1900;   // nessa biblioteca o ano 0 é 1900

    printf("Estamos no dia %i/%i/%i", d, m, y);



}
