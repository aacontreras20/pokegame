from monclass import Pokemon 
from urllib.request import Request, urlopen
from game_vals import *
import random
import json

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
                pokemon=Pokemon(list(DEX.values())[i][j], SUITS[j], VALS[i], j)
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
        def get_rating(attacking_poke, defending_poke):
            attack_cor = TYPES_FOR_DAMAGE.index(attacking_poke.types[0].title())
            defend_cor = TYPES_FOR_DAMAGE.index(defending_poke.types[0].title())
            
            rating = int(DAMAGE_ARRAY[attack_cor][defend_cor])

            if rating == 0:
                return -2
            elif rating == 0.5:
                return -1
            elif rating == 2:
                return 1
            else:
                return 0

        selected_rating = selected_pokemon.power + get_rating(selected_pokemon, self.opponent)    
        opponent_rating = self.opponent.power + get_rating(self.opponent, selected_pokemon)

        winner = selected_pokemon if selected_rating >= opponent_rating else self.opponent
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
     
    def getLocation(self):
        """
        PUBLIC; selects location for battle from NASA API; return type: string
        """
        with open("keys/key_nasa.txt", "r") as keyfile:
            key = keyfile.readline()
            
        photos = []
        while photos == []: #when there are no photos for the day "sol" the list is empty 
            sol = random.randint(550,1000)
            with urlopen(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&camera=fhaz&api_key={key}") as response:
                html = response.read()

            dic = json.loads(html)
            photos = dic["photos"]
            

        location = photos[0]["img_src"]
        return location  

    def end_game(self):
        del self