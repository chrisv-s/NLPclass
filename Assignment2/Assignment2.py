import json
import spacy
import random
import markovify

nlp = spacy.load("en_core_web_sm")

# This project transforms Kanye West’s lyrics into a “food-rap” remix. lyrics source: # https://www.kaggle.com/datasets/viccalexander/kanyewestverses?resource=download
# First, spaCy is used to parse each line and identify adjectives and nouns...These words are then replaced with items
# from two food datasets from https://github.com/dariusk/corpora/tree/master/data/foods keeping the original grammatical
# structure mostly intact. After the food-themed lines are created, the entire transformed text is passed into a Markovify model.
# Markovify learns the patterns and flow of the lyrics and generates new lines that sound similar

with open("wine_descriptions.json", "r", encoding="utf8") as f:
    wines = json.load(f)

with open("vegetables.json", "r", encoding="utf8") as f:
    vegetables = json.load(f)

food_adjs = [w.strip().lower() for w in wines["wine_descriptions"]]
food_nouns = [v.strip().lower() for v in vegetables["vegetables"]]

with open("kanyewest.txt", "r", encoding="utf8") as f:
    rap_lines = [line.strip() for line in f if line.strip()]

rap_docs = [nlp(line) for line in rap_lines]

food_rap_lines = []

for doc in rap_docs:
    new_tokens = []

    # So I want to switch out the nouns and adjectives from the lyrics with food words and loop through every element for that
    for token in doc:
        if token.pos_ == "ADJ" and food_adjs:
            new_tokens.append(random.choice(food_adjs))
        elif token.pos_ == "NOUN" and food_nouns:
            new_tokens.append(random.choice(food_nouns))
        else:
            new_tokens.append(token.text)

    # Then I join the tokens back into a single string and add to the list
    food_rap_lines.append(" ".join(new_tokens))


# Then I use Markovify to remix the lines, for that I need to combine all food-rap lines into a single text for Markovify
food_rap_text = "\n".join(food_rap_lines)

# Using the Markovify NewlineText Tool I create new lyrics (it remembers two words to create some new interesting patterns)
text_model = markovify.NewlineText(food_rap_text, state_size=2)

print("REMIXED FOOD-RAP LYRICS: ")
for lol in range(10):
    line = text_model.make_sentence(tries=100)
    if line:
        print(line)
