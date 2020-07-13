from .db import db
from .fabricante import Fabricante
from .familia import Familia
from .menu import Menu
from .oferta import Oferta
from .produto import Produto, Foto
from .produto_familia import ProdutoFamilia

__all__ = ['db', 'Fabricante', 'Menu', 'Oferta', 'Produto','Foto', 'ProdutoFamilia', 'Familia']
