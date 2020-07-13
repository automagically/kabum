from .. import models
from .. import models
from .common import ma

class FotoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Foto
        exclude = ('codigo_produto',)
