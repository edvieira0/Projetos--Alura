class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'O veiculo da marca "{self._marca}" modelo "{self._modelo}" está {self.ligado}'
    
    @property
    def ligado(self):
        return 'Ligado' if self._ligado else 'Desligado'