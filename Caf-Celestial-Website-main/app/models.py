from app import db

class Itens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    descricao = db.Column(db.String, nullable=False)
    qntdestoque = db.Column(db.Integer, nullable=True, default=0)
    preco = db.Column(db.Float, nullable=False)
    avaliacao = db.Column(db.Float, nullable=True, default=0.0)
    especial = db.Column(db.Integer, nullable=True, default=2)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    senha = db.Column(db.String, nullable=False)
    senha2 = db.Column(db.String, nullable=False)
    celestianus = db.Column(db.Integer, nullable=True, default=0)
    adm = db.Column(db.Boolean, nullable=True, default=0)
    #cep = db.Column(db.Integer, nullable=False)
    '''pagamento = db.Column(db.String, nullable=False)
    
    CARRINHO TEM QUE TER FOREIGN KEY LIGADA AOS PRODUTOS
    carrinho = db.Column()'''

'''class Avialiações(db.Model):'''

class User2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    senha = senha = db.Column(db.String, nullable=False)


'''class pagamento():'''
    