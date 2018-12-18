from __future__ import print_function

from datetime import datetime

import gensim.models

from config import *


def load_models(mode=None, embedding_serialization=None):
    if embedding_serialization == "vec":
        binary = False
    elif embedding_serialization == "bin":
        binary = True
    else:
        raise Exception()

    print('\n\n**** Model:', mode, " binary?:", binary)

    if mode == "doc2vec":
        word_model = gensim.models.doc2vec.Doc2Vec.load(MODEL_PATH + mode + ".model")
    else:
        word_model = gensim.models.KeyedVectors.load_word2vec_format(MODEL_PATH + mode + ".model", binary=binary)

    word_model.init_sims(replace=True)  # clean up RAM

    print("**** Model:", mode, " LOADED\n\n")

    return word_model


def print_details(task_res, msg):
    print("\n" + msg)
    for res in task_res:
        print("Task: %s -- Found: %s -- Correct: %s\n" % (res[0], res[1], res[2]))


def print_latex_version(results, method, FILTER_SECTIONS):
    """
        create a latex version of the results dictionary
        --> for easy updates of publication data
    """
    vals, counts = [], []
    for sec in FILTER_SECTIONS:
        data = results[sec]

        vals.append(str(round(data['perc'] * 100, 2)))
        counts.append(str(data['counts']))

    print('Number of tasks:       &', " & ".join(counts), " \\\\ \hline ")
    print(method, "               & ", " & ".join(vals), " \\\\ ")
    with open("./evaluation_result.txt", "a", encoding='utf-8') as f_out:
        f_out.write('Number of tasks: \t' + " & ".join(counts) + " \n")
        f_out.write(datetime.strftime(datetime.now(), "%d.%m %H:%M  ") + method + "\t  & " + " & ".join(vals) + " \n")


if __name__ == "__main__":
    model = load_models(mode='asoif_w2v-default', embedding_serialization='bin')
    print('\n\nMODEL', model)
