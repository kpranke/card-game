# Import everything you need to start the game!
# Start the game. You should only run this file to have the game running.
from utils.player import Player, Deck
from utils.game import Board
from utils.card import Card


print('The game has started.')
player_1_name = input('Add name of player 1: ')
player_2_name = input('Add name of player 2: ')
#for element in range(number_players):
#	name = input('Add name of a player')
#	Player(name)
player_1 = Player(player_1_name)
player_2 = Player(player_2_name)

players = [player_1, player_2] 


for element in players:
	print(f"Welcome, {element}!")

newdeck = Deck()
newdeck.fill_deck()
newdeck.shuffle()
newdeck.distribute(players)

player_1.play()



#board = Board()
#board.start_game()