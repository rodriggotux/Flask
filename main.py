from flask import Flask, redirect, url_for

app = Flask(__name__, static_folder='static') #para da o caminho dos arquivos como html, css e js

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


# Arquivos estaticos


#debug quando estamos em modo de desenvolvimento, ele vai mostrar os erros
# if __name__ == '__main__':
 #   app.run(debug=True, port="8080")
