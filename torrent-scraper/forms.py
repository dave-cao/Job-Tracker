from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Wtf Forms
class QueryForm(FlaskForm):
    query = StringField("Search Audiobook", validators=[DataRequired()])
    submit = SubmitField("Search")
