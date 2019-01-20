import sys, glob, pickle
from operator import itemgetter

DEFAULT_ENCODING = 'utf-8'
MIN_NUM = 5

def check_frequencies(INFILE, BOOK, encoding):
    all_words = []
    for name in glob.glob(INFILE + '*.txt'):
        for line in open(name, encoding=encoding):
            if line.startswith(':') or line.startswith('"') or not line.strip():
                continue

            words = line.split(' ')
            words = [word.strip() for word in words]
            all_words.extend(words)

    all_words = list(set(all_words))  # make unique

    print(all_words)

    ### ok, now we have the words, get the counts from the book
    book_text = open(BOOK, encoding=encoding).read()

    word_counts = []
    for word in all_words:
        count = book_text.count(word)
        word_counts.append((word, count))

    words_sorted = sorted(word_counts, key=itemgetter(1))

    for w in words_sorted:
        if w[1] <= MIN_NUM * 3:
            print(w)

    dw = dict(words_sorted)

    # pickle.dump(dw, open('freq_' + INFILE + '.pickle', 'wb'))
    pickle.dump(dw, open(INFILE + '.pickle', 'wb'))

def main():
    source_datasets_hp = "hp"
    source_datasets_asoif = "asoif"

    if len(sys.argv) < 2:
        raise Exception("Usage: preprocessing.py {lem|nolem} [ngram]")
    if sys.argv[1].lower() == "lem":
        source_book_hp = "../hp_processed_lem.txt"
        source_book_asoif = "../asoif_processed_lem.txt"
        if len(sys.argv) == 3:
            source_book_hp = "../hp_processed_lem_ngram.txt"
            source_book_asoif = "../asoif_processed_lem_ngram.txt"
    else:
        source_book_hp = "../hp_processed.txt"
        source_book_asoif = "../asoif_processed.txt"
        if len(sys.argv) == 3:
            source_book_hp = "../hp_processed_ngram.txt"
            source_book_asoif = "../asoif_processed_ngram.txt"

    print("\n\tHarry Potter\n")
    check_frequencies(source_datasets_hp, source_book_hp, DEFAULT_ENCODING)
    print("\n\n\tA Song of Ice and Fire\n")
    check_frequencies(source_datasets_asoif, source_book_asoif, DEFAULT_ENCODING)

if __name__ == "__main__":
    main()