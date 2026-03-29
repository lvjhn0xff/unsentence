import genanki

def create_note(model, question, answer): 
    return genanki.Note(model=model, fields=[question, answer])