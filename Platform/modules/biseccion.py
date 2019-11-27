from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SubmitField, validators
from wtforms.validators import DataRequired


class Form(FlaskForm):
    functionField = StringField('Function', validators=[DataRequired()])
    aValueField = DecimalField('AValue', validators=[validators.Length(min=1, max=4)])
    bValueField = DecimalField('BValue', validators=[validators.Length(min=1, max=4)])
    iterationsField = IntegerField('Iterations', validators=[validators.Length(min=1, max=15)])
    maxDecimalsField = IntegerField('MaxDecimals', validators=[validators.Length(min=1, max=12)])
    evaluateButton = SubmitField('Evaluate')


def validate_function(f):
    try:
        eval(f)
        return True
    except:
        return False