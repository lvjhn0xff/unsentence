import genanki 
from utils.model import base_model 
from utils.deck import create_deck
from utils.note import create_note 
import yaml 
from collections import deque
from utils.buffered_flush import BufferedFlush
from utils.helpers import *

def handle_chapters(
    parent_name, 
    decks,
    subject_data, 
    start_chapter = 0, 
    part_no = None,
    extra = False
):
    chapters = subject_data.get("Chapters", None)
    extra_chapters = subject_data.get("Extra-Chapters", None)
    chapter_label = subject_data.get("Chapter-Label", None)
    reset_chapters = subject_data.get("Reset-Chapters", None)
    is_appendix = subject_data.get("Is-Appendix", None)
    
    if reset_chapters:
        start_chapter = 0

    index = start_chapter + 0
    
    buffer = BufferedFlush(10)
    buffer.args = {
        "split_count" : 0,
        "parent_name" : parent_name,
        "decks" : decks
    }

    has_initialized = False

    buffer.flush = splitter

    if extra_chapters and extra: 
        chapters = extra_chapters

    for subject_specifier in chapters:

        chapter_no = None  

        sub_chapters = []

        # if sub-items 
        if type(subject_specifier) is dict: 
            sub_items = subject_specifier.get("Sub-Items", None)
            if sub_items: 
                for item in sub_items:
                    sub_chapters.append(item)

        if chapter_label == "Chapter-Number": 
            chapter_no = index + 1
        elif chapter_label == "Part-Bullet": 
            chapter_no = f"{part_no}.{index + 1}"
        elif chapter_label == "Appendix-Letters": 
            chapter_no = chr(ord('A') + index)
        else: 
            chapter_no = index + 1

        if extra:
            chapter_no = f"E:{chapter_no}"

        chapter_label = "Chapter"
        if is_appendix: 
            chapter_label = "Appendix"

        # record single chapter 
        if len(sub_chapters) == 0: 
            cardA_front, cardA_back = \
                prepare_subject_card(
                    shortname, 
                    "Chapters | " + subject_specifier, 
                    "Number", 
                    chapter_label + " "  + str(chapter_no)
                )
            cardB_front, cardB_back = \
                prepare_direct_card(
                    shortname, 
                    "Chapter " + str(chapter_no), 
                    subject_specifier
                )
            
            card_a = create_note(base_model, cardA_front, cardA_back) 
            card_b = create_note(base_model, cardB_front, cardB_back) 

            buffer.add(card_a)
            buffer.add(card_b)
        else: 
            for subchapter in sub_chapters: 
                cardA_front, cardA_back = \
                    prepare_subject_card(
                        shortname, 
                        "Chapters | " + subchapter["Name"], 
                        "Number", 
                        "Chapter " + subchapter["Key"]
                    )
                cardB_front, cardB_back = \
                    prepare_direct_card(
                        shortname, 
                        "Chapter " + subchapter["Key"],
                        subchapter["Name"], 
                    )
                cardA = create_note(base_model, cardA_front, cardA_back) 
                cardB = create_note(base_model, cardB_front, cardB_back) 

                buffer.add(cardA)
                buffer.add(cardB)
                    
        index += 1

    buffer.end()

    return index

def handle_parts(parent_name, decks, subject_data): 
    parts = subject_data.get("Parts", None) 
    shortname = subject_data.get("Shortname", None)
    subchapters = subject_data.get("Subchapters", None)

    part_deck_name = f"{parent_name}::000 - Parts"
    part_deck = create_deck(part_deck_name)
    decks.append(part_deck)

    buffer = BufferedFlush(10)
    buffer.args = {
        "split_count" : 0,
        "parent_name" : part_deck_name, 
        "decks" : decks
    }

    buffer.flush = splitter 

    last_chapter = 0

    index = 0 
    for part_data in parts: 
        part_name = part_data.get("Part-Name", None)
        is_appendix = part_data.get("Appendix", None) 
        part_no = index + 1

        # Card A 
        card_a_front, card_a_back = \
            prepare_subject_card(
                shortname, 
                part_name, 
                "Part Number", 
                f"Part {part_no}"
            )

        # Card B
        card_b_front, card_b_back = \
            prepare_direct_card(
                shortname, 
                f"Parts {part_no}",
                part_name, 
            )

        # Add notes
        note_a = create_note(base_model, card_a_front, card_a_back)
        note_b = create_note(base_model, card_b_front, card_b_back)
    
        # Add notes to the deck
        buffer.add(note_a)
        buffer.add(note_b)

        # Handle chapter 
        if subchapters: 
            last_chapter = 0 

        last_chapter = \
            handle_chapters(
                f"{parent_name}::001 - Chapters::Part {part_no:03}", 
                decks, 
                part_data, 
                start_chapter=last_chapter,
                part_no=part_no
            )

        index += 1

    buffer.end()

if __name__ == "__main__":
    # Input File 
    SUBJECTS_FILE = "./data/Subject Meta/Subjects.yaml"

    # Gather information about subjects
    subjects_data = None
    with open(SUBJECTS_FILE, "r") as file: 
        subjects_data = yaml.safe_load(file)

    # Decks 
    decks = []

    # Create base deck.
    gs_deck_name = "GS" 
    gs = create_deck(gs_deck_name) 

    # Create subjects deck 
    subjects_deck_name = f"{gs_deck_name}::Subjects" 
    subjects_deck = create_deck(subjects_deck_name)

    # Create meta subjects deck.
    subjects_meta_deck_name = f"{gs_deck_name}::Subjects::@ Meta" 
    subjects_meta_deck = create_deck(subjects_meta_deck_name)
    decks.append(subjects_meta_deck)

    # Gather subjects 
    for subject in subjects_data: 
        subject_data = subject 
        code = subject_data.get("Code", None)
        name = subject_data.get("Name", None)
        shortname = subject_data.get("Shortname", None)
        chapter_label = subject_data.get("Chapter-Label", None)
        chapters = subject_data.get("Chapters", None)
        parts = subject_data.get("Parts", None)
        extra_chapters = subject_data.get("Extra-Chapters", None)  

        # Generate deck for subjects 
        subject_deck_name = f"{code} - {shortname}"
        subject_deck_name = f"{subjects_deck_name}::{subject_deck_name}"

        # Generate question for subject name.  
        subject_question_note_a = create_note(base_model, f"GS | Subject Names [{code}]", name)
        subject_question_note_b = create_note(base_model, f"GS | {name} | Subject Code", code)
        subjects_meta_deck.add_note(subject_question_note_a) 
        subjects_meta_deck.add_note(subject_question_note_b) 

        # go through chapters if the subject has chapters 
        if chapters and not parts: 
            if extra_chapters:
                handle_chapters(
                    subject_deck_name + "::001 - Main Chapters", 
                    decks, 
                    subject_data
                )
            else: 
                handle_chapters(
                    subject_deck_name, 
                    decks, 
                    subject_data
                )
        elif parts: 
            handle_parts(subject_deck_name, decks, subject_data)

        # check if has extra chapters 
        if extra_chapters: 
            handle_chapters(
                subject_deck_name + "::002 - Extra Chapters", 
                decks, 
                subject_data,
                extra=True
            )
            

    # create decks
    genanki.Package(decks).write_to_file("outputs/subjects.apkg")