import glob
import re
import subprocess
import sys
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk
import spacy

OUTPUT_FILE = '_processed.txt'
OUTPUT_LEM_FILE = '_processed_lem.txt'
DEFAULT_ENCODING = 'utf-8'
RE_WORDS = r'(\w+[-\w+]*)'


def get_book_name(arg):
    if arg not in ["asoif", "hp", "asoif_eng", "hp_eng", "asoif_eng_processed", "hp_eng_processed"]:
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
                for rep_word in replacement_words:
                    if rep_word.replace('ё', 'е').lower() == word:
                        final_sent += rep_word + " "
                        replace = True
                        break
                if not replace:
                    final_sent += word + " "
            f_out.write(final_sent.strip() + "\n")

def lemmatizeENG(input_file, output_file):
    wordnet_lemmatizer = WordNetLemmatizer()
    raw_text = read_file(input_file, DEFAULT_ENCODING)
    with open(output_file, "w", encoding=DEFAULT_ENCODING) as f_out:
        for sent in raw_text.splitlines():
            lem_sent = ' '.join([wordnet_lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(sent)])
            # final_sent = wordnet_lemmatizer.lemmatize(sent, pos="v") + " "
            f_out.write(lem_sent.strip() + "\n")

def lemmatizeENG2(input_file, output_file):
    nlp = spacy.load('en', disable=['parser', 'ner'])
    raw_text = read_file(input_file, DEFAULT_ENCODING)
    with open(output_file, "w", encoding=DEFAULT_ENCODING) as f_out:
        for sent in raw_text.splitlines():
            doc = nlp(sent)
            lem_sent = " ".join([token.lemma_ if token.lemma_ != '-PRON-' else token.lower_ for token in doc])
            f_out.write(lem_sent.strip() + "\n")


def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

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
        raise Exception("We need three command line arguments: main.py book")
    book = get_book_name(sys.argv[1].lower())
    raw_text = read_file(book + ".txt", DEFAULT_ENCODING)
    raw_sentences = nltk.tokenize.sent_tokenize(raw_text)
    with open(book + OUTPUT_FILE, "w", encoding=DEFAULT_ENCODING) as f_out:
        process_sentences(raw_sentences, f_out)
    dataset_words = get_words_from_datasets("./datasets/" + book, DEFAULT_ENCODING)
    lemmatize(book + OUTPUT_FILE, book + OUTPUT_LEM_FILE, dataset_words)

    # lemmatizeENG(get_book_name(sys.argv[1].lower()) + ".txt", get_book_name(sys.argv[1].lower()) + "_lem.txt")
    # lemmatizeENG2(get_book_name(sys.argv[1].lower()) + ".txt", get_book_name(sys.argv[1].lower()) + "_lem.txt")

if __name__ == "__main__":
    main()
