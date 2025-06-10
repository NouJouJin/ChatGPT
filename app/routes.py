from flask import Blueprint, render_template, redirect, url_for
from .models import products, reservations

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html', products=products)

@bp.route('/reserve/<int:product_id>')
def reserve(product_id):
    if product_id not in reservations:
        reservations.append(product_id)
    return redirect(url_for('routes.index'))
