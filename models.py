from pyasn1.compat import integer
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

# ao importar o create_engine de dentro do Sqlalchemy eu consigo criar um banco de dados

db= create_engine('sqlite:///banco.db')

base= declarative_base()

#TABELA

class Usuario(base):

    __tablename__ = 'cliente'
    id= Column('id',Integer,primary_key=True,autoincrement=True)
    nome= Column('nome',String)
    email= Column('email',String,nullable=False)
    senha= Column('senha',String)
    ativo= Column('ativo',Boolean)
    admin= Column('admin',Boolean, default=False)

    def __init__(self,nome,email,senha,ativo=True,admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Pedidos(base):

    __tablename__ = 'pedidos'

    statusPedido = (
    ('pendente','Pendente'),
    ('Preparando','Preparando'),
    ('Pronto','Saiu para entrega'),
    ('Cancelado','Cancelado')
    )

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    status = Column('status',ChoiceType(statusPedido),default=ChoiceType.Pendente )
    usuario= Column('usuario',ForeignKey('usuarios.id'), nullable=False)
    preco= Column('preco', float, nullable=False)



    def __init__(self,usuario,preco,status,admin=False ):
        self.usuario = usuario
        self.preco = preco
        self.status = status



class ITemPedido(base):
        __tablename__ = 'itensPedidos'
        id= Column('id', Integer, primary_key=True, autoincrement=True)
        quantidade=Column('quantidade',Integer)
        sabor= Column('sabor',String)
        tamanho= Column('tamanho',Integer)
        precoUnit=Column("precoUnit",Float)
        pedido=Column('pedido',ForeignKey('pedidos.id'),nullable=False)

        def __init__(self,quantidade,pedido,sabor,tamanho,precoUnit):
            self.quantidade = quantidade
            self.pedido = pedido
            self.sabor = sabor
            self.tamanho = tamanho
            self.precoUnit = precoUnit



#usuario
#pedidos
#itenspedidos
