from app import db

class Itens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    descricao = db.Column(db.String, nullable=False)
    qntdestoque = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    avaliacao = db.Column(db.String, nullable=False)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    senha = db.Column(db.String, nullanle=False, unique=True)
    senha2 = db.Column(db.String, nullable=False, unique=True)
    celestianus = db.Column(db.Integer, nullable=False, default=0)
    "adm = db.Column(db.String, nullable=True)"
    cep = db.Column(db.String, nullable=False)
    '''pagamento = db.Column(db.String, nullable=False)
    
    CARRINHO TEM QUE TER FOREIGN KEY LIGADA AOS PRODUTOS
    carrinho = db.Column()'''

'''class Avialiações(db.Model):'''
    
class endereco(db.Model):
    id_endereco = db.Column(db.String, nullable=False)
    cep = db.Column(db.String, nullable=False)


'''class pagamento():'''
    