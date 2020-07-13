from .db import db

class Menu(db.Model):
    codigo = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    amigavel = db.Column(db.String)
    nome_url = db.Column(db.String)

    def __repr__(self):
        return f"<Menu {self.codigo} {self.nome}>"
