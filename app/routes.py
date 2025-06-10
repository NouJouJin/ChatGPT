from flask import Blueprint, render_template, redirect, url_for
from .models import Product, Reservation
from . import db

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@bp.route('/reserve/<int:product_id>')
def reserve(product_id):
    if not Reservation.query.filter_by(product_id=product_id).first():
        reservation = Reservation(product_id=product_id)
        db.session.add(reservation)
        db.session.commit()
    return redirect(url_for('routes.index'))
