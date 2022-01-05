from urllib.request import Request, urlopen

import json, random

class Grabber:
    def __init__(self, name):
        url=f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        self.mondict = json.loads(web_byte)
        self.movedict={
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
    
    def get_name(self):
        return self.mondict["name"].title()
    
    def get_number(self):
        return self.mondict["id"]

    def get_types(self):
        types = []
        for typ in self.mondict["types"]:
            types.append(typ["type"]["name"])
        return types, types[0]

    def get_move(self, movetype):
        move = random.randint(0,len(self.movedict[movetype])-1)
        return self.movedict[movetype].pop(move)
    
    def get_imgsrc(self):
        return self.mondict["sprites"]["other"]["official-artwork"]["front_default"]

class Pokemon:
    def __init__(self, number, suit, val, power):
        grabber=Grabber(number)

        self.name = grabber.get_name()
        self.types, movetype = grabber.get_types()
        self.move = grabber.get_move(movetype)
        self.sprite = grabber.get_imgsrc()
        #types is a dict with {type: type url} and move is just a move

        self.number = grabber.get_number()
        self.deckname = str(val) + suit
        self.power = power + 1

    def __repr__(self):
        return self.name