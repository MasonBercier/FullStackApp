from flask import render_template, request, flash, redirect, url_for
import requests
from app.forms import LoginForm, PokeForm, RegistrationForm
from app.models import User
from app import app
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user, logout_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        
        #query from db
        queried_user = User.query.filter_by(email=email).first()
        if queried_user and check_password_hash(queried_user.password, password):
            login_user(queried_user)
            flash(f'Successfully logged in! Welcome back, {queried_user.first_name}!', 'success')
            return redirect(url_for('home'))
        else:
            error = 'Incorrect Email/Password'
            flash(f'{error}', 'danger')
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    if current_user:
        logout_user()
        flash('You have logged out', 'success')
        return redirect(url_for('login'))


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        #grabbing our from data and storing into a dict
        new_user_data = {
            'first_name': form.first_name.data.title(),
            'last_name': form.last_name.data.title(),
            'email': form.email.data.lower(),
            'password': form.password.data
        }

        #create instance of user
        new_user = User()

        # implimenting values from our form data 
        new_user.from_dict(new_user_data)

        #save to database
        new_user.save_to_db()

        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    form = PokeForm
    if request.method == 'POST':#and form.validate_on_submit():
        #TypeError: FlaskForm.validate_on_submit() missing 1 required positional argument: 'self'
        pokemon = request.form.get('pokemon')
        print(pokemon)
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)
        poketeam = []
        if response.ok:
            pokeinfo = {}
            name = response.json()['name']
            pokeinfo['name'] = name
            ability = response.json()['abilities'][0]['ability']['name']
            pokeinfo['ability'] = ability
            base_exp = response.json()['base_experience']
            pokeinfo['base exp'] = base_exp
            sprite_url = response.json()['sprites']['front_default']
            pokeinfo['default sprite'] = sprite_url
            gif_sprite_url = response.json()['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
            pokeinfo['gif sprite'] = gif_sprite_url
            attack_stat = response.json()['stats'][1]['base_stat']
            pokeinfo['attack stat'] = attack_stat
            hp_stat = response.json()['stats'][0]['base_stat']
            pokeinfo['hp stat'] = hp_stat
            def_stat = response.json()['stats'][2]['base_stat']
            pokeinfo['defense stat'] = def_stat
            primary_type = response.json()['types'][0]['type']['name']
            pokeinfo['type'] = primary_type
        else:
            error = "This pokemon does not exist! Maybe check your spelling"
            return render_template('pokemon.html',error=error, form=form)
        poketeam.append(pokeinfo)
        return render_template('pokemon.html', pokeinfo=pokeinfo, poketeam=poketeam, form=form)
    return render_template('pokemon.html', form=form)