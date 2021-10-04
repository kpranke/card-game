icon = ["♠", "♡", "♢", "♣"] #Clubs (♣),Hearts (♥), Diamonds (♦), Spades (♠)
color = ["black", "red"]

symbols = [
	{
	'black': ["♠", "♣"]
	},{
	'red' : ["♡", "♢"]
	}
]


Class Symbol:
'''A class to store card symbols.'''
	def __init__(self, icon: str, color: str):
		# Symbol is defined by its icon and color
	    self.icon = icon
	    self.color = color

	def show(self):        

Class Card(Symbol):
'''A class to create a card. This class inherits from Symbol'''
	 def __init__(self, icon, color, value):
        # A Card inherits an icon and a color from Symbol and also has a value
        Symbol.__init__(self, icon, color)
        self.value = value
