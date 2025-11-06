import json
import random
import tracery
from tracery.modifiers import base_english

# So after having eaten a really bad sandwich last week, this is my revenge...
# I am using sandwiches.json, a library I found online

with open("sandwiches.json", "r") as f:
    sandwiches = json.load(f)

sandwich = random.choice(sandwiches)
sandwich_name = sandwich["name"]
ingredient = random.choice(sandwich["ingredients"])

rules = {
    "origin": ["#restaurant# ruined my #bodyPart#. The {sandwich} was #badAdj#. #ingredientSentence# #reaction#",
        "DO NOT EAT HERE. The {sandwich} gave me #illness#. #ingredientSentence# #reaction#",
        "#restaurant# made me question #existentialThought#. The {sandwich} was #badAdj#. #ingredientSentence#"],

    "ingredientSentence": ["Especially the {ingredient} — #ingredientInsult#.",
        "The {ingredient} alone could end civilizations.",
        "I still taste the {ingredient}, and I want to cry."],

    "restaurant": ["Leuphana Mensa", "Burger King", "HMS Mensa", "Penny", "HMS Café"],
    "bodyPart": ["stomach", "soul", "liver", "trust"],
    "badAdj": ["soggy", "radioactive", "slimy", "sad", "scandalous"],
    "illness": ["food poisoning", "diarrhea", "regret", "existential crisis"],
    "reaction": ["Never again.", "I regret being alive.", "Send help.", "I’m still recovering."],
    "existentialThought": ["my life choices", "the idea of eating", "humanity", "hope"],
    "ingredientInsult": ["who thought that was a good idea?","damn."]
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

# I found out that I basically need to let Tracery generate the sentence and then replace the injected random words from the
# sandwiches.json library afterwards for it to work

badReview = grammar.flatten("#origin#")
badReview = badReview.format(sandwich=sandwich_name, ingredient=ingredient)

print(badReview)
