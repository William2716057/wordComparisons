import spacy

nlp = spacy.load("en_core_web_lg")

word1 = "red"
word2 = "pink"

word1 = nlp.vocab[word1]
word2 = nlp.vocab[word2]

print("Word similarity: ", word1.similarity(word2))

sentence1 = nlp("this is good")
sentence2 = nlp("This is bad")

print("Sentence similarity: ", sentence1.similarity(sentence2))
