# nlp2018_hp_asoif_rus
Russian language evaluation of basic ASOIF and HP datasets.

_Currently on step 19.M2_

### How to?
1. Generate models with next command in console: `python create_model.py {hp|asoif} {w|w1|w2|w3|w4|f|f1|f2}`
- Word2Vec:
    - **w**: size=100, window=5, min_count=5, sample=0.001, sg=0, hs=0, negative=5, iter=5,
    - **w1**:  size=300, -negative=0, sg=1, hs=1, iter=15
    - **w2**:  size=300, -negative=0, sg=1, hs=1, iter=15, window=12
    - **w3**:  size=300, -negative=15, sg=1, hs=1, iter=15, window=12
    - **w4**:  size=300, -negative=0, sg=0, hs=1, iter=15
- FastText:
    - **f**: sg=0, hs=0, size=100, window=5, negative=5, iter=5
    - **f1**:  sg=1, hs=1, size=300, iter=15, window=12, negative=0
    - **f2**:  sg=1, hs=1, size=300, iter=15, window=12, negative=15

***
#### N-grams:
- Word2Vec:
    - **w1**: size=300, negative=0, sg=1, hs=1, iter=15, window=12
    - **w2**: size=300, negative=15, sg=1, hs=1, iter=15, window=12
- FastText:
    - **f**: defaults, iter=25, window=12

2. Check frequencies with `./datasets/check_frequencies.py`
3. Create questions with `./datasets/create_questions.py`
4. Run next commands in console:
- For HP:
  - `python analogies_evaluation.py hp`
  - `python doesnt_match_evaluation.py hp`
- For ASOIF:
  - `python analogies_evaluation.py asoif`
  - `python doesnt_match_evaluation.py asoif`
  
