from .. import models
from .common import ma

class FabricanteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Fabricante
