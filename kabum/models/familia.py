from .db import db

familia_produto = db.Table(
    'familia_produto',
    db.Column('codigo_produto', db.Integer, db.ForeignKey('produto_familia.codigo'), primary_key = True),
    db.Column('nome_familia', db.String, db.ForeignKey('familia.nome'), primary_key = True)
)

class Familia(db.Model):
    codigo = db.Column(db.Integer)
    nome = db.Column(db.String, primary_key = True)
    titulo = db.Column(db.String)
    produtos = db.relationship('ProdutoFamilia', secondary=familia_produto)

    def __repr__(self):
        return f"<Familia {self.nome}>"
