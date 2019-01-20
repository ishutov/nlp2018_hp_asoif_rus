# Books

### Harry Potter
>[**Антология Гарри Поттера** (Harry Potter anthology)](http://rosmean.ru//)
>
> Росмэн
> 1. Гарри Поттер и философский камень [ёфицировано] (пер. Оранский, Игорь В.) 283 с.
> 2. Гарри Поттер и Тайная комната (пер. Литвинова, Марина Дмитриевна) 254 с. 
> 3. Гарри Поттер и узник Азкабана (пер. Литвинова, Марина Дмитриевна) 309 с.
> 4. Гарри Поттер и Кубок огня (пер. Литвинова, Марина Дмитриевна) 526 с.
> 5. Гарри Поттер и Орден Феникса (пер. Голышев, Виктор Петрович et al.) 748 с.
> 6. Гарри Поттер и Принц-полукровка (пер. Ильин, Сергей Борисович) 523 с.
> 7. Гарри Поттер и Дары Смерти (пер. Ильин, Сергей Борисович et al.) 593 с.

### A song of ice and fire
>[**Игра престолов** (A Game of Thrones)](https://www.flip.kz/catalog?prod=5137)
>
>пер. Соколов, Юрий Ростиславович

>[**Битва королей** (A Clash of Kings)](https://www.flip.kz/catalog?prod=16682)
>
>пер. Виленская, Наталья И.

>[**Буря мечей** (A Storm of Swords)](https://www.flip.kz/catalog?prod=5147)
>
>пер. Виленская, Наталья И.

>[**Пир стервятников** (A Feast for Crows)](https://www.flip.kz/catalog?prod=253506)
>
>пер. Виленская, Наталья И.

# Results 

### Analogies evaluation for uni-gram English, Russian, Russian lemmatized
<table>
<tr><th>HP</th><th>ASOIF</th></tr>
<tr><td>

| **Model** | **English (total 4736)** | **Russian (total 4120)** |**Russian Lemmatized (total 2832)** |
|:----------|:-------------------------|:---------------------|:-------------------------|
| **w**     | 7.99 | 0.95| 3.64 |
| **w1**    | 25.55 |19.81 | 27.37 |
| **w2**    | 28.19 | 25.29| 28.43 |
| **w3**    | 32.22 | 17.11| 21.08 |
| **w4**    | 6.27 | 1.99| 4.63 |
| **f**     | 0.8 | 0.41| 0.95 |
| **f1**    | 24.51 | 9.27| 24.93 |
| **f2**    | 27.34 | 4.39| 17.02 |
    
</td><td>

| **English (total 2848)** | **Russian (total 2492)**| **Russian Lemmatized (total 2234)** |
|:-------------- |:-------------------------|:-------------------------|
|6.81 | 1.4| 1.88 |
|26.72 | 15.89| 22.56 |
| 38.41 | 22.67| 28.02 |
|38.55 | 19.74| 22.07 |
| 2.25 | 0.96| 1.34 |
| 1.12 | 0.44| 2.6 |
| 28.79 | 9.59| 26.32 |
| 32.16 | 1.12|17.46 |

</td></tr> </table>

### Doesn't match evaluation for uni-gram English, Russian, Russian lemmatized
<table>
<tr><th>HP</th><th>ASOIF</th></tr>
<tr><td>

| **Model** | **English (total 8420)** | **Russian (total 8340)** |**Russian Lemmatized (total 8340)** |
|:----------|:-------------------------|:---------------------|:-------------------------|
| **w**     | 65.78 | 34.88| 52.96 |
| **w1**    | 71.57 |61.4 | 61.95 |
| **w2**    | 68.06 | 62.4| 61.64 |
| **w3**    | 67.53 | 58.19| 63.84 |
| **w4**    | 59.06 | 47.42| 51.12 |
| **f**     | 56.22 | 47.39| 54.23 |
| **f1**    | 70.4 | 62.11| 61.76 |
| **f2**    | 69.13 | 64.18| 65.29 |
    
</td><td>

| **English (total 11180)** | **Russian (total 11180)**| **Russian Lemmatized (total 11180)** |
|:-------------- |:-------------------------|:-------------------------|
|86.6 | 62.45| 74.17 |
|77.05| 66.67| 68.18 |
| 74.36 | 66.58| 68.15 |
|72.74 | 69.41| 70.39 |
| 77.12 | 63.84| 73.43 |
| 73.02 | 63.0| 72.65 |
| 75.11 | 66.85| 68.8 |
| 73.97 | 70.67| 71.14 |

</td></tr> </table>

***

### Analogies evaluation for n-gram Russian, Russian lemmatized
<table>
<tr><th>HP</th><th>ASOIF</th></tr>
<tr><td>

| **Model** | **Russian** |**Russian Lemmatized** |
|:----------|:---------------------|:-------------------------|
| **w1**    | 0.0 | 6.82
| **w2**    | 2.08 | 4.55
| **f**     | 4.17 | 0.0
    
</td><td>

| **Model** | **Russian** |**Russian Lemmatized** |
|:----------|:---------------------|:-------------------------|
| **w1**    | 0.0 | 10.0
| **w2**    | 0.91 | 1.11
| **f**     | 0.0 | 0.0

</td></tr> </table>

### Doesn't match evaluation for n-gram Russian, Russian lemmatized
<table>
<tr><th>HP</th><th>ASOIF</th></tr>
<tr><td>

| **Model** | **Russian** |**Russian Lemmatized** |
|:----------|:---------------------|:-------------------------|
| **w1**    | 67.76 | 75.52
| **w2**    | 58.49 | 74.38
| **f**     | 63.44 | 73.44
    
</td><td>

| **Model** | **Russian** |**Russian Lemmatized** |
|:----------|:---------------------|:-------------------------|
| **w1**    | 65.3 | 69.6
| **w2**    | 65.8 | 70.05
| **f**     | 62.85 | 69.15

</td></tr> </table>

***

### Average words' frequencies 

#### Uni-gram
<table>
<tr><th>HP</th><th>ASOIF</th></tr>
<tr><td>

|  | **English** |**Russian** |**Russian Lemmatized** |
|:----------|:---------------------|:-------------------------|:-------------------------|
| **Average frequencies**    | 404 | 324.14 | 345.63
| **Amount of words < 5**    | 6 | 22 | 29
    
</td><td>

|  | **English** |**Russian** |**Russian Lemmatized** |
|:----------|:---------------------|:-------------------------|:-------------------------|
| **Average frequencies**    | 349 | 332.19 | 326.97
| **Amount of words < 5**    | 1 | 7 | 16
    
</td></tr> </table>

#### N-gram
<table>
<tr><th>HP</th><th>ASOIF</th></tr>
<tr><td>

|  | **English** |**Russian** |**Russian Lemmatized** |
|:----------|:---------------------|:-------------------------|:-------------------------|
| **Average frequencies**    | 456.64 | 400.14 | 422.47
| **Amount of words < 5**    | 5 | 24 | 56
    
</td><td>

|  | **English** |**Russian** |**Russian Lemmatized** |
|:----------|:---------------------|:-------------------------|:-------------------------|
| **Average frequencies**    | 276.62 | 236.19 | 258.57
| **Amount of words < 5**    | 6 | 30 | 59
    
</td></tr> </table>

[More stats for analogies and doesn't match evaluation](/evaluation/comparison_evaluation.md) 

[Comparison of evaluation between English and Russian](/evaluation/eng_rus_comparison.md) 

[Frequencies comparison between English and Russian](/evaluation/frequencies_comparison.md) 

[Wikipedia evaluation](/evaluation/wiki_evaluation.md) 

[Average frequencies for English and Russian](/evaluation/avg_frequencies_comparison.md) 


# Differences analysis

Russian measurements are similar to English. For HP books Russian values are just a bit lower (~2-3%), and for ASOIF values differ more (~8%). It is important to mention that russian books were processed after lemmatization - the results are much lower without it

We propose that the possible reasons of such results (russian values are lower even being lemmatized) are the following:

- The various forms of words in russian language. For example, the word "bronze" can be translated to multiple forms depends on context (бронза/бронзовый/бронзовых). This issue supposed to be solved by lemmatization, but it caused some other problems (below)
- Not "clear" lemmatization process. It's hard for lemmatization to detect international named entities, which can be also similar to some russian words. For example, a Fluffy from HP was translated as "Пушок". But there is a word "пушка" (a gun) in russian, so lemmatizator made a mistake
- Various synonims in Russian. For example, "intelligence" can be translated as "ум", "интеллект", "осознание", "остроумие" and so on.
- "е" and "ё" letters in Russian.
- Phonetic issues - there are no "ae" phonetic sound in Russian, so it can be transformed to multiple letters: "а","е","э"
- Translators are using not popular words in fictions to reach more emotional contrast in the book. (ex. "честолюбие")
