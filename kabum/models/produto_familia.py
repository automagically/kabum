from .db import db

class ProdutoFamilia(db.Model):
    codigo = db.Column(db.Integer, primary_key = True)
    disponibilidade = db.Column(db.Boolean)
    foto = db.Column(db.String)
    link_descricao = db.Column(db.String)
    nome = db.Column(db.String)
    preco = db.Column(db.Integer)
    preco_antigo = db.Column(db.Integer)
    preco_desconto = db.Column(db.Integer)
    preco_desconto_prime = db.Column(db.Integer)
    preco_prime = db.Column(db.Integer)
    produto_prime = db.Column(db.Boolean)

    def __repr__(self):
        return f"<ProdutoFamilia {self.codigo} {self.nome}>"
