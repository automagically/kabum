from .. import models
from .common import ma

class ProdutoFamiliaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.ProdutoFamilia
