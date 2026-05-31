from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

text = "NLP is fun. NLP is interesting. NLP helps in many applications."
words = word_tokenize(text)
fdist = FreqDist(words)
print(fdist.most_common(5))
