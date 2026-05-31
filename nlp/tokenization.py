import nltk

nltk.download("punkt")
nltk.download("punkt_tab")

text = "Hello world. This is an NLP course. It is very interesting!"
sentences = nltk.tokenize.sent_tokenize(text)
words = nltk.tokenize.word_tokenize(text)

print(sentences)
print(words)
