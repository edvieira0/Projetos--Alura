// Para incluir bibliotecas se usa a sintaxe #include <biblioteca>
#include <stdio.h>

// Toda linha de código precisa ser fechada com ';'
// Todo código é obrigado a estar em um bloco de código no int main() e é copilado pelo o copilador GCC

// prinf imprime na tela.
// scanf coleta um input
// mascara é usada %d para números inteiros

int main(){
    printf("Bem vindo ao nosso jogo de adivinhacao\n\n");
    // Em uma definição de variáveis preciso definir o tipo antes
    
    // int numSecreto = 30;

    int chute;

    printf("Qual e o seu chute?\n");
    scanf("%d", &chute);
}