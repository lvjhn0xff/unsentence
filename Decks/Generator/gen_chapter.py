import genanki 
from utils.model import content_model 
from utils.deck import create_deck
from utils.note import create_note 
import yaml 
from collections import deque
from utils.buffered_flush import BufferedFlush
from utils.helpers import *
import sys 

cards = {
    "Objectives" : [],
    "Sections" : [], 
    "Terminologies" : [],
    "Notes" : [], 
    "OrderedSets" : [], 
    "UnorderedSets" : [],
    "Objects" : [],
    "Direct" : [],
    "Illustrations" : []
}

valid_keywords = {
    "Root" : set([
        "Course-Code", 
        "Course-Shortname",
        "Chapter No", 
        "Name", 
        "Objectives", 
        "Sections"
    ])
}

id_ = 0 

def deck_prefix(): 
    global id_ 
    id_ += 1
    return f"{id_:03}"

def validate_keywords(subject_data, valid_keywords):
    for key in subject_data: 
        if key not in valid_keywords: 
            raise Exception(
                f"Invalid keyword ({key}) not found in " +
                f"[{" | ".join(list(valid_keywords))}]"
            )

def create_card(deck, model, creation_fn): 
    card_front, card_back = creation_fn() 
    card = create_note(content_model, card_front, card_back) 
    deck.add_note(card)

def handle_objectives(parent_name, chapters_data, decks):
    print("--- Handle objectives")
    objectives = chapters_data.get("Objectives", None) 
    
    def create_card_1(index, objective):
        card_front = \
            f"<div class='header'>{chapters_data['Course-Shortname']}</div>" + \
            f"<div class='level-1'>Chapters | {chapters_data['Name']}</div>" + \
            f"<div class='level-2'>Objective {index + 1}</div>" 
        card_back = \
            f"{objective}"
        return card_front, card_back

    def create_card_2(index, objective): 
        card_front = \
            f"<div class='header'>{chapters_data['Course-Shortname']}</div>" + \
            f"<div class='level-1'>Chapters | {chapters_data['Name']}</div>" + \
            f"<div class='level-2'>Objectives | {objective}</div>" + \
            f"<div class='level-3'>Objective Number</div>"  
        card_back = \
            f"{objective}"
        return card_front, card_back 

    def create_card_3(index, objective): 
        card_front = \
            f"<div class='header'>{chapters_data['Course-Shortname']}</div>" + \
            f"<div class='level-1'>Chapters | {chapters_data['Name']}</div>" + \
            f"<div class='level-2'>Objectives Count</div>"
        card_back = \
            f"{objective}"
        return card_front, card_back 

    objectives_deck_name = \
        f"{parent_name}::" + \
        f"{chapters_data['Name']:03}::" + \
        f"{deck_prefix()} - Objectives"
    objectives_deck = create_deck(objectives_deck_name)
    decks.append(objectives_deck)

    for index, objective in enumerate(objectives): 
        create_card(
            objectives_deck, 
            content_model, 
            lambda: create_card_1(index, objective)
        )
        create_card(
            objectives_deck, 
            content_model,
            lambda: create_card_2(index, objective)
        )

    create_card(
        objectives_deck, 
        content_model, 
        lambda: create_card_3(index, len(objectives))
    )
        

def handle_section_list(parent_name, chapters_data, decks):
    print("--- Handling section list")
    sections = chapters_data.get("Sections", None) 
    chapter_no = chapters_data.get("Chapter-Number", None)
    
    sections_deck_name = \
        f"{parent_name}::" + \
        f"{chapters_data['Name']:03}::" + \
        f"{deck_prefix()} - Sections"
    sections_deck = create_deck(sections_deck_name)
    decks.append(sections_deck)
    
    def create_card_1(index, section):
        card_front = \
            f"<div class='header'>{chapters_data['Course-Shortname']}</div>" + \
            f"<div class='level-1'>Chapters | {chapters_data['Name']}</div>" + \
            f"<div class='level-2'>Section {index + 1}</div>" 
        card_back = \
            f"{section}"
        return card_front, card_back

    def create_card_2(index, section):
        card_front = \
            f"<div class='header'>{chapters_data['Course-Shortname']}</div>" + \
            f"<div class='level-1'>Chapters | {chapters_data['Name']}</div>" + \
            f"<div class='level-2'>Sections | {section}</div>" 
        card_back = \
            f"{section}"
        return card_front, card_back

    def create_card_3(index, section):
        card_front = \
            f"<div class='header'>{chapters_data['Course-Shortname']}</div>" + \
            f"<div class='level-1'>Chapters | {chapters_data['Name']}</div>" + \
            f"<div class='level-2'>Section Count</div>" 
        card_back = \
            f"{section}"
        return card_front, card_back

    for index, section in enumerate(sections): 
        section_no = index + 1 

        create_card(
            sections_deck, 
            content_model, 
            lambda: create_card_1(index, section)
        )
        create_card(
            sections_deck, 
            content_model,
            lambda: create_card_2(index, section)
        )
    
    create_card(
        sections_deck, 
        content_model,
        lambda: create_card_3(index, len(sections))
    )

#
# SECTIONS
# 
def handle_sections(parent_name, chapters_data, decks): 
    pass 

# TERMINOLOGIES
def handle_terminologies(parent_name, chapters_data, decks, chapter_index): 
    pass 

# NOTES 
def handle_notes(parent_name, chapters_data, decks, chapter_index): 
    pass 

# UNORDERED SETS 
def handle_unordered_sets(parent_name, chapters_data, decks, chapter_index): 
    pass

# ORDERED SETS 
def handle_ordered_sets(parent_name, chapters_data, decks, chapter_index): 
    pass

# OBJECTS 
def handle_objects(parent_name, chapters_data, decks, chapter_index): 
    pass

# DIRECT
def handle_direct_cards(parent_name, chapters_data, decks, chapter_index): 
    pass


if __name__ == "__main__":
    # CLI Parameters
    COURSE_SLUG = sys.argv[1]
    CHAPTER_FILE = sys.argv[2]

    # Input File 
    SUBJECTS_FILE = f"./data/Subjects/{COURSE_SLUG}/{CHAPTER_FILE}.yaml"

    # Gather information about subjects
    chapters_data = None
    with open(SUBJECTS_FILE, "r") as file: 
        chapters_data = yaml.safe_load(file)

    # Chapter Number 
    chapter_number = chapters_data.get("Chapter-Number", None)  
    chapter_name = chapters_data.get("Name", None) 
    course_slug_tokens = COURSE_SLUG.split("-")
    course_code = course_slug_tokens[0].strip() 
    course_shortname = course_slug_tokens[1].strip()
    chapters_data["Course-Code"] = course_code 
    chapters_data["Course-Shortname"] = course_shortname

    # Decks 
    decks = []

    # Base Deck Name 
    base_deck_name = f"GS::Main::{COURSE_SLUG}" 
    
    # Validate Keywords 
    validate_keywords(chapters_data, valid_keywords["Root"])

    # Handle Objectives 
    handle_objectives(base_deck_name, chapters_data, decks)

    # Handle Section List 
    handle_section_list(base_deck_name, chapters_data, decks)

    # create decks
    genanki.Package(decks).write_to_file(f"outputs/{COURSE_SLUG} - {CHAPTER_FILE}.apkg")