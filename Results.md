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

[Analogies and doesn't match evaluation](/evaluation/comparison_evaluation.md) 

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
