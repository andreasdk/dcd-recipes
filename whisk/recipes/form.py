from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Optional

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
    submit = SubmitField('Submit Recipe')