"""Database models for the application."""

from . import db


class Product(db.Model):
    """A farm product available for reservation."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


class Reservation(db.Model):
    """A reservation for a specific product."""

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)

    product = db.relationship(Product, backref=db.backref("reservations", lazy=True))

