from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/inicio')
def incio():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('God Of War', 'Rack n slash', 'Ps2')
    jogo3 = Jogo('Battlefield 4', 'First Person Shooter', 'Pc')
    jogo4 = Jogo('Red Dead Redemption', 'Open World', 'Pc')

    lista_jogos = [jogo1, jogo2, jogo3, jogo4]

    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

app.run()


# Loop é feito no arquivo onde vai ser reproduzido a lista com a sintaxe de -> {% for i in lista %} <tr><td>{{ i }}</td></tr> e fechando em {% endfor %}