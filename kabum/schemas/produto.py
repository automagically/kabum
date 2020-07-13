from marshmallow_sqlalchemy.fields import Nested

from .common import ma
from .fabricante import FabricanteSchema
from .menu import MenusSchema
from .foto import FotoSchema
from .familia import FamiliaSchema

from .. import models

class FotoSerializer(Nested):
    def serialize(self, attr, obj, accessor=None):
        return [i.url for i in obj.fotos]

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Produto
        include_relationships = True
        load_instance = True
    fabricante = Nested(FabricanteSchema)
    menus = Nested(MenusSchema, many = True)
    fotos = FotoSerializer(FotoSchema, many = True)
    familia = Nested(FamiliaSchema)
