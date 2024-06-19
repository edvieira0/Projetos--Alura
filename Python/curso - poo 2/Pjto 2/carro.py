from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas
    
    def __str__(self):
        return f'O carro da marca "{self._marca}" modelo "{self._modelo}" com "{self._portas}" portas'