from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

db = create_engine('sqlite:///database.db')
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    name = Column("nome",String, nullable=False)
    email = Column("email",String, nullable=False)
    password = Column("senha",String)
    active=Column("ativo",Boolean)
    admin=Column("admin",Boolean, default=False)
    
    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin
class Product(Base):
    __tablename__ = 'products'

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    name = Column("nome",String, nullable=False)
    price = Column("preco",Float, nullable=False)
    description = Column("descricao",String)
    image = Column("imagem",String)
    
    def __init__(self, name, price, description, image):
        self.name = name
        self.price = price
        self.description = description
        self.image = image
class Order(Base):
    __tablename__ = 'orders'

    #status_pedidos = [("pendente", "pendente"), ("preparando", "preparando"),("entregue", "entregue"), ("cancelado", "cancelado")]
    
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    status = Column("status",String)
    usuario= Column("usuario",ForeignKey("users.id"))
    preco= Column("preco",Float)
    
    def __init__(self, usuario,status="pendente",preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco
class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    quantity = Column("quantidade",Integer, nullable=False)
    sabores = Column("sabores",String)
    tamanho = Column("tamanho",String)
    preco_unitario = Column("preco_unitario",Float)
    pedido = Column("pedido",ForeignKey("orders.id"))
    

    def __init__(self, quantity, sabores, tamanho, preco_unitario, pedido):
        self.quantity = quantity
        self.sabores = sabores
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido
