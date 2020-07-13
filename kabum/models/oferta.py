from .db import db

class Oferta(db.Model):
    codigo = db.Column(
        db.String,
        primary_key = True
    )
    evento_codigo = db.Column(db.Integer)
    data_inicio = db.Column(db.DateTime)
    data_fim = db.Column(db.DateTime)
    quantidade = db.Column(db.Integer)
    evento = db.Column(db.String)
    logar = db.Column(db.Integer)

    def __repr__(self):
        return f"<Oferta {self.codigo} {self.evento}>"
