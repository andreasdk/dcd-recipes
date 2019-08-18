from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
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
    description = TextAreaField('Description',
                            validators=[DataRequired()])
    meal_type = StringField('Meal Type',
                            validators=[DataRequired()])
    allergens = StringField('Recipe Category',
                            validators=[Optional()])
    prep_time = IntegerField('Prep Time',
                            validators=[DataRequired()])
    time = IntegerField('Cooking Time',
                            validators=[DataRequired()])
    image = StringField('Recipe Image',
                            validators=[DataRequired()])
    ingredient_name = TextAreaField('Ingredient Name',
                            validators=[DataRequired()])
    directions = TextAreaField('Directions',
                            validators=[DataRequired()])
    submit = SubmitField('Add Recipe')

    