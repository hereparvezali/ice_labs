import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

text = "This is a simple sentence for removing stopwords in NLP."
words = word_tokenize(text)
stop_words = set(stopwords.words("english"))
filtered = [w for w in words if w.lower() not in stop_words]

print(stop_words)
print(filtered)
