from monclass import SUITS, VALS, Pokemon, DEX, TYPECOLORS
from urllib.request import Request, urlopen
import json, random

class Actions:
    def __init__(self, user): 
        self.typecolors = TYPECOLORS
        self.allmoves = {
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

        url="http://deckofcardsapi.com/api/deck/new/"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        self.deck = json.loads(web_byte)["deck_id"]
        self.deckAction("shuffle/")

        self.POKES=[]
        self.username=user
        self.rounds=0
        
        for i in range(13):
            for j in range(4):
                pokemon=Pokemon(list(DEX.values())[i][j], SUITS[j], VALS[i])
                self.POKES.append(pokemon)
        
        self.hand = self.drawCards()
    
    def card_to_pokemon(self, code):
        """
        PRIVATE
        """
        for poke in self.POKES:
            if poke.deckname == code:
                return poke

    def deckAction(self, action):
        """
        PRIVATE
        """
        url=f"http://deckofcardsapi.com/api/deck/{self.deck}/{action}"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        return json.loads(web_byte)

    def drawCards(self):
        """
        PUBLIC; returns 5 random pokemon from the deck; return type: list of Pokemon() instances
        """
        drawn_pokemon = []
        cards = self.deckAction("draw/?count=4")["cards"]
        for card in cards:
            card_id = card["code"]
            drawn_pokemon.append(self.card_to_pokemon(card_id))
        
        return drawn_pokemon
    
    def getOpponent(self):
        """
        PUBLIC; returns random pokemon from the deck (the opponent); return type: Pokemon() instance
        """
        card = self.deckAction("draw/?count=1")["cards"][0]
        self.opponent = self.card_to_pokemon(card["code"])

        return self.opponent

    def getWinner(self, selected_pokemon):
        """
        PUBLIC; returns the winning pokemon; return type: Pokemon() instance
        """
        #can replace with AI at some point
        return selected_pokemon if random.randint(1,10) < 5 else self.opponent

    def nextRoundExists(self):
        """
        PUBLIC; moves current round forward by 1; return type: none
        """
        if self.current_round == 10:
            self.gameover()
            return False
        else:
            self.current_round += 1
            self.hand = self.drawCards()
            return True
    
    def gameover(self):
        """
        PUBLIC; idk; return type: none
        """
        print("game ended")

