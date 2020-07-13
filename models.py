import json

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

class Fabricante(db.Model):
    codigo = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    img = db.Column(db.String)

    def __repr__(self):
        return f"<Fabricante {self.codigo} {self.nome}>"

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

class Foto(db.Model):
    codigo_produto = db.Column(db.Integer, db.ForeignKey('produto.codigo'), primary_key = True)
    url = db.Column(db.String, primary_key = True)

    def __repr__(self):
        return f"<Foto {self.url}>"

class Menu(db.Model):
    codigo = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    amigavel = db.Column(db.String)
    nome_url = db.Column(db.String)

    def __repr__(self):
        return f"<Menu {self.codigo} {self.nome}>"

produto_menu = db.Table(
    'produto_menu',
    db.Column('codigo_produto', db.Integer, db.ForeignKey('produto.codigo'), primary_key = True),
    db.Column('codigo_menu', db.Integer, db.ForeignKey('menu.codigo'), primary_key = True)
)

class Produto(db.Model):
    """Model for products"""
    #familia = 

    codigo = db.Column(db.Integer,primary_key=True)

    codigo_oferta = db.Column(db.String, db.ForeignKey('oferta.codigo'), nullable = True)
    oferta = db.relationship('Oferta')
    codigo_familia = db.Column(db.String, db.ForeignKey('familia.nome'))
    familia = db.relationship('Familia')
    codigo_fabricante = db.Column(db.String, db.ForeignKey('fabricante.codigo'), nullable = True)
    fabricante = db.relationship('Fabricante')
    fotos = db.relationship('Foto')

    menus = db.relationship('Menu', secondary=produto_menu)
    origem = db.Column(db.Integer, nullable = True)
    origem_nome = db.Column(db.String, nullable = True)
    nome = db.Column(db.String)
    oferta_inicio = db.Column(db.Integer)
    menu = db.Column(db.String)
    disponibilidade = db.Column(db.Boolean)
    pre_venda = db.Column(db.Boolean)
    nova_descricao = db.Column(db.String)
    preco = db.Column(db.Integer)
    # ask about this
    brinde = db.Column(db.Integer, db.ForeignKey('produto.codigo'), nullable=True)
    preco_prime = db.Column(db.Integer)
    preco_desconto = db.Column(db.Integer)
    preco_desconto_prime = db.Column(db.Integer)
    preco_antigo = db.Column(db.Integer)
    economize_prime = db.Column(db.Integer)
    avaliacao_numero = db.Column(db.Integer)
    avaliacao_nota = db.Column(db.Integer)
    desconto = db.Column(db.Integer)
    dimensao_peso = db.Column(db.Integer)
    produto_especie = db.Column(db.Integer)
    flag_blackfriday = db.Column(db.Integer)
    tem_frete_gratis = db.Column(db.Boolean)
    frete_gratis_somente_prime = db.Column(db.Boolean)
    is_openbox = db.Column(db.Boolean)
    sucesso = db.Column(db.Boolean)
    descricao = db.Column(db.String)
    tag_title = db.Column(db.String)
    tag_description = db.Column(db.String)
    produto_html = db.Column(db.String)
    peso = db.Column(db.String)
    garantia = db.Column(db.String)
    codigo_anatel = db.Column(db.String)
    link_descricao = db.Column(db.String)

    def __repr__(self):
        return f"<Produto {self.codigo} {self.nome}>"





