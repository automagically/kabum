from .db import db

class Fabricante(db.Model):
    codigo = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    img = db.Column(db.String)

    def __repr__(self):
        return f"<Fabricante {self.codigo} {self.nome}>"
