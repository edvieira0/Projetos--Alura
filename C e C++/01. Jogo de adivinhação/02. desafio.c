#include <stdio.h>

int main() {
	int x;
	int y;


	printf("Digite o valor da variavel x: ");
	scanf("%d", &x);

	printf("Digite o valor da variavel y: ");
	scanf("%d", &y);

    int multi = y * x;
    
    printf("O valor da multiplicacao e de %d", multi);
}