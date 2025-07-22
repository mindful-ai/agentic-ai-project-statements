# cards.py
class Card:
    def __init__(self, rank, suit, status="in deck"):
        self.rank = rank
        self.suit = suit
        self.status = status

    def __repr__(self):
        return f"Card({self.rank}, {self.suit}, {self.status})"


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        pass

    def remove_card(self, card):
        pass

    def update_card_status(self, card, new_status):
        pass

    def list_cards(self, status=None):
        pass
