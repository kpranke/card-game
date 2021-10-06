from utils.player import Player, Deck
from utils.game import Board
from utils.card import Card


player_1_name = input("Add name of player 1: ")
player_2_name = input("Add name of player 2: ")

player_1 = Player(player_1_name)
player_2 = Player(player_2_name)

players = [player_1, player_2]

for element in players:
    print(f"Welcome, {element}!")

board = Board(players)
board.start_game()

print(
    "This is it. Game over. If you want to make this game more fancy, consider contributing to the project! Ciao!"
)
