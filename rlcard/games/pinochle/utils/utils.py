'''
    File name: bridge/utils/utils.py
    Author: William Hale
    Date created: 11/26/2021
'''

from typing import List

import numpy as np

from .pinochle_card import PinochleCard


def encode_cards(cards: List[PinochleCard]) -> np.ndarray:  # Note: not used ??
    plane = np.zeros(52, dtype=int)
    for card in cards:
        plane[card.card_id] = 1
    return plane
