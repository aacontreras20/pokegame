from urllib.request import Request, urlopen
import json, random

SUITS = ["H", "S", "C", "D"]
VALS = ["A"] + list(range(2,10)) + ["0", "J", "Q", "K"]

DEX = {
    "fire": ["Fennekin", "Vulpix", "Charizard", "Moltres"],
    "water": ["Squirtle", "Psyduck", "Blastoise", "Kyogre"],
    "grass": ["Snivy", "Turtwig", "Venusaur", "Virizion"],
    "electric": ["Mareep", "Pikachu", "Luxray", "Zapdos"],
    "psychic": ["Abra", "Espurr", "Mew", "Mewtwo"],
    "ghost": ["Gastly", "Duskull", "Gengar", "Giratina-altered"],
    "dark": ["Umbreon", "Zorua", "Houndoom", "Darkrai"],
    "steel": ["Cufant", "Meltan", "Aggron", "Jirachi"],
    "dragon": ["Dratini", "Goomy", "Salamence", "Rayquaza"],
    "fairy": ["Togepi", "Clefairy", "Sylveon", "Zacian-crowned"],
    "flying": ["Noibat", "Noivern", "Corviknight", "Tornadus-incarnate"],
    "fighting": ["Mankey", "Mienfoo", "Urshifu-single-strike", "Marshadow"],
    "ice": ["Snorunt", "Bergmite", "Beartic", "Articuno"]
}

TYPECOLORS = {
    "fire": "#F08030",
    "water": "#6890F0",
    "grass": "#78C850",
    "electric": "#F8D030",
    "psychic": "#F85888",
    "ghost": "#705898",
    "dark": "#705848",
    "steel": "#B8B8D0",
    "dragon": "#7038F8",
    "fairy": "#EE99AC",
    "flying": "#A890F0",
    "fighting": "#C03028",
    "ice": "#98D8D8",
    "poison": "#A040A0",
    "rock": "#B8A038"
}

PERMA_MOVEDICT = {
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
        types = {}
        temp = []
        for type in self.mondict["types"]:
            temp += [type["type"]["name"], type["type"]["url"]]
        movetype = temp[0]
        for i in range(0, len(temp), 2):
            types[temp[i]] = temp[i+1]
        return types, movetype

    def get_move(self, movetype):
        move = random.randint(0,len(self.movedict[movetype])-1)
        return self.movedict[movetype].pop(move)
    
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

        self.number = grabber.get_number()
        self.deckname = str(val) + suit

    def __repr__(self):
        return self.name