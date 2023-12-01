'''
    File name: bridge/dealer.py
    Author: William Hale
    Date created: 11/25/2021
'''

from typing import List

from .player import PinochlePlayer
from .utils.pinochle_card import PinochleCard


class PinochleDealer:
    ''' Initialize a PinochleDealer dealer class
    '''
    def __init__(self, np_random):
        ''' set shuffled_deck, set stock_pile
        '''
        self.np_random = np_random
        self.shuffled_deck: List[PinochleCard] = PinochleCard.get_deck()  # keep a copy of the shuffled cards at start of new hand
        self.np_random.shuffle(self.shuffled_deck)
        self.stock_pile: List[PinochleCard] = self.shuffled_deck.copy()

    def deal_cards(self, player: PinochlePlayer, num: int):
        ''' Deal some cards from stock_pile to one player

        Args:
            player (PinochlePlayer): The PinochlePlayer object
            num (int): The number of cards to be dealt
        '''
        for _ in range(num):
            player.hand.append(self.stock_pile.pop())
