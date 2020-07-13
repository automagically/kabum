from flask_restful import Resource

from .models import Produto as ProdutoModel
from .schemas import ProdutoSchema

class Produto(Resource):

    def get(self):
        produto_list = ProdutoModel.query.all()
        return ProdutoSchema(many = True).dump(produto_list)
        #return [i.name for i in produto_list[0].__table__.columns]
