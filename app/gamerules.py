from monclass import SUITS, VALS, Pokemon, DEX, TYPECOLORS, PERMA_MOVEDICT
from urllib.request import Request, urlopen
import json, random

class Actions:
    def __init__(self, user): 
        self.typecolors = TYPECOLORS
        self.allmoves = PERMA_MOVEDICT

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
        self.opponent = self.getOpponent()
    
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
        winner = selected_pokemon
        loser = selected_pokemon if winner is self.opponent else self.opponent
        return winner, loser

    def nextRoundExists(self, winner):
        """
        PUBLIC; moves current round forward by 1; return type: none
        """
        if self.rounds == 9 or winner is self.opponent:
            return False
        else:
            self.rounds += 1
            self.hand = self.drawCards()
            self.opponent = self.getOpponent()
            return True
    
    def end_game(self):
        del self