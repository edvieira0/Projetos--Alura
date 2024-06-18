from models.restaurant import Restaurante

restaurante_praca = Restaurante('praça', 'brasileira')
restaurante_beto = Restaurante('beto food', 'mexicana')
restaurante_irmaos = Restaurante('two brothers', 'japonesa')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()