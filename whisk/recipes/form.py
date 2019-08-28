from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, Optional

class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name',
                            validators=[DataRequired()])
    description = TextAreaField('Description',
                            validators=[DataRequired()])
    meal_type = SelectField(u'Meal Type',
                            choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack'), ('Dessert', 'Dessert')], validators=[DataRequired()])
    diet_type = SelectField(u'Diet Type',
                            choices=[('Dairy-Free', 'Dairy-Free'), ('Gluten-Free', 'Gluten-Free'), ('Nut-Free', 'Peanut-Free'), ('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian')], validators=[Optional()])
    prep_time = IntegerField('Prep Time',
                            validators=[DataRequired()])
    time = IntegerField('Cooking Time',
                            validators=[DataRequired()])
    image = StringField('Recipe Image',
                            validators=[Optional()])
    ingredient_name = TextAreaField('Ingredient Name',
                            validators=[DataRequired()])
    directions = TextAreaField('Directions',
                            validators=[DataRequired()])
    submit = SubmitField('Submit Recipe')