from models.restaurant import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
from models.cardapio.sobremesa import Sobremesa



restaurante_praca = Restaurante('praça', 'brasileira')
restaurante_beto = Restaurante('beto food', 'mexicana')
restaurante_irmaos = Restaurante('two brothers', 'japonesa')

bebida_1 = Bebida('Coca', 5.50, 'pequena')
bebida_1.aplicar_desconto()

prato_1 = Prato('Feijoada', 7.50, 'Feijão preto com linguiça')
prato_1.aplicar_desconto()

sobremesa_1 = Sobremesa(nome='Sorvete', preco=24, descricao='Cremoso com baunilha', tipo='gelado', tamanho='ultra blaster')

restaurante_praca.adicionar_cardapio(bebida_1)
restaurante_praca.adicionar_cardapio(prato_1)

restaurante_praca.adicionar_cardapio(sobremesa_1)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()