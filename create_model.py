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
    if arg == "asoif" or arg == "hp":
        return arg
    else:
        raise Exception("The book series must be either *ASOIF* or *HP*")


def main():
    if len(sys.argv) < 3:
        raise Exception("We need three command line arguments: create_model.py book model")
    else:
        book = get_book_name(sys.argv[1].lower())
        sentences = LineSentence(book + "_processed.txt")

        model_arg = sys.argv[2].lower()
        if model_arg[0] == 'w':
            model = train_model_w2v(sentences, model_arg)
        elif model_arg[0] == 'f':
            model = train_model_ft(sentences, model_arg)
        else:
            raise Exception("Please choose w2v or ft")

        model_name = book + "_" + model_arg + ".model"
        print("Model " + model_name + " created")

        if model_arg[0] == 'w':
            save_model(model, "models/" + model_name)
        elif model_arg[0] == 'f':
            save_model(model, "models/" + model_name)   # todo - how to save FastText model?

        print("Unique words count:")
        print(len(model.wv.vocab))


if __name__ == "__main__":
    main()
