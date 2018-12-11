import nltk
import re

INPUT_FILE = 'asoif.txt'
OUTPUT_FILE = 'asoif_processed.txt'
DEFAULT_ENCODING = 'utf-8'
RE_WORDS = r'(\w+[-\w+]*)'

def read_file(path, encoding):
    with open(path, 'r', encoding=encoding) as file:
        text = file.read()
    return text


def is_valid(sentence):
    return re.search('\w+', sentence)


def remove_punctuation(sentence):
    return " ".join(re.findall(RE_WORDS, sentence))


def process_sentences(raw_sentences, output_file):
    for raw_sent in raw_sentences:
        # consider \n symbol as a new sentence
        for sent in raw_sent.splitlines():
            if is_valid(sent):
                processed_sent = remove_punctuation(sent)
                output_file.write(processed_sent + "\n")


def main():
    raw_text = read_file(INPUT_FILE, DEFAULT_ENCODING)
    raw_sentences = nltk.tokenize.sent_tokenize(raw_text)
    with open(OUTPUT_FILE, "w", encoding=DEFAULT_ENCODING) as f_out:
        process_sentences(raw_sentences, f_out)


if __name__ == "__main__":
    main()


