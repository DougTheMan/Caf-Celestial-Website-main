from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField, BooleanField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from app.models import Usuario, Itens, User2
from app import db

#-----#-----#-----#-----#-----#-----#
#Cadastro e Login

class User2Form(FlaskForm):
    nome = usuario = StringField('Nome: ', validators=[DataRequired()])
    senha = PasswordField('Senha: ', validators=[Length(min=3, max=20), DataRequired()])
    btnSubmit = SubmitField('Cadastrar!')

    def save(self):
        add = User2(
            nome = self.nome.data,
            senha = self.senha.data
        )
        db.session.add(add)
        db.session.commit()
    
class CadastroForm(FlaskForm):
    usuario = StringField('Nome: ', validators=[Length(min=3, max=20), DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha: ', validators=[Length(min=3, max=20), DataRequired()])
    senha2 = PasswordField('Confirmação de senha: ', validators=[DataRequired(), EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar!')

    def validate_username(self, check_user):
        user = Usuario.query.filter_by(usuario=check_user.data).first()
        if user: 

            #flashar depois -------------------------------------------------

            raise ValidationError("Usuário já existe: Cadastre outro usuário.")
    def validate_email(self, check_email):
        email = Usuario.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Email já existe! Cadastre outro email.")

    def save(self):
        add = Usuario(
            usuario = self.usuario.data,
            email = self.email.data,
            senha = self.senha.data,    #BYCRYPTAR ESSA COISA DEPOIIS
            senha2 = self.senha.data
            #Aqui será que vai senha 2?sq
            #cep = self.cep.data  #a gente uida aqui e models 
        )
        db.session.add(add)
        db.session.commit()


    #colocar LOGIN AUQI TA NÂO SE ESQUECE

#class LoginForm(FlaskForm):

#-----#-----#-----#-----#-----#-----#

class ItensForm(FlaskForm):
    titulo = StringField("Nome do Produto: ", validators=[DataRequired()])
    descricao = StringField("Descrição: ", validators=[DataRequired()])
    qntdestoque = IntegerField("Estoque", validators=[DataRequired()])
    preco = FloatField("Preço: ", validators=[DataRequired()])
    especial = IntegerField("1 para promoção || 2 para não promoção", validators=[DataRequired()])
    btnSubmit = SubmitField('Registrar Item. REVISE!')

    def SalvaItens(self):
        add = Itens(
            titulo = self.titulo.data,
            descricao = self.descricao.data,
            qntdestoque = self.qntdestoque.data,
            preco = self.preco.data,
            especial = self.especial.data
        )
        db.session.add(add)
        db.session.commit()
        
