SUITS = ["H", "S", "C", "D"]

VALS = ["A"] + list(range(2,10)) + ["0", "J", "Q", "K"]

DEX = {
    "fire": ["Fennekin", "Vulpix", "Charizard", "Moltres"],
    "water": ["Squirtle", "Psyduck", "Blastoise", "Kyogre"],
    "grass": ["Snivy", "Turtwig", "Venusaur", "Virizion"],
    "electric": ["Mareep", "Pikachu", "Luxray", "Zapdos"],
    "psychic": ["Abra", "Espurr", "Alakazam", "Mewtwo"],
    "ghost": ["Gastly", "Duskull", "Gengar", "Giratina-altered"],
    "dark": ["Zorua", "Umbreon", "Houndoom", "Darkrai"],
    "steel": ["Cufant", "Melmetal", "Aggron", "Jirachi"],
    "dragon": ["Shelgon", "Axew", "Dragonite", "Rayquaza"],
    "fairy": ["Togepi", "Clefairy", "Sylveon", "Xerneas"],
    "flying": ["Noibat", "Corviknight", "Noivern", "Tornadus-incarnate"],
    "fighting": ["Mankey", "Mienfoo", "Machamp", "Marshadow"],
    "ice": ["Snorunt", "Avalugg", "Beartic", "Articuno"]
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

TYPES_FOR_DAMAGE = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                 "Fighting", "Poison", "Ground", "Flying", "Psychic",
                 "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

DAMAGE_ARRAY = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
                    [1, 2, 1/2, 1, 1/2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1/2, 1, 1, 1],
                    [1, 1, 2, 1/2, 1/2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1/2, 1, 1, 1],
                    [1, 1/2, 2, 1, 1/2, 1, 1, 1/2, 2, 1/2, 1, 1/2, 2, 1, 1/2, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 1/2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1/2, 1],
                    [2, 1, 1, 1, 1, 2, 1, 1/2, 1, 1/2, 1/2, 1/2, 2, 0, 1, 2, 2, 1/2],
                    [1, 1, 1, 1, 2, 1, 1, 1/2, 1/2, 1, 1, 1, 1/2, 1/2, 1, 1, 0, 2],
                    [1, 2, 1, 2, 1/2, 1, 1, 2, 1, 0, 1, 1/2, 2, 1, 1, 1, 2, 1],
                    [1, 1, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1/2, 1],
                    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1/2, 1, 1, 1, 1, 0, 1/2, 1],
                    [1, 1/2, 1, 1, 2, 1, 1/2, 1/2, 1, 1/2, 2, 1, 1, 1/2, 1, 2, 1/2, 1/2],
                    [1, 2, 1, 1, 1, 2, 1/2, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 1/2, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1/2, 0],
                    [1, 1, 1, 1, 1, 1, 1/2, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1/2],
                    [1, 1/2, 1/2, 1/2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1/2, 2],
                    [1, 1/2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1, 1, 1, 2, 2, 1/2, 1]]