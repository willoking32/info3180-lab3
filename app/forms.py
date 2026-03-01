from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField('Name',validators=[InputRequired()])
    email = StringField('E-mail',validators=[InputRequired()])
    subject = StringField('Subject',validators=[InputRequired()])
    message = StringField('Message',validators=[InputRequired()])