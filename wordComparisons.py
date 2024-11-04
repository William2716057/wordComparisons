import spacy

nlp = spacy.load("en_core_web_lg")

word1 = "red"
word2 = "ref"

word1 = nlp.vocab[word1]
word2 = nlp.vocab[word2]

print("Word similarity: ", word1.similarity(word2))

sentence1 = input(nlp("Enter sentence 1: "))
sentence2 = input(nlp("Enter sentence 2: "))

sentence1 = nlp(sentence1)
sentence2 = nlp(sentence2)

print("Sentence similarity: ", sentence1.similarity(sentence2))

print(" ".join([token.lemma_ for token in sentence1 if token.pos_ == "VERB"]))
print(" ".join([token.lemma_ for token in sentence1 if token.pos_ == "NOUN"]))
print(" ".join([token.lemma_ for token in sentence1 if token.pos_ == "ADJ"]))

print(" ".join([token.lemma_ for token in sentence2 if token.pos_ == "VERB"]))
print(" ".join([token.lemma_ for token in sentence2 if token.pos_ == "NOUN"]))
print(" ".join([token.lemma_ for token in sentence2 if token.pos_ == "ADJ"]))
