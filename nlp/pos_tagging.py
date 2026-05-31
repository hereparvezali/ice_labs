import nltk
from nltk.tokenize import word_tokenize

nltk.download("averaged_perceptron_tagger_eng", quiet=True)

text = "The quick brown fox jumps over the lazy dog."
words = word_tokenize(text)
pos_tags = nltk.pos_tag(words)
print(pos_tags)
