from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email("Wrong email")])
    psw = PasswordField("Password", validators=[DataRequired(), Length(min=4, max=100, message="Bad password")])
    remember = BooleanField("Remember me", default=False)
    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[Length(min=4, max=100, message="Name to short")])
    email = StringField("Email", validators=[Email("Not correct format")])
    psw = PasswordField("Password", validators=[DataRequired(), Length(min=4, max=100, message="Too short")])
    psw2 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('psw', message="Password don't match")])
    submit = SubmitField("Submit")
