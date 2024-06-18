#include <stdio.h>

int main() {

    printf("******************************************\n");
    printf("* Bem vindo ao nosso jogo de adivinhacao *\n");
    printf("******************************************\n");

    int numeroSecreto = 10;

    int chute;

    printf("Qual e o seu chute? ");
    scanf("%d", &chute);
    printf("Seu chute foi de %d\n\n", chute);

    if (chute == numeroSecreto) {
        printf("Seu numero esta correto.");
    }
    else {
        if (chute > numeroSecreto) {
            printf("O numero escolhido e maior que o numero secreto.");
        }
        else {
            printf("O numero escolhido e menor que o numero secreto.");
        }
    }

}