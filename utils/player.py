from random import shuffle
from card import Card

class Player:
	'''A class to manage a player'''
	def __init__(self, name: str):
		self.name = name
		self.cards = [] #cards assigned
		self.turn_count = 0 
		self.number_of_cards = 0 
		self.history = [] #what cards were assigned to the player

	def __str__(self):
		return self.name	


	def play(self):
		'''randomly pick a Card in cards.
#Add the Card to the Player's history.
#Print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.
#Return the Card.'''

class Deck:
	'''A class to store a deck of cards.'''
	def __init__(self):
		''' Initialize a deck of cards'''
		icon = ["Clubs", "Hearts", "Diamonds", "Spades"]
		color = ["black", "red"]
		value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

		self.cards = []
		self.players = []
		for icon in range(4):  
			for value in range(13):
				self.cards.append(Card(color, icon, value))
	def __str__(self): #fill deck?
		'''Shows a deck of cards'''
		list_of_cards = []
		for element in self.cards:
			list_of_cards.append(element.__str__())
		return list_of_cards

	def shuffle(self):
		''' Shuffles all cards in the list of cards. '''
		random.shuffle(self.cards)
		print("deck shuffled")

	def distribute(self, players: list):
		'''
		Takes a list of players as a parameter and distributes the cards evenly between all the players.
		'''  
	'''while len(self.cards) > 0:
		for player in players:
			if len(self.cards) > 0:
				card = self.cards.pop()
				print(f"{player['name']} receives the following card:{card.show()}")
				player['cards'].append(card)'''

newdeck = Deck()
print(newdeck)
deck.shuffle()
for card in newdeck:
	print(card)
print(len(newdeck))	