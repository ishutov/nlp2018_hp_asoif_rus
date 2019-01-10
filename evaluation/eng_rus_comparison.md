# "Analogies" and "Doesn't match" evaluation comparison between English and Lemmatized Russian 

## Analogies evaluation

### HP

| **Model** | **English (total 4736)** | **Lemmatized Russian (total 2832)** |
|:----------|:-------------------------|:-------------------------|
| **w**     | 7.99 | 3.64 |
| **w1**    | 25.55 | 27.37 |
| **w2**    | 28.19 | 28.43 |
| **w3**    | 32.22 | 26.62 |
| **w4**    | 6.27 | 4.63 |
| **f**     | 0.8 | 0.95 |
| **f1**    | 24.51 | 24.93 |
| **f2**    | 27.34 | 25.88 |

### ASOIF

| **Model** | **English (total 2848)** | **Lemmatized Russian (total 2234)** |
|:----------|:-------------------------|:-------------------------|
| **w**     | 6.81 | 1.88 |
| **w1**    | 26.72 | 22.56 |
| **w2**    | 38.41 | 28.02 |
| **w3**    | 38.55 | 29.23 |
| **w4**    | 2.25 | 1.34 |
| **f**     | 1.12 | 2.6 |
| **f1**    | 28.79 | 26.32 |
| **f2**    | 32.16 | 27.08 |

## Doesn't match evaluation

### HP

| **Model** | **English (total 8420)** | **Lemmatized Russian (total 8340)** |
|:----------|:-------------------------|:-------------------------|
| **w**     | 65.78 | 52.96 |
| **w1**    | 71.57 | 61.95  |
| **w2**    | 68.06 | 61.64  |
| **w3**    | 67.53 | 60.59  |
| **w4**    | 59.06 | 51.12 |
| **f**     | 56.22 | 54.23 |
| **f1**    | 70.4 |  61.76 |
| **f2**    | 69.13 |  61.87 |

### ASOIF

| **Model** | **English (total 11180)** | **Lemmatized Russian (total 11180)** |
|:----------|:-------------------------|:-------------------------|
| **w**     | 86.6 | 74.17 |
| **w1**    | 77.05 | 68.18 |
| **w2**    | 74.36 | 68.15 |
| **w3**    | 72.74 | 67.1 |
| **w4**    | 77.12 | 73.43 |
| **f**     | 73.02 | 72.65 |
| **f1**    | 75.11 | 68.8 |
| **f2**    | 73.97 | 66.52 |

***
## Differences analysis

Russian measurements are similar to English. For HP books Russian values are just a bit lower (~2-3%), and for ASOIF values differ more (~8%). 
It is important to mention that russian books were processed after lemmatization - the [results are much lower](https://github.com/ishutov/nlp2018_hp_asoif_rus/blob/master/evaluation/comparison_evaluation.md) without it

We propose that the possible reasons of such results (russian values are lower even being lemmatized) are the following:

- The various forms of words in russian language. For example, the word "bronze" can be translated to multiple forms depends on context (бронза/бронзовый/бронзовых). This issue supposed to be solved by lemmatization, but it caused some other problems (below)
- Not "clear" lemmatization process. It's hard for lemmatization to detect international named entities, which can be also similar to some russian words. For example, a Fluffy from HP was translated as "Пушок". But there is a word "пушка" (a gun) in russian, so lemmatizator made a mistake
- Various synonims in Russian. For example, "intelligence" can be translated as "ум", "интеллект", "осознание", "остроумие" and so on. 
- "е" and "ё" letters in Russian.
- Phonetic issues - there are no "ae" phonetic sound in Russian, so it can be transformed to multiple letters: "а","е","э"
- Translators are using not popular words in fictions to reach more emotional contrast in the book. (ex. "честолюбие")
