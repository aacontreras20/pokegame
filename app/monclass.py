from urllib import request
import json, random

SUITS = ["H", "S", "C", "D"]
VALS = ["A"] + list(range(2,11)) + ["J", "Q", "K"]

MONS = list(range(1,53))

movedict = {
    "fire": ["Blast Burn", "Blue Flare", "Flamethrower", "V-Create"],
    "water": ["Aqua Jet", "Surging Strikes", "Hydro Pump", "Liquidation"],
    "grass": ["Solar Beam", "Frenzy Plant", "Leaf Blade", "Vine Whip"],
    "electric": ["Zap Cannon", "Thunderbolt", "Volt Tackle", "Fusion Bolt"],
    "psychic": ["Extrasensory", "Psystrike", "Psycho Cut", "Psybeam"],
    "ghost": ["Shadow Ball", "Hex", "Night Shade", "Moongeist Beam"],
    "dark": ["Sucker Punch", "Night Slash", "Foul Play", "Darkest Lariat"],
    "steel": ["Meteor Mash", "Metal Claw", "Steel Roller", "Iron Tail"],
    "dragon": ["Outrage", "Draco Meteor", "Dragon Rush", "Spacial Rend"],
    "fairy": ["Dazzling Gleam", "Fleur Cannon", "Moonblast", "Play Rough"],
    "flying": ["Oblivion Wing", "Aerial Ace", "Air Cutter", "Brave Bird"],
    "fighting": ["Brick Break", "Close Combat", "Cross Chop", "Meteor Assault"],
    "ice": ["Freeze-Dry", "Glaciate", "Ice Hammer", "Ice Beam"]
}

class ApiURLopener(request.FancyURLopener):
    version = "Mozilla/5.0"

class Grabber:
    def __init__(self, name):
        opener = ApiURLopener()
        with opener.open(f"https://pokeapi.co/api/v2/pokemon/{name}") as response:
            html = response.read()
        self.mondict = json.loads(html)
    
    def get_name(self):
        return self.mondict["name"].title()

    def get_types(self):
        types = {}
        temp = []
        for type in self.mondict["types"]:
            temp += [type["type"]["name"], type["type"]["url"]]
        movetype = temp[0]
        for i in range(0, len(temp), 2):
            types[temp[i]] = temp[i+1]
        return types, movetype

    def get_move(self, movetype):
        move = random.randint(0,len(movedict[movetype])-1)
        return movedict[movetype].pop(move)
    
    def get_imgsrc(self):
        return self.mondict["sprites"]["other"]["official-artwork"]["front_default"]

class Pokemon:
    def __init__(self, number, suit, val):
        grabber=Grabber(number)

        self.name = grabber.get_name()
        self.types, movetype = grabber.get_types()
        self.move = grabber.get_move(movetype)
        self.sprite = grabber.get_imgsrc()
        #types is a dict with {type: type url} and move is just a move

        self.number = number
        self.deckname = str(val) + suit

    def __repr__(self):
        return self.name