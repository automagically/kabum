from marshmallow_sqlalchemy.fields import Nested

from .. import models
from .common import ma
from .produto_familia import ProdutoFamiliaSchema

class FamiliaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Familia
        include_relationsships = True

    produtos = Nested(ProdutoFamiliaSchema, many = True)
