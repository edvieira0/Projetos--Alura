from models.restaurant import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato


restaurante_praca = Restaurante('praça', 'brasileira')
restaurante_beto = Restaurante('beto food', 'mexicana')
restaurante_irmaos = Restaurante('two brothers', 'japonesa')

bebida_1 = Bebida('Coca', 5.40, 'pequena')

prato_1 = Prato('pão', 2.50, 'pão carioca')

def main():
    print(bebida_1)

if __name__ == '__main__':
    main()