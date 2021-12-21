from flask import Flask, app, render_template, redirect
from gamerules import Actions

app = Flask(__name__)
@app.route('/')
def load():
    try:
        return render_template('loading_page.html')
    except:
        return render_template('error.html')

@app.route('/temphome')
def temphome():
    try:
        global gamerules
        gamerules = Actions("Jeff")
        return render_template('home.html', title = "home")
    except:
        return render_template('error.html')

@app.route('/home')
def home():
    try:
        return render_template('home.html', title="home")
    except:
        return render_template('error.html')
    
@app.route('/about')
def about():
    try:
        return render_template('about.html', title = "about")
    except:
        return render_template('error.html')

@app.route('/pokedex')
def pokedex():
    try:
        colors, mons, types, moves = gamerules.typecolors, gamerules.POKES, gamerules.allmoves.keys(), gamerules.allmoves.values()
        return render_template('pokedex.html', colors=colors, title = "pokedex", types=list(types), moves=list(moves), mons=mons, accordion=["One", "Two", "Three", "four", "five", "six", "seven", "eight", "nine", "ten", "11", "12", "13"])
    except:
        return load()
        #return render_template('error.html')

@app.route('/battle')
def battle():
    try:
        images = []
        hand = gamerules.drawCards()
        for card in hand:
            if card is not None:
                images.append(card.sprite)
        return render_template('battle.html', title = "battle", images = images)
    except:
        return load()
        #return render_template('error.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
