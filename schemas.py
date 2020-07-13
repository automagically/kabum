import logging

from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy.fields import Nested, RelatedList

import models

ma = Marshmallow()

class FabricanteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Fabricante

class MenusSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Menu

class FotoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Foto
        exclude = ('codigo_produto',)

class FotoSerializer(Nested):
    def serialize(self, attr, obj, accessor=None):
        return [i.url for i in obj.fotos]

class ProdutoFamiliaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.ProdutoFamilia

class FamiliaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Familia
        include_relationsships = True

    produtos = Nested(ProdutoFamiliaSchema, many = True)

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Produto
        include_relationships = True
        load_instance = True
    fabricante = Nested(FabricanteSchema)
    menus = Nested(MenusSchema, many = True)
    fotos = FotoSerializer(FotoSchema, many = True)
    familia = Nested(FamiliaSchema)
