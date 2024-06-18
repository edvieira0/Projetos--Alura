from models.restaurant import Restaurante

restaurante_praca = Restaurante('praça', 'brasileira')
restaurante_beto = Restaurante('beto food', 'mexicana')
restaurante_irmaos = Restaurante('two brothers', 'japonesa')

restaurante_praca.receber_avaliacao('Eduardo', 10)
restaurante_praca.receber_avaliacao('Fulano', 5)
restaurante_praca.receber_avaliacao('Ciclano', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()