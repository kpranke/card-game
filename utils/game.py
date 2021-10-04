
class Deck:
	'''A class to store a deck of cards.'''
	def __init__(self):
		''' Initialize a deck of cards'''
        self.cards = []
        for icon in range(4):  
            for value in range(13):
                self.cards.append(Card(icon, value))
    def show(self):
    	'''Shows a deck of cards'''
        list_of_cards = []
        for element in self.cards:
            list_of_cards.append(element.show())
        return list_of_cards
    def shuffle():
    	''' Shuffles all cards in the list of cards. '''

    def distribute():
    	'''
    	Takes a list of players as a parameter and distributes the cards evenly between all the players.
    	'''   

class Board:
	'''A class to stores a board'''
	def __init__(self, players, turn_count, active_cards, history_cards):

	def start_game():
	''' 
	Starts the game, fills a Deck, distributes cards of the Deck to the players.
	'''	