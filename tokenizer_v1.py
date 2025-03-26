import re

class Tokenizer:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {val: key for key, val in vocab.items()}
    
    # Convert text into token IDs
    def encode(self, text):
        preprocessed = list(filter(None, re.split(r'([,.:;?_!"()\'])|__|\s', text)))  # Remove None values
        preprocessed = [item.strip() for item in preprocessed if item.strip()]  # Remove empty strings
        token_ids = [self.str_to_int[token] for token in preprocessed if token in self.str_to_int]  # Avoid KeyError
        return token_ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s([,.:;?_!"()\'])', r'\1', text)  # Remove space before punctuation
        return text

def main():
    # Read text file
    with open("the-verdict.txt", 'r', encoding="utf-8") as f:
        raw_text = f.read()

    # Tokenize text
    preprocessed = list(filter(None, re.split(r'([,.:;?_!"()\'])|__|\s', raw_text)))  # Remove None values
    preprocessed = [item.strip() for item in preprocessed if item.strip()]  # Remove empty strings

    vocab = sorted(set(preprocessed))
    vocabulary = {val: id for id, val in enumerate(vocab)}

    simple_tokenizer = Tokenizer(vocabulary)

    # Test encoding
    text = "In the dimmest corner of her boudoir, amid a profusion of delicate and distinguished objects, hung one of the familiar oval canvases, in the inevitable garlanded frame. The mere outline of the frame called up all Gisburn's past!"
    encode_text_id = simple_tokenizer.encode(text)

    print(encode_text_id)

    print(simple_tokenizer.decode(encode_text_id))


if __name__ == "__main__":
    main()
