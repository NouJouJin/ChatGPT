from flask import Blueprint, render_template, redirect, url_for, abort
from flask_login import login_user, logout_user, login_required, current_user
from .models import Product, Reservation, User
from .forms import ReservationForm, LoginForm, ProductForm
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


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('routes.index'))
    return render_template('login.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('routes.index'))


@bp.route('/add-product', methods=['GET', 'POST'])
@login_required
def add_product():
    if not current_user.is_admin:
        abort(403)
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, quantity=form.quantity.data)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('routes.index'))
    return render_template('add_product.html', form=form)
