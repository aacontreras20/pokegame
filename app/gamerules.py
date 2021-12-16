from monclass import SUITS, VALS, Pokemon, DEX
from urllib.request import Request, urlopen
import json, random

class Actions:
    def __init__(self, user):        
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
        
        print(self.POKES)
    
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
        cards = self.deckAction("draw/?count=5")["cards"]
        for card in cards:
            card_id = card["code"]
            print(card_id)
            drawn_pokemon.append(self.card_to_pokemon(card_id))
        
        return drawn_pokemon
    
    def getOpponent(self):
        """
        PUBLIC; returns random pokemon from the deck (the opponent); return type: Pokemon() instance
        """
        card = self.deckAction("draw/?count=1")["cards"]
        self.opponent = self.card_to_pokemon(card["code"])
        return self.opponent

    def getWinner(self, selected_pokemon):
        """
        PUBLIC; returns the winning pokemon; return type: Pokemon() instance
        """
        #can replace with AI at some point
        return selected_pokemon if random.randint(10) < 5 else self.opponent

    def nextRoundExists(self):
        """
        PUBLIC; moves current round forward by 1; return type: none
        """
        if self.current_round == 10:
            self.gameover()
            return False
        else:
            self.current_round += 1
            return True
    
    def gameover(self):
        """
        PUBLIC; idk; return type: none
        """
        print("game ended")

    """
    POKEMON() WRAPPER METHODS
    """

    def getTypes(self, pokemon):
        """
        PUBLIC; returns 5 random pokemon from the deck; return type: dictionary {type1: type1 name, type1 url: type1 url...etc}
        """
        return pokemon.types
    
    def getMove(self, pokemon):
        """
        PUBLIC; returns a pokemon's move; return type: dictionary {name: name of move, url: url to webpage for move}
        """
        return pokemon.move
    
    def getSprite(self, pokemon):
        """
        PUBLIC; returns a pokemon's sprite; return type: string (image url)
        """
        return pokemon.sprite
    
    def getName(self, pokemon):
        """
        PUBLIC; returns a pokemon's name; return type: string
        """
        return pokemon.name