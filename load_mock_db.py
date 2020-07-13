from datetime import datetime

from flask import Flask

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mock.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)

db.create_all()
for filename in ['1.json','2.json','3.json']:
    with open(filename, 'r') as f:
        raw = json.load(f)

        oferta = raw['oferta']
        if oferta:
            oferta['data_inicio'] = datetime.fromtimestamp(oferta['data_inicio'])
            oferta['data_fim'] = datetime.fromtimestamp(oferta['data_fim'])
            oferta = Oferta(**oferta)
            db.session.add(oferta)
            raw['oferta'] = oferta
            print(oferta)

        fabricante = Fabricante(**raw['fabricante'])
        raw['fabricante'] = fabricante
        print(fabricante)
        db.session.add(fabricante)

        # guarda fotos para mais tarde 
        fotos = []
        for foto in raw['fotos']:
            foto = Foto(url=foto)
            fotos.append(foto)
            #db.session.add(foto)
            print(foto)
        raw['fotos'] = fotos

        menus = []
        for raw_menu in raw['menus']:
            menu = Menu(**raw_menu)
            menus.append(menu)
            db.session.merge(menu)
            print(menu)
        raw['menus'] = menus

        familia = raw['familia']
        prods = []
        for i in familia['produtos']:
            produto_familia = ProdutoFamilia(**i)
            prods.append(produto_familia)
            db.session.merge(produto_familia)
            print(produto_familia)
        familia['produtos'] = prods
        familia = Familia(**familia)
        raw['familia'] = familia
        print(familia)


        produto = Produto(**raw)
        db.session.merge(produto)
        print(produto)


db.session.commit()

