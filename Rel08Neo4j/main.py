from database import Database
from player import Player
from match import Match

db = Database("bolt://3.95.8.178:7687","neo4j","stands-termination-decision")
db.drop_all()

player_db = Player(db)
match_db = Match(db)

player_db.create_player("Pelé")
player_db.create_player("Maradona")
player_db.create_player("Cristiano Ronaldo")
player_db.create_player("Neymar")

player_db.update_player("Maradona", "Messi")

player_db.delete_player("Cristiano Ronaldo")

print("Jogadores =  ")
for player in player_db.get_players():
    print(player)

match_db.create_match(["Pelé", "Messi"], "O jogador Pelé ganhou do jogador Messi")
match_db.create_match(["Pelé", "Messi", "Neymar"], "Neymar ganha de Messi mas perde para Pelé")

match_db.delete_match("O jogador Pelé ganhou do jogador Messi")

print("\nJogadores que participaram dessa partida = ")
for match in match_db.get_match("Neymar ganha de Messi mas perde para Pelé"):
    print(match)

match_db.update_match("Neymar ganha de Messi mas perde para Pelé", "Neymar ganha de Messi e empata com Pelé")

print("\njogos em que o jogador Pelé participou =")
for match in match_db.get_match_per_player("Pelé"):
    print(match)

db.close()