"""We have to implement the tokenizer class """

import re
class Tokenizer:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {val:key  for key, val in vocab.items()}
     # Convert text into token ID
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\'])|__|\s', text)
        # remove the space from the preprocessed
        preprocessed = [item.strip() for item in preprocessed if item.strip()]

        token_ids = [self.str_to_int[token]  for token in preprocessed]
        return token_ids
    def decode(self, ids):
        # Convert 
        text = " ".join([self.int_to_str[i] for i in ids])
        # Replace spaces before the specified punctuations 
        text = re.sub(r'([,.:;?_!"()\'])', r'\1', text)
        return text


def main():
    # First Make the vocab 
    with open("the-verdict.txt", 'r', encoding="utf-8") as f:
        raw_text = f.read()
    #print(raw_text)
    # First make the vocal 
    preprocessed = re.split(r'([,.:;?_!"()\'])|__|\s', raw_text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]

    vocab = sorted(set(preprocessed))
    vocablary = {val:id  for id, val in enumerate(vocab)}
    simple_tokenizer = Tokenizer(vocablary)

    text = "In the dimmest corner of her boudoir, amid a profusion of delicate and distinguished objects, hung one of the familiar oval canvases, in the inevitable garlanded frame. The mere outline of the frame called up all Gisburn's past!"
    encode_text_id = simple_tokenizer.encode(text)

    print(encode_text_id)
main()