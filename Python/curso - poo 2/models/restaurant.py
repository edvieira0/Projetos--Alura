from models.avaliacao import Avalicao
from models.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} || {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Ativo'.ljust(26)} | {'Avaliação'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {restaurante.media_avaliacao}')

    @property
    def ativo(self):
        return '✔️' if self._ativo else '❌'

    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avalicao = Avalicao(cliente, nota)
        self._avaliacao.append(avalicao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 5.0

        soma_das_notas = sum(avalicao._nota for avalicao in self._avaliacao)
        qtd_notas = len(self._avaliacao)
        media = round(soma_das_notas / qtd_notas, 1)
        return 5.0 if media >= 5.0 else media

    def adicionar_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                msg = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.descricao}'
                print(msg)
            else:
                msg = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}'
                print(msg)