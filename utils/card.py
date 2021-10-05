#Clubs (♣),Hearts (♥), Diamonds (♦), Spades (♠)
# color = ["black", "red"], icon = ["Clubs", "Hearts", "Diamonds", "Spades"], value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Symbol:
	'''A class to store the card symbols.'''

	def __init__(self, color, icon):
		'''Initialize a symbol and set its icon and color.'''
	
		self.icon = icon
		self.color = color
	    
	def __str__(self):
		'''Return a symbol which consists of an icon and a color.'''
		return f"{self.color}, {self.icon}"

class Card(Symbol):
	'''A class to create a card. This class inherits from Symbol'''

	def __init__(self, color, icon, value):
		super().__init__(color, icon)
		
        # Initialize a card that inherits an icon and a color from Symbol and set its value.
		self.value = value
		

	def __str__(self):
		'''Return a card which consists of an icon, a color and a value.'''    
		return f"{self.color}, {self.icon}, {self.value}"

	def create_list_of_cards(self):
		'''Creates a list with 4 cards'''



mySymbol = Symbol('black', 'spades')
print(mySymbol)
print(mySymbol.color)
print(mySymbol.icon)

myCard = Card('black', 'spades','4')
print(myCard)
print(myCard.color)
print(myCard.icon)
print(myCard.value)
