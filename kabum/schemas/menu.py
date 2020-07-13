from .. import models
from .common import ma

class MenusSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Menu
