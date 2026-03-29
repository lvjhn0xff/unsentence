import genanki
import time 
import random

def create_deck(name):
    deck_id = random.randrange(1 << 30, 1 << 31)
    return genanki.Deck(deck_id, name)
