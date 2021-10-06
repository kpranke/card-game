from utils.card import Card
from utils.player import Player, Deck

# from card import Card
# from player import Player, Deck


class Board:
    """A class to stores a board"""

    def __init__(self, players: list):
        self.players = players
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def start_game(self):
        """
        Starts the game, fills a Deck, distributes cards of the Deck to the players.
        """
        print("The game has started.")
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(self.players)

        while self.turn_count < 26:
            self.turn_count += 1
            print(f"Starting turn {self.turn_count}")
            for player in self.players:
                card = player.play(self.turn_count)
                self.history_cards.append(card)
                self.active_cards.append(card)
