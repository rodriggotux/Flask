from flask import Flask, redirect, url_for, request, abort

app = Flask(__name__, static_folder='static') #para da o caminho dos arquivos como html, css e js

# posso usar o @pp.get e @app.route
@app.route('/')
def home():
    return f'<h1>Bem-Vindo</h1>'

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
   # else:
    #    return redirect(url_for('guest', guest = guest))


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
# como sendo id http://127.0.0.1:5000/usuarios?name=rodrigo&idade=29
@app.route('/usuarios', methods=['POST', 'GET'])
def usuarios():
    print(request.method, request.args)
    
    
#redirecionamento de erros
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == int(123):
            return redirect(url_for('pagina_admin'), code=302)
        else:
            # tenho que importar o abort
            abort(401)
    else:
        abort(403)#mostrando algum statos, como 404 depois procurar lista de status


@app.route('/paginaadmin')
def paginaadmin():
    return f'Pagina de administrador'

#debug quando estamos em modo de desenvolvimento, ele vai mostrar os erros
if __name__ == '__main__':
    app.run(debug = True)
