from utils.deck import create_deck

def prepare_subject_card(shortname, front, prompt, back):
    card_front = f"<u>{shortname}</u> | {front} | {prompt}" 
    card_back  = str(back)
    return card_front, card_back

def prepare_direct_card(shortname, front, back):
    card_front = f"<u>{shortname}</u> | {front}" 
    card_back  = str(back)
    return card_front, card_back

def splitter(items, args): 
    decks = args['decks']
    split_count = args['split_count']
    parent_name = args['parent_name']
    partial_deck = create_deck(f"{parent_name}::Split {split_count:03}")
    for item in items: 
        partial_deck.add_note(item)
    decks.append(partial_deck)
    args['split_count'] += 1

    