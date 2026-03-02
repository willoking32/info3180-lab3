from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField('Name (Required)',validators=[InputRequired()])
    email = StringField('E-mail (Required)',validators=[InputRequired()])
    subject = StringField('Subject (Required)',validators=[InputRequired()])
    message = StringField('Message (Required)',validators=[InputRequired()])