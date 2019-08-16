from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional

class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name',
                            validators=[DataRequired()])
    description = StringField('Description',
                            validators=[DataRequired()])
    meal_type = SelectField('Meal Type',
                            validators=[DataRequired()])
    allergens = SelectField('Recipe Category',
                            validators=[Optional()])
    time = IntegerField('Cooking Time',
                            validators=[DataRequired()])
    image = StringField('Recipe Image',
                            validators=[DataRequired()])
    ingredient_amt = IntegerField('Ingredient Amount',
                            validators=[DataRequired()])
    unit = SelectField('Measurement Unit',
                            validators=[DataRequired()])
    ingredient_name = StringField('Ingredient Name',
                            validators=[DataRequired()])
    directions = StringField('Directions',
                            validators=[DataRequired()])
    submit = SubmitField('Add Recipe')

    