import spacy

nlp = spacy.load("en_core_web_lg")

word1 = "red"
word2 = "pink"

word1 = nlp.vocab[word1]
word2 = nlp.vocab[word2]

print(word1.similarity(word2))

