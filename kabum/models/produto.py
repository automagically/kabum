from .db import db

class Foto(db.Model):
    codigo_produto = db.Column(db.Integer, db.ForeignKey('produto.codigo'), primary_key = True)
    url = db.Column(db.String, primary_key = True)

    def __repr__(self):
        return f"<Foto {self.url}>"


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





