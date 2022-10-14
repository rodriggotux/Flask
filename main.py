from flask import Flask
from flask import redirect, url_for

app = Flask(__name__)

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

@app.route('/usuario/<user>')
def usuario(user):
    if user == 'admin':
        return redirect(url_for('admin'))
    else:
        return f'erro no login'





























if __name__ == '__main__':
    app.run(debug=True)
