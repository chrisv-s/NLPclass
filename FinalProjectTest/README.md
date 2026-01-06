# AI Text Ambiguity Project

## What This Project Is About

So, this project started because I was curious why AI-generated text often seems “ambiguous” and whether that ambiguity actually *means* anything. In normal human language, ambiguity is when a sentence can make sense in two or more ways. But with AI, it’s often not really ambiguity—it’s more like the AI is unsure and just produces vague, kind of bland, or generically plausible sentences.

I wanted to play around with this, so I built a little system that takes two sentences and tries to generate a third sentence that could sort of relate to both. It doesn’t try to actually “understand” the sentences. Instead, it looks at the overlap in meaning using word vectors and picks words that are kind of in the middle between the two inputs. The results are often neutral, a bit funny, or weirdly abstract—basically highlighting the gap between how humans interpret language and what AI actually does.

## How It Works 

The system is actually pretty simple under the hood, but I tried to make it as transparent as possible:

1. **Analyze the sentences**: I use **spaCy** to break each input into subject-verb-object (SVO) chunks.
2. **Find the middle**: For each subject, verb, and object, I compute a kind of semantic “midpoint” based on their word vectors. I actually do this at two levels—word-level and chunk-level—so the system considers both single words and small phrases.
3. **Pick candidates**: Instead of hardcoding words, the system looks at a list of common English words and finds the ones closest to the midpoint while still being the right type (noun, verb, pronoun, etc.).
4. **Build a sentence**: Finally, it puts together a new SVO sentence using these candidates.

The goal isn’t to make perfect sentences—it’s to see what happens when you smooth over the differences statistically and let the AI pick “neutral” words.

## What I Learned / Observations

.....

## How to Try It

1. Run the Python script.
2. Enter one sentences when prompted.
3. Watch the pipeline generate a third sentence that’s (according to the language model) in the middle of the first two.

## Dependencies

- Python 3
- [spaCy](https://spacy.io/) with the `en_core_web_md` model
- NumPy

