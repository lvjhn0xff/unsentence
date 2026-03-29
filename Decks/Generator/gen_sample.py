import genanki 
from utils.model import base_model 
from utils.deck import create_deck
from utils.note import create_note 

decks = []

sample_deck = create_deck("Sample Deck") 
note = create_note(base_model, "<u>Question</u> | Hello there...", "Answer") 

sample_deck.add_note(note)

decks.append(sample_deck)

genanki.Package(decks).write_to_file("outputs/sample.apkg")