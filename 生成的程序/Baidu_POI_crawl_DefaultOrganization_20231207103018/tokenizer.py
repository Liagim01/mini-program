'''
Tokenizer class
'''
import nltk
class Tokenizer:
    def __init__(self):
        nltk.download('punkt')
    def tokenize(self, data):
        # Tokenize text
        tokenized_text = []
        for text in data:
            tokens = nltk.word_tokenize(text)
            tokenized_text.append(tokens)
        return tokenized_text