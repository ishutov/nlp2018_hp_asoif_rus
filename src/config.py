"""
    This is the central config file
    @author: Gerhard Wohlgenannt (2017), ITMO University, St.Petersburg, Russia

    Here you can change pathes, add models, add new BOOK_SERIES, new dataset (towards the end of the file).
    But just to start with existing datasets and models, no change is needed
"""

import sys

# NGRAMS = False
NGRAMS=True

## this sets if we do evaluation based on term frequency (new) in doesnt_match evaluation
## for this you might need the book corpora to recompute the frequencies
## that is why we made this feature optional
DO_FREQ_EVAL = True
# DO_FREQ_EVAL=False

## use the input parameter to select the book series
if len(sys.argv) < 2:
    raise Exception("We need two command line arguments!")
if sys.argv[1].lower() == 'asoif':
    BOOK_SERIES = "ASOIF"
elif sys.argv[1].lower() == 'hp':
    BOOK_SERIES = "HP"
elif sys.argv[1].lower() == 'sh':
    BOOK_SERIES = "SH"  ## new: Sherlock Holmes book

else:
    raise Exception("the book series must be either *ASOIF* or *HP* or *SH*")

MODEL_PATH = "../models/"

############## settings ###################################
############# BASH constructed models:
# w2v-default-bash:     ./word2vec -train $TEXT -output $VECTORS -cbow 0 -size 300 -window 5  -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 1
# w2v-w12-i15-bash:     ./word2vec -train $TEXT -output $VECTORS -cbow 0 -size 300 -window 12 -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 1 -iter 15
# w2v-w12-i15-ns-bash:  ./word2vec -train $TEXT -output $VECTORS -cbow 0 -size 300 -window 12 -negative 1 -hs 1 -sample 1e-4 -threads 12 -binary 1 -iter 15
# w2v-w12-cbow-bash:    ./word2vec -train $TEXT -output $VECTORS -cbow 1 -size 300 -window 12 -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 1 -iter 15

#
# fasttext-12-e25       ./fasttext skipgram -input "${DATADIR}"/$INFILE -output "${RESULTDIR}"/$OUTFILE -dim 300 -ws 12 -minCount 5 -thread 4 -epoch 25
#
# glove_w12             glove trained with: VOCAB_MIN_COUNT=5; VECTOR_SIZE=300; MAX_ITER=15; WINDOW_SIZE=12; BINARY=2
#
# lexvec-default        $DIR/im_lexvec.sh -corpus $CORPUS -dim 200 -iterations 15 -subsample 1e-4 -window 2  -model 1 -negative 25 -minfreq 5
# lexvec-w05            $DIR/im_lexvec.sh -corpus $CORPUS -dim 300 -iterations 15 -subsample 1e-4 -window 5  -model 1 -negative 25 -minfreq 5
# lexvec-w12            $DIR/im_lexvec.sh -corpus $CORPUS -dim 300 -iterations 15 -subsample 1e-4 -window 12 -model 1 -negative 25 -minfreq 5
#
# text8 models: computed with w2v-default-gensim and fasttext-12-e25 settings.
# wikipedia models: computed with w2v-default-gensim using gensim-data 2017 wikipedia. preprocessing: sentence-splitting, tokenize, clean
# pretrained fasttext wikipedia  https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md (english wikipedia)

if BOOK_SERIES == "ASOIF":
    METHODS = [
        # w2vec models
        ('lem_asoif_w', 'vec'),
        ('lem_asoif_w1', 'vec'),
        ('lem_asoif_w2', 'vec'),
        ('lem_asoif_w3', 'vec'),
        ('lem_asoif_w4', 'vec'),
        # fastText models
        ('lem_asoif_f', 'vec'),
        ('lem_asoif_f1', 'vec'),
        ('lem_asoif_f2', 'vec'),
        # ('ruwikiruscorpora_upos_skipgram_300_2_2018.vec', 'vec'),
        # ('wiki.ru.vec', 'vec'),
    ]

    if NGRAMS:
        METHODS = [
            ('ngram_lem_asoif_w1', 'vec'),
            ## Skip-gram, window-size 12, 300dim, hier.softmax, iter 15, no neg-sampling
            ('ngram_lem_asoif_w2', 'vec'),
            ## Skip-gram, window-size 12, 300dim, hier.softmax, iter 15, -negative 15
            ('ngram_lem_asoif_f', 'vec'),  # default and: -epoch 25 -ws 12
        ]

