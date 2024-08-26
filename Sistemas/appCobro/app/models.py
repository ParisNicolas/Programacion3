from datetime import datetime
from . import db

from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    numero_tarjeta = db.Column(db.Integer)
    vencimiento_tarjeta = db.Column(db.DataTime)
    numero_seguridad_tarjeta = db.Column(db.Integer)

    def __repr__(self):
        return f"<Usuario {self.name}>"

class Carrito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    fecha = db.Column(db.DataTime, nullable=False)

    def __repr__(self):
        return f"<Carrito {self.email}>"

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DataTime, nullable=False)
    carrito = db.Column(db.Integer, db.ForeignKey('carrito.id'))

    cantidad = db.Column(db.Integer, default=1)
    producto = db.Column(db.Integer, db.ForeignKey('producto.id'))

    def __repr__(self):
        return f"<Carrito {self.email}>"

class Producto(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    descuento = db.Column(db.Float, default=0.0)

    proveedor = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Producto {self.nombre}>"