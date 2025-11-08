from collections import Counter
import string
def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        return text


def word_frequency(text: str):
    text = text.lower()
    # text = text.replace('.', '')
    # text = text.replace(',', '')
    text = text.translate(str.maketrans('','', string.punctuation))

    stop_words = ['a', 'an', 'the', 'end', 'in']

    word_unique = [word for word in text.split() if word not in stop_words]
    word_count = Counter(word_unique)

    print(dict(word_count))

    return dict(word_count)



if __name__ == "__main__":
    txt = read_file('empty_file.txt')

    word_frequency(txt)
