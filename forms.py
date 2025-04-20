from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class BugForm(FlaskForm):
    title = StringField('Bug Title', validators=[DataRequired()])
    description = TextAreaField('Bug Description', validators=[DataRequired()])
    priority = SelectField('Priority', choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    submit = SubmitField('Submit Bug')
