from fLoginlask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import Email, DataRequired, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email()])
    psw = PasswordField("Password", validators=[DataRequired(), Length(min=4, max=100)])
    remember = BooleanField("Remember me", default=False)
    submit = SubmitField("Submit")
