import nltk
from nltk.tokenize import word_tokenize

nltk.download("wordnet")

text = "The cats are running and jumping quickly."
lemmatizer = nltk.stem.WordNetLemmatizer()
words = word_tokenize(text)

lemmatized = [lemmatizer.lemmatize(w) for w in words]

print(lemmatized)
