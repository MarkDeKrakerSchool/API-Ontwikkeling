from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class KentekenForm(FlaskForm):
    kenteken = StringField('Kenteken', validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField('Zoek resultaten')

# import pandas as pd
# from sodapy import Socrata
#
# client = Socrata("opendata.rdw.nl", None)
# kenteken = str(input("Wat is je kenteken?         "))
# results = client.get("m9d7-ebf2", "?kenteken=" + kenteken)
# results_df = pd.DataFrame.from_records(results)
# print(results)
#
#
#
