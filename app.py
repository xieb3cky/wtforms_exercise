from flask import Flask, url_for,redirect, render_template, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

#step 2: make homepage listing pets
@app.route('/')
def list_pets():
    """show list of pets"""
    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)

#step 3: create add pet form
#step 4: create handler for add pet form
@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """handle form submission for adding pets"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect('/')
    else:
        return render_template("add_pet_form.html", form=form)

#step 6: add display/edit form
@app.route('/<int:pet_id>')
def show_pet(pet_id):
     pet = Pet.query.get_or_404(pet_id)
     return render_template('show_pet.html', pet=pet)

@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """handle form submission for editing pets"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        
        db.session.commit()
        flash(f'{pet.name} was updated')
        return redirect(f'/{pet_id}')
    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)