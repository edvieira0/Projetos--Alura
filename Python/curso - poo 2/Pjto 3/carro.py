from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def __str__(self):
        return f'O carro {self._modelo} da {self._marca} na cor {self.cor}'

    def alguma_coisa(self):
        pass