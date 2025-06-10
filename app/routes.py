from flask import Blueprint, render_template, redirect, url_for, request
from .models import Product, Reservation
from .forms import ReservationForm
from . import db

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    products = Product.query.all()
    forms = {p.id: ReservationForm(product_id=p.id) for p in products}
    return render_template('index.html', products=products, forms=forms)

@bp.route('/reserve', methods=['POST'])
def reserve():
    form = ReservationForm()
    if form.validate_on_submit():
        reservation = Reservation(product_id=form.product_id.data)
        db.session.add(reservation)
        db.session.commit()
    return redirect(url_for('routes.index'))
