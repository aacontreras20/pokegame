from urllib import request
import json, random

SUITS = ["H", "S", "C", "D"]
VALS = ["A"] + list(range(2,11)) + ["J", "Q", "K"]

MONS = [3, 6, 9, ]
#Venusaur, Charizard, Blastoise, 

movedict = {
    "Fire": [" Burn", "Blue Flare", "Flamethrower", "V-Create"],
    "Water": ["", "", "", ""],
    "Grass": ["", "", "", ""],
    "Electric": ["", "", "", ""],
    "Psychic": ["", "", "", ""],
    "Ghost": ["", "", "", ""],
    "Dark": ["", "", "", ""],
    "Steel": ["", "", "", ""],
    "Dragon": ["", "", "", ""],
    "Fairy": ["", "", "", ""],
    "Flying": ["", "", "", ""],
    "Fighting": ["", "", "", ""],
    "Bug": ["", "", "", ""],
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
        movetype = types[0]
        for i in range(0, len(temp), 2):
            types[temp[i]] = temp[i+1]
        return types, movetype

    def get_move(self):
        move = random.randint(0,3)
        return movedict[self.movetype].pop(move)
    
    def get_imgsrc(self):
        return self.mondict["sprites"]["other"]["official-artwork"]["front_default"]

class Pokemon:
    def __init__(self, number, suit, val):
        grabber=Grabber(number)

        self.name = grabber.get_name()
        self.types, self.movetype = grabber.get_types()
        self.move = grabber.get_move()
        self.sprite = grabber.get_imgsrc()
        #types is a dict with {type: type url} and moves is a dict with name, power, and url

        self.number = number
        self.deckname = str(val) + suit

    def __repr__(self):
        return self.name