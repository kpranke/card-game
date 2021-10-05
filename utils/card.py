#Clubs (♣),Hearts (♥), Diamonds (♦), Spades (♠)


values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Symbol:
	'''A class to store card symbols.'''
	colors = ["black", "red"]
	icons = ["♥", "♦", "♣", "♠"]
	def __init__(self, icon: str, color: str):
		'''Initialize a symbol and set its icon and color.'''
		self.icon = icon
		self.color = color
	    
	def show(self):
		'''Return a symbol which consists of an icon and a color.'''   
		return f"{Card.colors[self.color]} {Card.icons[self.icon]}"

class Card(Symbol):
	'''A class to create a card. This class inherits from Symbol'''
	def __init__(self, icon, color, value):
        # Initialize a card that inherits an icon and a color from Symbol and set its value.
		Symbol.__init__(self, icon, color)
		self.value = value

	def show(self):
		'''Return a card which consists of an icon, a color and a value.'''    
		return f"Color: {self.color} Icon:{self.icon} Value {self.value}"

