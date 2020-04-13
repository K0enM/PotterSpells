from src import spell_reader as sr
import pyttsx3
import json


class SpellNotFoundError(Exception):
    pass


def cast(spellname):
    spells = sr.load_spells("../data/spells.json")
    spell_data = json.loads(spells)
    for spell in spell_data["spells"]:
        if spell["incantation"] == spellname:
            pyttsx3.speak(spellname)
            return 
    raise SpellNotFoundError("That is not an existing spell!")

