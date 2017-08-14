from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class CompareForm(Form):
    string1 = StringField('string1', validators=[DataRequired()])
    string2 = StringField('string2', validators=[DataRequired()])
    metric = SelectField('metric', choices=[ \
        ('Levenshtein','Levenshtein Distance'), \
        ('Jaccard','Jaccard Distance'), \
        ('Sorensen','Sorensen Distance')])

