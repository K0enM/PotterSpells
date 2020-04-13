from src import spell_reader as sr
import pyttsx3
import json


class SpellNotFoundError(Exception):
    pass


class NameNotFound(Exception):
    pass


engine = pyttsx3.init()
names = ["Harry", "Hermione", "Ron"]

def cast(spellname):
    spells = sr.load_spells("../data/spells.json")
    spell_data = json.loads(spells)
    for spell in spell_data["spells"]:
        if spell["incantation"] == spellname:
            engine.say(spellname)
            engine.runAndWait()
            return
    raise SpellNotFoundError("That is not an existing spell!")


def change_character(name):
    voices = engine.getProperty("voices")
    if name not in names:
        raise NameNotFound("That is not a Harry Potter character that can cast spells")
    if name == "Harry":
        engine.setProperty("voice", voices[0].id)
    else:
        print(f"Unfortunately, there is only one voice installed")

cast("Accio")
change_character("Hermione")
cast("Accio")