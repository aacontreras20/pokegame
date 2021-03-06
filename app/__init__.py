from flask import Flask, app, render_template, redirect, request
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
        return render_template('pokedex.html', title = "pokedex", colors=colors, types=list(types), moves=list(moves), mons=mons, accordion=["One", "Two", "Three", "four", "five", "six", "seven", "eight", "nine", "ten", "11", "12", "13"])
    except:
        return load()
        #return render_template('error.html')

@app.route('/battle')
def battle():
    try:
        colors, types = gamerules.typecolors, gamerules.POKES
        return render_template('battle.html', title = "battle", colors=colors, types=list(types), mons=gamerules.hand, opponent = gamerules.opponent)
    except:
        return load()
        return render_template('error.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    try:
        colors, types = gamerules.typecolors, gamerules.POKES
        selected_name = request.form["selected"]

        location = gamerules.getLocation()
        for card in gamerules.hand:
            if card.name == selected_name:
                selected = card
        winner, loser = gamerules.getWinner(selected)
        text = winner.name + " used " + winner.move + "! " + loser.name + " fainted!"
        current_opponent=gamerules.opponent
        if gamerules.nextRoundExists(winner):
            result = "winmessage.png"
            return render_template('result.html', types=list(types), selected = selected, colors=colors, opponent = current_opponent, text = text, page = "battle", button_text = "Next Battle", imgsrc="", result=result, location = location)
        else:
            result = "lossmessage.png"
            if gamerules.rounds == 9:
                result = "game_complete.png"
                text = "Congrats, you won all 10 rounds! Game Over."
            gamerules.end_game()
            return render_template('result.html', types=list(types), selected = selected, colors=colors, opponent = current_opponent, text = text, page = "load", button_text="Home", imgsrc="", result=result, location = location)
    except:
        return load()
        return render_template('error.html')
        
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
