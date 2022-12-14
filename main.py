from flask import Flask
from flask import redirect, url_for, request, abort, render_template


# usando static_folder='caminho', para arquivos estaticos
# app = Flask(__name__, static_folder='static')

# renderizar template, template recebe variaveis no html usando {% %} ou {{  }}
app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return f'<h2>Bem Vindos(a)</h2>'

@app.route('/produtos')
def produtos():
    return f'lista de produtos'

# criando uma url dinamica, passando informacoes via parametro pela rota
# da url. https://localhost:500/nomedarota/rodrigo
@app.route('/cliente/<name>')
def cliente(name):
    return f'cliente {name}'


# redirecionamento de rota
@app.route('/admin')
def admin():
    return f'<h4> Logado como administrador </h4>'

# aqui estou fazendo o redirecionamento para a pagina de admin
@app.route('/usuario/<user>')
def usuario(user):
    if user == 'admin':
        return redirect(url_for('admin', admin = admin))
    else:
        return f'erro no login'

# METODOS
# essa rota vai ser do tipo POST
# para eu saber qual o modulo usar, tenho que importar o request
@app.route('/add', methods=['POST', 'GET'])
def adicionar():
    if request.method == 'POST':
       return f'Enviado com sucesso! %s.' % request.form['name']

"""
recebendo dados via method GET
@app.route('/dados')
def dados():
    usario = request.args.get('nomedo campo do input do html')
    reurn 'ola {usuario}'
"""
# trabalhando com erro
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['name'] == 'admin' and request.form['password'] == 'admin':
            return f'passou'
        else:
            abort(401) #erro, nao autorizado, pesquisar mais sobre erros
    else:
        abort(403)

@app.route('/home')
def inicio():
    x = 10
    y = 15
    res = x + y
    query = request.args.to_dict()
    return render_template('index.html', res = res, query = query)

# passando dados de um template paa outro
@app.route('/main')
def main():
    return render_template('nota.html')

@app.route('/calculo', methods=['POST'])
def claculo():
    total =int( request.form.to_dict().values())
    return render_template('calculo.html')


# manipulando sesion, tem que importar o session
# depois vejo no youtube











if __name__ == '__main__':
    app.run(debug=True)
