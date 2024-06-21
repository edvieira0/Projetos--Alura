from flask import Flask, render_template

app = Flask(__name__)

jogos = ['God of war', 'Red dead Redemption', 'Skyrim', 'Need for Speed', 'The last of us', 'Battlefield 4']

@app.route('/inicio')
def incio():
    return render_template('lista.html', titulo='Jogos', lista_jogos=jogos)

app.run()


# Loop é feito no arquivo onde vai ser reproduzido a lista com a sintaxe de -> {% for i in lista %} <tr><td>{{ i }}</td></tr> e fechando em {% endfor %}