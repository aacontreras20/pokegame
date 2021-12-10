from urllib import request
import json

SUITS = ["hearts", "spades", "clubs", "diamonds"]
VALS = ["a"] + list(range(2,11)) + ["J", "Q", "K"]

class Pokemon:
    def __init__(self, name, suit, val):
        def get_info():
            with request.urlopen(f"https://pokeapi.co/api/v2/pokemon/{name}") as response:
                html = response.read()
            dic = json.loads(html)
            print(dic)

        get_info()
        #types=[]

        #self.type1 = types[0]
        #self.type2 = types[1] if types[1] else None
        self.name = name
        self.deckname = str(val) + "-" + suit

    def get_deckname(self):
        return self.deckname

    def __repr__(self):
        return self.name

pokemon=Pokemon("bulbasaur", "blah", "blah")