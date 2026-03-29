import genanki
import random

base_model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    "Base Model",
    fields=[
        {"name": "Question"},
        {"name": "Answer"}
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": """
                {{FrontSide}}
                <hr id="answer">
                {{Answer}}
            """
        }
    ],
    css="""
        .card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
        }

        hr#answer {
            margin-top: 20px;
            margin-bottom: 20px;
        }
    """
)



content_model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    "Base Model",
    fields=[
        {"name": "Question"},
        {"name": "Answer"}
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": """
                {{FrontSide}}
                <hr id="answer">
                {{Answer}}
            """
        }
    ],
    css="""
        .card {
            font-family: arial;
            font-size: 20px;
            color: black;
            background-color: white;
        }

        hr#answer {
            margin-top: 20px;
            margin-bottom: 20px;
        }


        .header {
            padding-bottom: 10px;
            text-align: left;
        }

        [class^="level-"] {
            text-align: left;
            padding-left: 50px;
        }
    """
)