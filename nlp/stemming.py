import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")

text = "The cats are running and jumping quickly."
ps = nltk.stem.PorterStemmer()
words = word_tokenize(text)

stemmed = [ps.stem(w) for w in words]
print(stemmed)
