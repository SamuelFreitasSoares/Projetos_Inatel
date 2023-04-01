from DataB import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
pokemon = db.collection.find_one({"name": "Bulbasaur"})
writeAJson(pokemon, "pokemon")


#--------------------------------------------------------------#


from pokedex import Pokedex
from helper.WriteAJson import writeAJson


def main():

    types = ["Bug"]
    pokemons_Bug = Pokedex.getPokemonsByType(types)
    writeAJson(pokemons_Bug, "pokemons_Bug")

    types = ["Fire"]
    pokemons_Fire = Pokedex.getPokemonsByType(types)
    writeAJson(pokemons_Fire, "pokemons_Fire")

    pokemons_by_Weight = Pokedex.getPokemonsByWeight("80.0 kg")
    writeAJson(pokemons_by_Weight, "Pokemons_Weight_80kg")

    pokemons_Height = Pokedex.getPokemonsByHeight("0.61 m")
    writeAJson(pokemons_Height, "Pokemon_61cm")

    pokemons_Candy = Pokedex.getPokemonsByCandy("50")
    writeAJson(pokemons_Candy, "Pokemons_Candy50")


if __name__ == '__main__':
    main()