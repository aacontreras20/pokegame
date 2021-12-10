from urllib import request
import json

SUITS = ["H", "S", "C", "D"]
VALS = ["A"] + list(range(2,11)) + ["J", "Q", "K"]

class ApiURLopener(request.FancyURLopener):
    version = "Mozilla/5.0"

class Grabber:
    def __init__(self, url, name):
        self.opener = ApiURLopener()
        with self.opener.open("https://pokeapi.co/api/v2/pokemon/1") as response:
            html = response.read()
        self.mondict = json.loads(html)
    
    def get_types(self):
        types = {}
        for type in self.mondict["types"]:
            types[type["type"]["name"]] = type["type"]["url"]
        return types
    
    def get_move(self):
        move_to_use = {}
        for move in self.mondict["moves"]:
            with self.opener.open(move["move"]["url"]) as move_data:
                if move_data["power"] >= 80:
                    move_to_use["name"] = move["name"]
                    move_to_use["url"] = move["move"]["url"]
                    move_to_use["power"] = move_data["power"]
        return move_to_use
    
    def get_imgsrc(self):
        return self.mondict["sprites"]["other"]["official-artwork"]["front-default"]
    
    def return_all(self):
        return self.get_types(), self.get_move(), self.get_imgsrc()

class Pokemon:
    def __init__(self, name, suit, val):
        grabber=Grabber()

        self.types, self.move, self.sprite = grabber.return_all()
        #types is a dict with {type: type url} and moves is a dict with name, power, and url

        self.name = name
        self.deckname = str(val) + suit

    def __repr__(self):
        return self.name