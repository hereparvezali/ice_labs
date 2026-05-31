import string

text = "Hello, World! This is Natural Language Processing."
cleaned = text.lower().translate(str.maketrans("", "", string.punctuation))
print(cleaned)
