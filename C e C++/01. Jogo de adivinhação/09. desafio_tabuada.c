#include <stdio.h>
#include <stdlib.h>

int main(){
    int multiplicador;
    int multiplicando;
    int conta;

    printf("Digite o numero para ver a tabuada dele.\n");
    scanf("%d", &multiplicador);

    for(int i = 0; i <= 9; i++){
        multiplicando = i + 1;
        conta = multiplicando * multiplicador;

        printf("%d x %d = %d\n", multiplicando, multiplicador, conta);
    }
}