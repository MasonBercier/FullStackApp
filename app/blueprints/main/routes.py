from flask import render_template, request
import requests
from app.blueprints.auth.forms import PokeForm
from app.blueprints.main import main


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/pokemon', methods=['GET', 'POST'])
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