if BOOK_SERIES == "HP":
    METHODS = [
        # w2vec models
        ('lem_hp_w', 'vec'),
        ('lem_hp_w1', 'vec'),
        ('lem_hp_w2', 'vec'),
        ('lem_hp_w3', 'vec'),
        ('lem_hp_w4', 'vec'),
        # fastText models
        ('lem_hp_f', 'vec'),
        ('lem_hp_f1', 'vec'),
        ('lem_hp_f2', 'vec'),
        # ('ruwikiruscorpora_upos_skipgram_300_2_2018.vec', 'vec'),
        # ('wiki.ru.vec', 'vec'),
    ]

    if NGRAMS:
        METHODS = [
            ('ngram_lem_hp_w1', 'vec'),
            ('ngram_lem_hp_w2', 'vec'),
            ('ngram_lem_hp_f', 'vec'),  # for paper!, 25 epoch
        ]

# -----------------------------------------------------
# for "doesnt_match" evaluation script
# -----------------------------------------------------

if BOOK_SERIES == "ASOIF":
    PRINT_DETAILS = False  ## verbose debugging of eval results

    if NGRAMS:
        ANALOGIES_FILE = "../datasets/ngram/questions_asoif_analogies_ngram.txt"
        DOESNT_MATCH_FILE = "../datasets/ngram/questions_asoif_doesnt_match_ngram.txt"
        ANALOGIES_SECTIONS = ['name-nickname', 'child-father', 'total']
        DOESNT_MATCH_SECTIONS = [': bays', ': gods', ': cities-fortresses', ': Maesters', ': Houses', 'TOTAL']
        FREQ_FILE = "../datasets/ngram/asoif.pickle"

    else:
        ANALOGIES_FILE = "../datasets/questions_asoif_analogies.txt"
        DOESNT_MATCH_FILE = "../datasets/questions_asoif_doesnt_match.txt"
        ANALOGIES_SECTIONS = ['firstname-lastname', 'child-father', 'husband-wife', 'geo-name-location', 'houses-seats',
                              'total']
        DOESNT_MATCH_SECTIONS = [': family-siblings', ': names-of-houses', ': Stark clan', ': free cities', 'TOTAL']
        FREQ_FILE = "../datasets/freq_asoif.pickle"

if BOOK_SERIES == "HP":
    PRINT_DETAILS = False  ## verbose debugging of eval results

    if NGRAMS:
        ANALOGIES_FILE = "../datasets/ngram/questions_hp_analogies_ngram.txt"
        DOESNT_MATCH_FILE = "../datasets/ngram/questions_hp_doesnt_match_ngram.txt"
        # ANALOGIES_SECTIONS = ['Gryffindor-Quidditch-team', 'Yule_ball-gentleman-lady', 'character-where_they_work', 'character-creature', 'total']
        ANALOGIES_SECTIONS = ['character-creature', 'character-where_they_work', 'total']
        # DOESNT_MATCH_SECTIONS = [': geographical-objects', ': closest-friends', ': unforgivable-curses', ': members-of-Order_of_the_Phoenix', ': ministers-for-magic', 'TOTAL']
        DOESNT_MATCH_SECTIONS = [': geographical-objects', ': ministry_of_magic-employees',
                                 ': members-of-Order_of_the_Phoenix', 'TOTAL']
        FREQ_FILE = "../datasets/ngram/hp.pickle"
    else:
        ANALOGIES_FILE = "../datasets/questions_hp_analogies.txt"
        DOESNT_MATCH_FILE = "../datasets/questions_hp_doesnt_match.txt"
        ANALOGIES_SECTIONS = ['firstname-lastname', 'child-father', 'husband-wife', 'name-species', 'total']
        # DOESNT_MATCH_SECTIONS = [': family-members', ': Gryffindor-members', ': magic-creatures', ': wizards-animagi', 'TOTAL']
        DOESNT_MATCH_SECTIONS = [': family-members', ': Gryffindor-members', ': magic-creatures', ': professors',
                                 'TOTAL']
        FREQ_FILE = "../datasets/freq_hp.pickle"
