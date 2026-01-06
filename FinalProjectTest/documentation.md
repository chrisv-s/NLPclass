Phase 1: Conceptualization — Why Ambiguity Matters

When I started this project, I wanted to explore a question that’s been on my mind: why does AI-generated text often feel vague or ambiguous? In human language, ambiguity usually has a reason — a sentence can be interpreted in multiple coherent ways. AI, however, often produces text that looks ambiguous but is really just statistical uncertainty. My goal was to see what happens if a system tries to generate a sentence that sits between two distinct inputs — something that relates to both without explicitly choosing a meaning. The idea was simple: take two sentences, analyze them semantically, and create a third that lies somewhere in the “semantic middle” using vectors, embeddings, and probabilities, without relying on grammar rules or templates.

Phase 2: Building the SVO Extraction Pipeline

The first practical step was figuring out the input sentences. I used subject-verb-object (SVO) structures as the building blocks since they’re very simple and interpretable. SpaCy helped me identify nouns, pronouns, and verbs, and extract the core triplets. This worked well for short sentences, though I noticed it can fail with longer, more complex sentences — sometimes missing the subject or object. I then implemented a two-layer semantic interpolation: the word layer averaged the vectors of individual tokens, while the chunk/span layer included full noun phrases and noun-verb pairs to capture more context. The idea was to combine these to form a sort of semantic “midpoint” for each SVO element.

Phase 3: Candidate Selection 

Next, I needed to pick actual words from a vocabulary. I initially tried SpaCy’s full lexicon but ran into errors because Lexeme objects don’t have POS tags directly. My solution/idea was to include a words list: SpaCy could tag them, and I could pick candidates close to the midpoint of the analysed vectors and suitable for the SVO-structure. Even so, the system sometimes repeated one of the original words or produced odd sentences like “him eat water.” I experimented with adding some weighting to for example the noun-verb span and a touch of randomness to make outputs more varied, but that also made them less predictable. Interestingly, these “errors” were revealing: they showed the fuzzy areas in semantic space where the system replaces commitment with abstraction.

Phase 4: Third Sentence Generation 

Once words were chosen, generating the sentence was simple: just assemble the SVO words in order, optionally adding articles for readability. The resulting sentences felt mostly super random and funny — like “village eat ocean” from inputs such as “The man ate an apple” and “The father drank water.” These outputs confirmed my hypothesis: the language model doesn’t need to understand to produce text that seems meaningful. The challenge is that vector analysis/midpoint often landed in a semantic place that missed a lot of context, far from words that make perfect sense together. This explains why outputs are abstract or slightly nonsensical, even when SVO extraction and candidate selection are carefully done.

Phase 5: Reflection and Visualization 

Finally, I wanted to make the process transparent. I want to use the cosine similarity scores for each chosen word to visualize 
why certain words were chosen. I might want to give many different outputs and compare the similarity score behind them. 
