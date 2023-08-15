#include <stdio.h>
#include <locale.h>
#include <math.h>




int main(){
    setlocale(LC_ALL, "Portuguese");

    float freq, XM, XMxfreq, XMquadr, XMquadxfreq;
    float freqFIM = 0, XMxfreqFIM = 0, XMquadxfreqFIM = 0;




    int medias[3][3] ={
    {25,29,880232},
    {30,34,836377},
    {35,39,787370}

    };




    for(int vez = 0; vez < 3; vez++){

    printf("media: %i", (medias[vez][0] + medias[vez][1])/2);

    };


printf("\nFI: %i", freqFIM);

printf("\nXMxFREQ: %i", XMxfreqFIM);

printf("\nXM² * FI: %i", XMquadxfreqFIM);






return 0;
}
