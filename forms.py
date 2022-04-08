from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

#Step 5: Add Validation
class AddPetForm(FlaskForm):
    """form for adding pets"""
    name = StringField("Pet Name", 
        validators=[InputRequired()],)

    species = SelectField(
        "Species",
        #the species should be either “cat”, “dog”, or “porcupine”
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )

    photo_url = StringField("Photo URL",
        validators=[Optional(), URL()],) #photo URL must be URL but optional

    age =  IntegerField(
        "Age",
        #the age should be between 0 and 30, if provided
        validators=[Optional(), NumberRange(min=0, max=30)],
    )
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=20)],
    )


#Step 6: Edit pet form

class EditPetForm(FlaskForm):
    """form for editing existing pet"""
    photo_url = StringField("Photo URL",
                validators=[Optional(), URL()],
                )
    age =  IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)],
    )
    notes = TextAreaField('Comments',
                validators=[Optional(), Length(min=10)],
                )
    available = BooleanField("Available?")