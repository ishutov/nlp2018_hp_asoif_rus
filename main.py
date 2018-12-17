import glob
import re
import subprocess
import sys

import nltk

OUTPUT_FILE = '_processed.txt'
OUTPUT_LEM_FILE = '_processed_lem.txt'
DEFAULT_ENCODING = 'utf-8'
RE_WORDS = r'(\w+[-\w+]*)'


def get_book_name(arg):
    if arg not in ["asoif", "hp"]:
        raise Exception("The book series must be either *ASOIF* or *HP*")
    return arg


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


def lemmatize(input_file, output_file, replacement_words):
    subprocess.call([r"./mystem.exe", "-lcd", input_file, output_file])
    raw_text = read_file(output_file, DEFAULT_ENCODING)
    with open(output_file, "w", encoding=DEFAULT_ENCODING) as f_out:
        for sent in raw_text.splitlines():
            processed_sent = remove_punctuation(sent)
            final_sent = ""
            for word in processed_sent.split(' '):
                replace = False
                for repword in replacement_words:
                    if repword.replace('ё', 'е') == word:
                        final_sent += repword + " "
                        replace = True
                if not replace:
                    final_sent += word + " "
            f_out.write(final_sent.strip() + "\n")


def getAllWordsFromDataset(INFILE, encoding):
    result = []
    for name in glob.glob(INFILE + '*'):

        for line in open(name, encoding=encoding):
            if line.startswith(':') or line.startswith('"') or not line.strip():
                continue

            words = line.split(' ')
            words = [word.strip() for word in words]
            for word in words:
                if "ё" in word:
                    result.append(word)

    return list(set(result))


def main():
    if len(sys.argv) < 2:
        raise Exception("We need three command line arguments: main.py book")
    book = get_book_name(sys.argv[1].lower())
    raw_text = read_file(book + ".txt", DEFAULT_ENCODING)
    raw_sentences = nltk.tokenize.sent_tokenize(raw_text)
    with open(book + OUTPUT_FILE, "w", encoding=DEFAULT_ENCODING) as f_out:
        process_sentences(raw_sentences, f_out)
    oy_words = getAllWordsFromDataset("./dataset/" + book, DEFAULT_ENCODING)
    lemmatize(book + OUTPUT_FILE, book + OUTPUT_LEM_FILE, oy_words)


if __name__ == "__main__":
    main()
