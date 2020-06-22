from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class KentekenForm(FlaskForm):
    kenteken = StringField('Kenteken', validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField('Zoek resultaten')





