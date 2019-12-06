from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CadastroForm(FlaskForm):
    usuario = StringField("Usuário", validators=[DataRequired])
    nome = StringField("Nome", validators=[DataRequired])
    senha = StringField("Senha", validators=[DataRequired])
    confirmars = StringField("Confirmar Senha", validators=[DataRequired])
    email = StringField("E-mail", validators=[DataRequired])
    cidade = StringField("Cidade", validators=[DataRequired])
    estado = StringField("Estado", validators=[DataRequired])
    botao = SubmitField("Enviar")

class LoginForm(FlaskForm):
    usuario = StringField("Usuário", validators=[DataRequired])
    senha = StringField("Senha", validators=[DataRequired])
    botao = SubmitField("Enviar")