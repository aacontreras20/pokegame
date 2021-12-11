from monclass import SUITS, VALS, Pokemon, ApiURLopener
from urllib import request
import json, random

class Actions:
    def __init__(self, user):
        self.opener = ApiURLopener()

        with self.opener.open("http://deckofcardsapi.com/api/deck/new/jokers_enabled=false") as response:
            html = response.read()
        self.deck = json.loads(html)["deck_id"]
        self.deckAction("shuffle/")

        self.POKES=[]
        self.username=user
        self.rounds=0

        for i in range(1,53):
            suit = SUITS[i%4]
            val = VALS[i%13]
            pokemon=Pokemon(str(i), suit, val)
            self.POKES.append(pokemon)
    
    def card_to_pokemon(self, code):
        for poke in self.POKES:
            if poke.deckname == code:
                return poke

    def deckAction(self, action):
        with self.opener.open(f"http://deckofcardsapi.com/api/deck/{self.deck}/{action}") as response:
            html = response.read()
        return json.loads(html)

    def drawCards(self):
        drawn_pokemon = []
        cards = self.deckAction("draw/?count=5")["cards"]
        for card in cards:
            drawn_pokemon.append(self.card_to_pokemon(card["code"]))
        
        return drawn_pokemon
    
    def getOpponenet(self):
        card = self.deckAction("draw?count=1")["cards"]
        self.opponent = self.card_to_pokemon(card["code"])
        return self.opponent

    def chooseWinner(self, selected_pokemon):
        return selected_pokemon if random.randint(10) < 5 else self.opponent

    def nextRound(self):
        if self.current_round == 10:
            self.gameover()
        else:
            self.current_round += 1
    
    def gameover(self):
        print("game ended")