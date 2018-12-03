# nlp2018_hp_asoif_rus
Russian language evaluation of basic ASOIF and HP datasets.

### How to?
1. Generate models with `create_model.py` for HP and ASOIF
2. Check frequencies with `./dataset/check_frequencies.py`
3. Create questions with `./dataset/create_questions.py`
4. Run next commands in console:
- For HP:
  - `python analogies_evaluation.py hp`
  - `python doesnt_match_evaluation.py hp`
- For ASOIF:
  - `python analogies_evaluation.py asoif`
  - `python doesnt_match_evaluation.py asoif`
  
