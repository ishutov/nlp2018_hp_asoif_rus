# Russian Language Datasets in the Digitial Humanities Domain and Their Evaluation with Word Embeddings

### Goals
- Russian language evaluation of basic ASOIF (A Song of Ice and Fire by GRR Martin) and HP (Harry Potter by JK Rowling) datasets.
- Research language evaluation for uni-grams/n-grams, with/without lemmatisation 
- Compare and analyse results for English and Russian translations

### Dependencies:

- `gensim-2-1-0 (or higher)`
- `pandas`
- `nltk`

### Summary
Here you find the following:
- 4 datasets (for uni-grams & n-grams) each for evaluating language models about the books **A Song of Ice and Fire** by GRR Martin and **Harry Potter** by JK Rowling _in translations for Russian language_
- The datasets contain a large of number of task of type **analogy** and **doesnt-match**.
- Your model can be tested easily, esp. if you can load it with [Gensim](https://radimrehurek.com/gensim).
- Furthermore, here you find scripts to create / extend the datasets -- by creating permutations of input data.
- Finally, you can re-use the scripts to evaluate the data.

### Preprocessing
If you want to do some preprocessing for your source books, you can easily run the following:
```
    python preprocessing.py {hp|asoif} [lem]
```
where `{hp|asoif}` is the book you want to preprocess and `lem` is an optional argument, if you want to try with lemmatization.
After preprocessing you'll have two output files transformed to `one sentence - one line` format with no punctuation

## The Datasets
The datasets can be found in the folder [datasets](datasets).
Like in the original word2vec-toolkit, the files to be evaluated are named `questions`\*.
There are four datasets for **uni-gram** data:
- `datasets/questions_asoif_analogies.txt`: Analogies relation test data for *A Song of Ice and Fire* in Russian translation
- `datasets/questions_asoif_doesnt_match.txt`: Doesnt_match task test data for *A Song of Ice and Fire* in Russian translation
- `datasets/questions_hp_analogies.txt`: Analogies relation test data for *Harry Potter* in Russian translation
- `datasets/questions_hp_doesnt_match.txt`: Doesnt_match task test data for *Harry Potter* in Russian translation

And 4 more datasets, same as the 4 original ones, but for **n-gram** data located in `datasets/ngram/`

If you want to extend or modify the test data, edit the respective source files in the folder [datasets](datasets):
`hp_analogies.txt`, `hp_doesnt_match.txt`, `asoif_analogies.txt`,`asoif_doesnt_match.txt`.
To extend or modify the test n-gram data, edit the same respective source files with `_ngram` in the folder [ngram](datasets/ngram).

After modifying the test data run the following command to re-create the datasets (the `question_` files).
```
    cd datasets 
    python create_questions.py [ngram]
```

This will generate section-based permutations to create the evaluation datasets. 
If you want to proceed with `ngram` datasets, please add `ngram` option
You can also add completly new datasets and add a line into `create_questions.py`.

## The Models
To evaluate the datasets you need language models, examples of which are provided in the folder [models](models)
(or you can use your own strategies).

We used different well-known techniques to create word-embedding models, for example word2vec, GloVe, fastText, and LexVec. 
The models having names staring with `asoif_` are trained on the first for books of *A Song of Ice and Fire*,
and the models starting with `hp_` are trained on the complete *Harry Potter*. For copyright reasons the plain-text of
the books can not be included here.

To generate models use next command in console: `python create_model.py {hp|asoif} {w|w1|w2|w3|w4|f|f1|f2} [ngram]` (Please note, for `ngram` only `{w1|w2|f}` modes are supported)

Next setups for models are in use for current project:
#### For uni-grams:
- Word2Vec:
    - **w**: size=100, window=5, min_count=5, sample=0.001, sg=0, hs=0, negative=5, iter=5,
    - **w1**:  size=300, -negative=0, sg=1, hs=1, iter=15
    - **w2**:  size=300, -negative=0, sg=1, hs=1, iter=15, window=12
    - **w3**:  size=300, -negative=15, sg=1, hs=0, iter=15, window=12
    - **w4**:  size=300, -negative=0, sg=0, hs=1, iter=15
- FastText:
    - **f**: sg=0, hs=0, size=100, window=5, negative=5, iter=5
    - **f1**:  sg=1, hs=1, size=300, iter=15, window=12, negative=0
    - **f2**:  sg=1, hs=0, size=300, iter=15, window=12, negative=15
#### For n-grams:
- Word2Vec:
    - **w1**: size=300, negative=0, sg=1, hs=1, iter=15, window=12
    - **w2**: size=300, negative=15, sg=1, hs=1, iter=15, window=12
- FastText:
    - **f**: defaults, iter=25, window=12
    
## Frequencies evaluation
If you want to see frequencies statistics of your datasets (how many times each term in dataset appears in the books), 
you can do frequencies evaluation:
```
    cd datasets
    python check_frequencies.py {lem|nolem} [ngram]
```
choose `lem` option, if you want to check on lemmatized version, otherwise put `nolem`
If you want to check ngrams, just add optional argument `ngram`

## Doing the evalation

Choose the book series you want to evaluate (`asoif` or `hp`), and the task type you want to
do, analogy or doesnt_match. Call the scripts as shown below.
In `config.py` you can switch from uni-gram (default) to n-gram datasets. For evaluation n-gram datasets
set `NGRAMS=True`. For evaluation lemmatized version set `LEMMATIZATION=True`

#### Analogies task
```
    cd src
    python analogies_evaluation.py asoif        # to eval A Song of Ice and Fire book series
    python analogies_evaluation.py hp           # to eval Harry Potter book series
```

#### Doesnt_match task
```
    cd src
    python doesnt_match_evaluation.py hp        # to eval Harry Potter book series
    python doesnt_match_evaluation.py asoif     # to eval A Song of Ice and Fire book series

```

The output of the scripts will be various counts (how many tasks per section, how many correctly and incorrectly solved,
and the percentage (**accuracy**) of correct suggestions).

## For adding new dataset or models
We tried to make the system **easily extendable** to evaluate new models.

* Adding models: just put them into the [models](models) folder, and add them into the `METHODS` variable in `config.py`. 
* Adding new datasets and models: add the raw dataset into [datasets](datasets), generate the `questions` with `create_questions.py`. 
Add a new section to `config.py` with the settings for the new dataset. 
  
## Results
For more information about results of this project, see [Results.md](Results.md)

Evaluation results of the Russian books and datasets are a bit lower than for English, but still quite similar. 
Generally, this difference might be mainly explained by various forms of words in Russian (Russian morphology). 

We've attacked this problem by lemmatization of the Russian books, and the results became better - 
the difference between English and Russian evaluation results was reduced.

The results could still be better, as the lemmatization process is done according to the Russian language rules -- 
and some English words (specially, named entities) -- were lemmatized wrongly, which leads to decreasing total results. 
If such words are excluded during lemmatization, the results will be higher. 
The full analysis can be found [here -- Results.md](Results.md#differences-analysis)
