from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from models import Usuario #colocar app.models?


class CadastroForm(FlaskForm):
    def validate_username(self, check_user):
        user = Usuario.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuário já existe: Cadastre outro usuário.")
    def validate_email(self, check_email):
        email = Usuario.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Email já existe! Cadastre outro email.")
    def validate_senha(self, check_senha):
        senha = Usuario.query.filter_by(senha=check_senha.data).first()
        if senha:
            raise ValidationError("senha ja existe! Cadastre outra senha.")

    usuario = StringField(label='Nome: ', validators=[Length(min=3, max=20), DataRequired()])
    email = StringField(label='Email: ', validators=[DataRequired()])
    senha = PasswordField(label='Senha: ', validators=[Length(min=3, max=20), DataRequired()])
    senha2 = PasswordField(label='Confirmação de senha: ', validators=[EqualTo('senha1'), DataRequired()])
    cep = IntegerField(label='Cep: ', validators=[Length(min=8, max=8), DataRequired()])

    def SalvaUser():
        salvar = {
            
        }