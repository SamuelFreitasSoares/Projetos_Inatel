from DataB import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")


class Pokedex:
    def getPokemonsByPrevolutionNum(name: str):
        return db.collection.find({"prev_evolution.name": name})

    def getPokemonsByType(types: list):
        return db.collection.find({"type": {"$in": types}})

    def getPokemonsByWeight(weight: str):
        return db.collection.find({"weight": weight})

    def getPokemonsByHeight(heigth: str):
        return db.collection.find({"heigth": heigth})

    def getPokemonsByCandy(candy: str):
        return db.collection.find({"candy": candy})