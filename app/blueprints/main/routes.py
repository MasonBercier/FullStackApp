from flask import render_template, request, flash, redirect, url_for
import requests
from .forms import PokeForm, PokeTeamForm
from . import main
from app.models import User, Caught
from flask_login import login_required, current_user


@main.route('/')
def home():
    users = User.query.all()
    print(users)
    return render_template('home.html', users=users)


@main.route('/pokemon', methods=['GET', 'POST'])
@login_required
def pokemon():
    form = PokeForm()
    if request.method == 'POST' and form.validate_on_submit():
        pokemon = form.pokename.data
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)
        if response.ok:
            if current_user.poketeam.count() < 6:
                new_team = []
                pokename = response.json()
                pokeinfo = {    
                    "name" : pokename['name'],
                    "ability": pokename['abilities'][0]['ability']['name'],
                    "base_exp": pokename['base_experience'],
                    "sprite_url": pokename['sprites']['front_default'],
                    "gif_sprite_url": pokename['sprites']['versions']['generation-v']['black-white']['animated']['front_default'],
                    "attack_stat": pokename['stats'][1]['base_stat'],
                    "hp_stat": pokename['stats'][0]['base_stat'],
                    "defense_stat": pokename['stats'][2]['base_stat'],
                    "primary_type": pokename['types'][0]['type']['name']
                }
            else:
                flash('Sorry youre team is full!')
            poke_check = current_user.poketeam.filter_by(name=pokeinfo['name']).first()

            if poke_check:
                flash('Sorry, it looks like that pokemon is already on your team!')
                return redirect(url_for('main.pokemon'))
            new_team.append(pokeinfo)

            new_pokemon = Caught()

            new_pokemon.from_dict(pokeinfo)

            new_pokemon.save_to_db()

            current_user.catch_poke(new_pokemon)

            return render_template('pokemon.html', pokeinfo=pokeinfo, new_team=new_team, form=form)

        else:
            flash("This pokemon does not exist! Maybe check your spelling", "warning")
            return redirect(url_for('main.pokemon'))
    return render_template('pokemon.html', form=form)



@main.route('/catch/<caught_name>')
@login_required
def catch_poke(caught_name):
    poke = Caught.query.get(caught_name)
    if poke:
        current_user.catch_poke(caught_name)
        return render_template('view_team.html', poke=poke)
    else:
        flash('This poke does not exist', 'danger')


# @main.route('/catch/<caught_name>', methods=['GET', 'POST'])
# @login_required
# def catch_poke(caught_name):
#     poke = Caught.query.get(caught_name)
#     poke_check = current_user.poketeam.filter_by(name=poke['name']).first()
#     if poke_check:
#         flash('Sorry, it looks like that pokemon is already on your team!')
#         return redirect(url_for('main.pokemon'))
#     if poke:
#         current_user.catch_poke()
#         return render_template('view_team.html')
#     else:
#         flash('This poke does not exist', 'danger')

@main.route('/view_team')
@login_required
def view_team():
    my_team = current_user.poketeam
    return render_template('view_team.html', my_team=my_team)


@main.route('/release_pokemon/<caught_name>')
@login_required
def release_pokemon(caught_name):
        pokemon = Caught.query.get(caught_name)
        if pokemon in Caught:
            current_user.release_pokemon()
            flash('Pokemon successfully released into the wild')
        else:
            flash('This pokemon is not in your party')

        return redirect(url_for('main.view_team'))