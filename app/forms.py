from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from models import Usuario #colocar app.models?
from app import db


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

    usuario = StringField('Nome: ', validators=[Length(min=3, max=20), DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    senha = PasswordField('Senha: ', validators=[Length(min=3, max=20), DataRequired()])
    senha2 = PasswordField('Confirmação de senha: ', validators=[EqualTo('senha1'), DataRequired()])
    cep = IntegerField('Cep: ', validators=[Length(min=8, max=8), DataRequired()])

    def validate_email(self, email):
        if Usuario.query.filter_by(email=email.data).first():
            return ValidationError('Usuário já cadastrado com esse email')
    def SalvaUser(self):
        salvar = Usuario(
            usuario = self.nome.data,
            email = self.email.data,
            senha = self.senha.data,
            cep = self.cep.data
        )
        db.session.add(salvar)
        db.session.commit()