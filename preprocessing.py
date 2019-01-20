import glob
import re
import subprocess
import sys
import nltk

"""
    This is the preprocessing file
    Usage: preprocessing.py book [lem]
    It removes punctuation, empty lines, lines without letters, split sentences and lemmatization if needed
"""


OUTPUT_FILE = '_processed.txt'
OUTPUT_LEM_FILE = '_processed_lem.txt'
DEFAULT_ENCODING = 'utf-8'
RE_WORDS = r'(\w+[-\w+]*)' # don't remove dashes in words like 'когда-нибудь', 'кто-то' etc.


def get_book_name(arg):
    acceptable_args = ["asoif", "hp", "asoif_eng", "hp_eng"]
    if arg not in acceptable_args:
        raise Exception("The book series must be in " + str(acceptable_args))
    return arg


def read_file(path, encoding):
    with open(path, 'r', encoding=encoding) as file:
        text = file.read()
    return text


def is_valid(sentence):
    return re.search('\w+', sentence) # leave only sentences contains at least one word character


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
    # run Yandex mystem for lemmatization
    subprocess.call([r"./mystem.exe", "-lcd", input_file, output_file])
    raw_text = read_file(output_file, DEFAULT_ENCODING)
    with open(output_file, "w", encoding=DEFAULT_ENCODING) as f_out:
        for sent in raw_text.splitlines():
            processed_sent = remove_punctuation(sent) # clean words from '{}' symbols put by mystem
            final_sent = ""
            # mystem replaces all 'ё' letters to 'e' and makes all words lowercase
            # so we need to proceed some steps to restore original words in the books
            for word in processed_sent.split(' '): # loop through words in each sentence in the books
                replace = False
                for rep_word in replacement_words: # loop through words in datasets
                    # replace 'ё' letters to 'e' and transform to lowercase
                    # if transformed word in dataset equals to word in sentence from book
                    # take the original word from dataset
                    if rep_word.replace('ё', 'е').lower() == word:
                        final_sent += rep_word + " "
                        replace = True
                        break
                if not replace:
                    final_sent += word + " "
            f_out.write(final_sent.strip() + "\n")


def get_words_from_datasets(INFILE, encoding):
    result = []
    for name in glob.glob(INFILE + '*'):
        for line in open(name, encoding=encoding):
            if line.startswith(':') or line.startswith('"') or not line.strip():
                continue
            words = line.split(' ')
            words = [word.strip() for word in words]
            for word in words:
                result.append(word)
    return list(set(result))


def main():
    if len(sys.argv) < 2:
        raise Exception("Usage: preprocessing.py book [lem]")
    is_lem = False
    if len(sys.argv) == 3:
        is_lem = True
    book = get_book_name(sys.argv[1].lower())
    raw_text = read_file(book + ".txt", DEFAULT_ENCODING)
    raw_sentences = nltk.tokenize.sent_tokenize(raw_text)
    with open(book + OUTPUT_FILE, "w", encoding=DEFAULT_ENCODING) as f_out:
        process_sentences(raw_sentences, f_out)
    if is_lem:
        dataset_words = get_words_from_datasets("./datasets/" + book, DEFAULT_ENCODING) # all words in datasets
        lemmatize(book + OUTPUT_FILE, book + OUTPUT_LEM_FILE, dataset_words)


if __name__ == "__main__":
    main()
