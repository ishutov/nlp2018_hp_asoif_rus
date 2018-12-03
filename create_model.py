import gensim
from gensim.models.word2vec import LineSentence

INPUT_FILE = "HP_processed.txt"
OUTPUT_FILE = "models/hp.model"


def train_model(sentences):
    return gensim.models.Word2Vec(sentences, min_count=5, size=300, workers=4, window=10, sg=1, negative=5)


def save_model(model, path):
    model.wv.save_word2vec_format(path)


def main():
    sentences = LineSentence(INPUT_FILE)
    model = train_model(sentences)
    print("Model created")
    save_model(model, OUTPUT_FILE)
    print("Model saved to " + OUTPUT_FILE)
    print("Unique words count:")
    print(len(model.wv.vocab))

if __name__ == "__main__":
    main()