import sys
from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
from gensim.models import FastText


def save_model(model, path):
    model.wv.save_word2vec_format(path)


def train_model_w2v(sentences, arg):
    if arg == 'w':
        return Word2Vec(sentences)
    elif arg == 'w1':
        return Word2Vec(sentences, size=300, negative=0, sg=1, hs=1, iter=15)
    elif arg == 'w2':
        return Word2Vec(sentences, size=300, negative=0, sg=1, hs=1, iter=15, window=12)
    elif arg == 'w3':
        return Word2Vec(sentences, size=300, negative=15, sg=1, hs=1, iter=15, window=12)
    elif arg == 'w4':
        return Word2Vec(sentences, size=300, negative=0, sg=0, hs=1, iter=15)
    else:
        raise Exception("Please choose: w{1,2,3,4}")


def train_model_ft(sentences, arg):
    if arg == 'f':
        return FastText(sentences)
    elif arg == 'f1':
        return FastText(sentences, sg=1, hs=1, size=300, iter=15, window=12, negative=0)
    elif arg == 'f2':
        return FastText(sentences, sg=1, hs=1, size=300, iter=15, window=12, negative=15)
    else:
        raise Exception("Please choose: f{1,2}")


def get_book_name(arg):
    if arg not in ["asoif", "hp"]:
        raise Exception("The book series must be either *ASOIF* or *HP*")
    return arg


def get_model(model_type, sentences, method_type):
    if model_type == 'w':
        return train_model_w2v(sentences, method_type)
    elif model_type == 'f':
        return train_model_ft(sentences, method_type)
    else:
        raise Exception("Please choose w2v or ft")


def main():
    if len(sys.argv) < 3:
        raise Exception("We need three command line arguments: create_model.py book model")
    book = get_book_name(sys.argv[1].lower())
    sentences = LineSentence(book + "_processed.txt")

    model_arg = sys.argv[2].lower()
    model = get_model(model_arg[0], sentences, model_arg)

    model_name = book + "_" + model_arg + ".model"
    print("Model " + model_name + " created")

    path = "models/" + model_name
    save_model(model, path)
    print("Model saved to path " + path)

    print("Unique words count:")
    print(len(model.wv.vocab))


if __name__ == "__main__":
    main()
