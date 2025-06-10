from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired, ValidationError

from .models import Product, Reservation

class ReservationForm(FlaskForm):
    """Form to reserve a product."""

    product_id = HiddenField(validators=[DataRequired()])
    submit = SubmitField('Reserve')

    def validate_product_id(self, field):
        product = Product.query.get(field.data)
        if not product:
            raise ValidationError('Product not found.')
        # Count existing reservations
        count = Reservation.query.filter_by(product_id=field.data).count()
        if count >= product.quantity:
            raise ValidationError('No more stock available.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Save')
