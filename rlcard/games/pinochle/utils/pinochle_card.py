'''
    File name: bridge/utils/bridge_card.py
    Author: William Hale
    Date created: 11/25/2021
'''

from rlcard.games.base import Card


class PinochleCard(Card):

    suits = ['C', 'D', 'H', 'S']
    ranks = ['9', 'J', 'Q', 'K', 'T', 'A']

    @staticmethod
    def card(card_id: int):
        return _deck[card_id]

    @staticmethod
    def get_deck() -> [Card]:
        return _deck.copy()

    def __init__(self, suit: str, rank: str):
        super().__init__(suit=suit, rank=rank)
        suit_index = PinochleCard.suits.index(self.suit)
        rank_index = PinochleCard.ranks.index(self.rank)
        self.card_id = 13 * suit_index + rank_index

    def __str__(self):
        return f'{self.rank}{self.suit}'

    def __repr__(self):
        return f'{self.rank}{self.suit}'


# deck is always in order from 9C, ... TC, AC, 9D, ... TD, AD, 9H, ... TH, AH, 9S, ... TS, AS
_deck = [PinochleCard(suit=suit, rank=rank) for suit in PinochleCard.suits for rank in PinochleCard.ranks]  # want this to be read-only
