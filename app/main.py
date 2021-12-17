from flask import Flask, app, render_template, redirect
from gamerules import Actions

gamerules = Actions("Jeff")

app = Flask(__name__) 
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = "home")
    
@app.route('/about')
def about():
    return render_template('about.html', title = "about")

@app.route('/pokedex')
def pokedex():
    colors, mons, types, moves = gamerules.typecolors, gamerules.POKES, gamerules.allmoves.keys(), gamerules.allmoves.values()
    return render_template('pokedex.html', colors=colors, title = "pokedex", types=list(types), moves=list(moves), mons=mons, accordion=["One", "Two", "Three", "four", "five", "six", "seven", "eight", "nine", "ten", "11", "12", "13"])

@app.route('/battle')
def battle():
    return render_template('battle.html', title = "battle")

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()