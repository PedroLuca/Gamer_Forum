from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from formulario import CadastroForm, LoginForm

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gamerforum.db'
app.config['SECRET_KEY'] = 'dfsshfehryuakbfpefeg875368jgkdfoadydgkfbdfnlshobcl'

class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(300), nullable = False)
    usuario = db.Column(db.String(20), nullable = False, unique = True)
    senha = db.Column(db.String(12), nullable = False)
    email = db.Column(db.String(150), nullable = False, unique = True)
    estado = db.Column(db.String(50), nullable = False)
    cidade = db.Column(db.String(100), nullable = False)


    def __repr__(self): 
        return '<<<user %r>>>' % (self.usuario, self.senha, self.email, self.nome, self.estado, self.cidade)


@app.route('/')
@app.route('/index')
@app.route('/inicio')
def home():
    return render_template("./index.html")

@app.route('/doar')
def doar():
    return render_template("./_pages/doar.html")

@app.route('/cadastrar')
def cadastrar():
    form = CadastroForm()
    if form.validate_on_submit():
        user = Cadastro()
        user.usuario = form.usuario.data
        user.nome = form.nome.data
        user.email = form.email.data
        user.senha = form.senha.data
        user.confirmars = form.confirmars.data
        user.cidade = form.estado.data
        user.estado = form.estado.data
        db.session.add(user)
        db.session.commit()
    return render_template("./_pages/cadastro.html", form = form)

@app.route('/pedroluca')
def pedroluca():
    return render_template("./_pages/pedroluca.html")

@app.route('/danielvittor')
def danielvittor():
    return render_template("./_pages/danielvittor.html")

@app.route('/login')
@app.route('/logar')
@app.route('/entrar')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Login()
        user.usuario = form.usuario.data
        user.senha = form.senha.data
        db.session.add(user)
        db.session.commit()
    return render_template("./_pages/login.html", form = form)


if __name__ == '__main__':
    app.run(debug=True)