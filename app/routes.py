from flask import render_template, request
import requests
from app.forms import LoginForm, SignupForm, PokeForm
from app import app

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        if email in app.config.get('REGISTERED_USERS') and password == app.config.get('REGISTERED_USERS').get(email).get('password'):
            return f"Login Successful! Welcome {app.config.get('REGISTERED_USERS').get(email).get('name')}"
        else:
            error = 'Incorrect Email/Password'
            return render_template('login.html', error=error, form=form)
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data.lower()
        password = form.password.data
        if email not in app.config.get('REGISTERED_USERS'):
            return f"Registration successful! Welcome!"
        else:
            error = "It looks like that email already has an account! Try logging in."
            return render_template('signup.html', error=error, form=form)
    return render_template('signup.html', form=form)


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