from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokeForm(FlaskForm):
    pokename = StringField('pokename', validators=[DataRequired()])
    submit_btn = SubmitField('Search!')
