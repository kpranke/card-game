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
		'''WRITE A BETTER DESCRIPTION randomly pick a Card in cards.'''
		shuffle(self.cards)
		card = self.cards.pop()
		self.history.append(card)
		print(f"{self.name} in turn {self.turn_count} played: {card}")
		return card

class Deck:
	'''A class to store a deck of cards.'''
	def __init__(self):
		''' Initialize a deck of cards'''
		self.cards = []
		self.players = []

	def fill_deck(self):
		icons = ["Club", "Heart", "Diamond", "Spade"]
		values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
		for icon in icons:
			if icon == "Heart" or icon =="Diamond":
				color = "red"
			else:
				color = "black"	
			for value in values:
				self.cards.append(Card(color, icon, value))


	def __str__(self): 
		'''Shows a deck of cards'''
		string_of_cards = ''
		for element in self.cards:
			string_of_cards += element.__str__() + " "
		return string_of_cards

	def shuffle(self):
		''' Shuffles all cards in the list of cards. '''
		shuffle(self.cards)
		print("The deck has been shuffled.")

	def distribute(self, players: list):
		'''
		Takes a list of players as a parameter and distributes the cards evenly between all the players.
		'''  
		while len(self.cards) > 0:
			for player in players:
				if len(self.cards) > 0:
					card = self.cards.pop()
					player.cards.append(card)
		print('Cards have been distributed.') # move to game

newdeck = Deck()
newdeck.fill_deck()
newdeck.shuffle()

player_1 = Player('Ian')
player_2 = Player('Jon')
player_3 = Player('Ina')
