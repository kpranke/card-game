
class Deck:
	'''A class to store a deck of cards.'''
	def __init__(self):
		''' Initialize a deck of cards'''
        self.cards = []
        for icon in range(4):  
            for value in range(13):
                self.cards.append(Card(icon, value))
    def show(self):
    	'''Show a deck of cards'''
        list_of_cards = []
        for element in self.cards:
            list_of_cards.append(element.show())
        return list_of_cards

class Board:
	'''A class to stores a board'''
	def __init__(self):