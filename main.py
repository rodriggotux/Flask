from flask import Flask, redirect, url_for, request, abort, render_template,
make_response

#aqui para arquivostaticos
app = Flask(__name__,static_folder='static') #para da o caminho dos arquivos como html, css e js

#aqui para templates,ao como componentes que iraervir de base ee repetir
app = Flask(__name__,template_folder='templates') #para da o caminho dos arquivos como html, css e js

# posso usar o @pp.get e @app.route
@app.route('/')
def home():
    return render_template('index.html')

#aqui eu vou passar um name via parametro de url, uma url dinamica
@app.route('/clientes/<name>')
def clientes(name):
    return f'<h4>Ola {name}</h4>'

#redirecionamento de url, temos que impotar redirect, url_for
@app.route('/admin')
def admin():
    return f'Logado como administrador'

@app.route('/guest/<guest>')
def guest(guest):
    return f'ola {guest}' % guest

@app.route('/user/<nome>')
def user(nome):
    if nome == 'admin': #redirecionando para a rota de admin la em cima
       return  redirect(url_for('admin'))
    else:
       return redirect(url_for('guest', guest = guest))


# Verbos da HTTP podemos importar o
# request, para facilitar
@app.route('/add', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        return f'funcinou %s' %request.form['name'] #name e o nome do campo no html
    else:
        return f'Falha no Engando'


# Objetos de requisição
# os args, quer dize que posso passa via url
# comoendo id http://127.0.0.1:5000/usuarios?name=rodrigo&idade=29
@app.route('/usuarios', methods=['POST', 'GET'])
def usuarios():
    print(request.method, request.args)


#redirecionamento de erros [FALTA EU ARRUMAR ESSE BLOCO DE CODIGO]
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['nome'] == 'user' and request.form['senha'] == '123':
            return redirect(url_for('administrador'), code=302)
        else:
            abort(401)
    else:
        abort(403)

@app.route('/administrador')
def administrador():
    return f'Pagina do administrador'

#debug quando estamos em modo de desenvolvimento, ele vai mostrar os erros
if __name__ == '__main__':
    app.run(debug = True)

# renderizando templates djinja, pra colocar variaveis dentro do html impotar
# render_template
@app.route('/index')
def index():
    x = 50
    y = 10
    res = X + y
    return render_template('index.html')

#enviar dados para o template
@app.route('/dados')
def dados():
    return render_template(index.html)

#cookies
@app.route('/cookeis')
def cookeis():
    return render_template('main.html')

#setcookei
@app.route('/setcookei')
defetcookei():
    resp = make_response(render_template('main.html'))
    if request.method == 'POST':
        dados = request.for['c']
#tem que importa o make_response
        resp =et_cookie('nomedocookei', dados)
    return resp

#getcookei
@aap.route('/getcookei')
def getcookei():
    return ''
