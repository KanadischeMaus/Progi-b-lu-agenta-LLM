# Pakiet do zewnętrznej weryfikacji (Perplexity)

> Stan na 13.11.2026. Narzędzie, które przygotowało pakiet: aplikacja Claude (projekt), model claude-fable-5-2.

## Zakres

19 pozycji w 4 paczkach:

- 2 pozycje nowe: `agresti2013categorical`, `kleijnen2015design`;
- 9 pozycji ze statusem K, które zostają w wyborze: `russell2020artificial`, `sutton2018reinforcement`, `kingdom2016psychophysics`, `maslow1943theory`, `tversky1981framing`, `vaswani2017attention`, `brown2020language`, `ouyang2022training`, `wei2022chain`;
- 1 pozycja ze statusem „?” w wyborze: `sharma2024towards`;
- 7 preprintów z wyboru: `keeling2024can`, `bianco2026beyond`, `masumori2025survival`, `tagliabue2025probing`, `li2023large`, `schulhoff2024prompt`, `qwen2024qwen25`.

Poza pakietem: pozostałe pozycje (metadane sprawdzane 27.09, 07.10 i w audycie 08.10) oraz pozycje rezerwowe i odłożone do usunięcia, także te ze statusem K (`yao2023react`, `shinn2023reflexion`, `park2023generative`) i „?” (`liu2024agentbench`).

Pakiet zawiera wyłącznie dane bibliograficzne z `literatura.bib` i jednozdaniowe twierdzenia. Nie ma w nim tekstu pracy.

## Jak używać

1. Do każdego zapytania wklej cały prompt, a pod nim jedną paczkę.
2. Odpowiedź o metadanych porównaj ze stroną, do której prowadzi podany odnośnik. Bez odnośnika do wydawcy odpowiedź się nie liczy.
3. Odpowiedź na pytanie 3 (gdzie jest twierdzenie) jest wskazówką do lektury, nie potwierdzeniem. Potwierdzenie daje dopiero notatka z lektury.
4. Zmiany w `literatura.bib` wynikające z odpowiedzi nanosi Claude Code, ze źródłem i datą w polu `weryfikacja`.

## Prompt (po angielsku, wklejany przed każdą paczką)

```text
You are checking bibliographic records for an academic thesis. For every item in the batch below, answer three questions. Use primary sources only: the publisher's page, the DOI landing page, ACL Anthology, PMLR, the NeurIPS proceedings site, OpenReview, arXiv, DBLP, or (for books) the publisher's catalogue page and a national-library or WorldCat record.

Q1. Does the publication exist with exactly the data given? Check every field: authors (complete list, order, spelling), title, venue (journal, proceedings, or publisher and place), year, volume, issue, pages, DOI or ISBN. List each field that differs and give the correct value. Where our author list ends with "et al.", give the complete author list.

Q2. Is this version peer-reviewed? Does a newer version or a peer-reviewed version exist (journal article, conference paper, later edition, later arXiv version)? If yes, give its full reference with DOI. For arXiv preprints, also report what the "Comments" and "Journal reference" fields on the arXiv abstract page say, and whether DBLP lists any entry for this work other than CoRR.

Q3. In which section does the publication make the statement given as "Claim"? Give the section number and title, and page numbers if you can see them. If the publication does not make this statement, or makes a narrower or different one, say so plainly.

Rules:
- Give a link to the primary-source page for every answer. A blog, a summary site, Wikipedia, ResearchGate or Semantic Scholar is not enough on its own.
- If you cannot confirm a field at a primary source, answer "I don't know" for that field. Do not guess and do not answer from memory.
- Do not rephrase the claim into something easier to confirm. If you can read the text, quote the supporting sentence (at most 25 words). If you cannot, answer "full text not accessible".
- Keep the item keys unchanged.

Output: one table per item, with rows Q1, Q2, Q3 and columns: answer | corrected value (if any) | source URL | status (confirmed at source / not confirmed).
```

## Paczka 1: książki (5)

```text
[agresti2013categorical]
Agresti, Alan. Categorical Data Analysis. 3rd edition. Hoboken, NJ: Wiley, 2013. ISBN 978-0-470-46363-5.
Claim: Section 1.4 presents the score confidence interval for a binomial proportion and names it the Wilson interval; chapter 5 covers logistic regression; section 8.1 covers baseline-category logit models for a nominal response with more than two categories.

[kleijnen2015design]
Kleijnen, Jack P. C. Design and Analysis of Simulation Experiments. 2nd edition. Cham: Springer, 2015. ISBN 978-3-319-18086-1. DOI 10.1007/978-3-319-18087-8.
Claim: Using common random numbers (the same seeds) across the compared conditions of a simulation experiment makes their outputs correlated, which allows the conditions to be compared pairwise.
Extra question: is the book open access or paid on the publisher's site, and is the place of publication Cham or New York?

[russell2020artificial]
Russell, Stuart; Norvig, Peter. Artificial Intelligence: A Modern Approach. 4th edition. Hoboken: Pearson, 2020. ISBN 978-0-13-461099-3.
Claim: An agent perceives its environment and selects actions; the book defines agent and environment.

[sutton2018reinforcement]
Sutton, Richard S.; Barto, Andrew G. Reinforcement Learning: An Introduction. 2nd edition. Cambridge, MA: MIT Press, 2018.
Claim: The book defines state, action, reward and policy for a reinforcement-learning agent.
Extra question: what is the ISBN of the 2nd edition, and is the full text legally free at the authors' site?

[kingdom2016psychophysics]
Kingdom, Frederick A. A.; Prins, Nicolaas. Psychophysics: A Practical Introduction. 2nd edition. London: Academic Press, 2016. ISBN 978-0-12-407156-8.
Claim: The book describes psychometric functions with threshold, slope, guess-rate and lapse-rate parameters, adaptive methods, and the comparison of conditions by model comparison (likelihood-ratio test).
Extra question: is the place of publication London or Amsterdam?
```

## Paczka 2: pozycje klasyczne (5)

```text
[maslow1943theory]
Maslow, Abraham H. A Theory of Human Motivation. Psychological Review, vol. 50, no. 4, pp. 370-396, 1943. DOI 10.1037/h0054346.
Claim: Human needs are ordered in a hierarchy, so that some needs take priority over others.

[tversky1981framing]
Tversky, Amos; Kahneman, Daniel. The Framing of Decisions and the Psychology of Choice. Science, vol. 211, no. 4481, pp. 453-458, 1981. DOI 10.1126/science.7455683.
Claim: Presenting the same decision problem in different ways changes people's choices (framing effect).

[vaswani2017attention]
Vaswani, Ashish; Shazeer, Noam; Parmar, Niki; Uszkoreit, Jakob; Jones, Llion; Gomez, Aidan N.; Kaiser, Łukasz; Polosukhin, Illia. Attention Is All You Need. Advances in Neural Information Processing Systems 30 (NeurIPS 2017), pp. 5998-6008, 2017.
Claim: The paper introduces the Transformer architecture, whose output is a probability distribution over the next token.

[brown2020language]
Brown, Tom B.; Mann, Benjamin; Ryder, Nick; Subbiah, Melanie; et al. Language Models are Few-Shot Learners. Advances in Neural Information Processing Systems 33 (NeurIPS 2020), pp. 1877-1901, 2020.
Claim: A large language model can perform a task from instructions and examples given in the prompt, without updating its weights (in-context learning).

[ouyang2022training]
Ouyang, Long; Wu, Jeff; Jiang, Xu; Almeida, Diogo; et al. Training Language Models to Follow Instructions with Human Feedback. Advances in Neural Information Processing Systems 35 (NeurIPS 2022), pp. 27730-27744, 2022.
Claim: Fine-tuning with human feedback makes a language model follow the instructions given in the prompt.
```

## Paczka 3: materiały konferencyjne i preprinty (5)

```text
[wei2022chain]
Wei, Jason; Wang, Xuezhi; Schuurmans, Dale; Bosma, Maarten; et al. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. Advances in Neural Information Processing Systems 35 (NeurIPS 2022), pp. 24824-24837, 2022.
Claim: A model can be made to generate a chain of intermediate reasoning steps before its final answer.

[sharma2024towards]
Sharma, Mrinank; et al. Towards Understanding Sycophancy in Language Models. International Conference on Learning Representations (ICLR 2024), 2024. OpenReview id: tvhaxkMKAn.
Claim: Language models tend to give in to opinions or suggestions that the user states in the prompt (sycophancy).
Extra question: give the complete author list exactly as on the OpenReview page.

[keeling2024can]
Keeling, Geoff; Street, Winnie; Stachaczyk, Martyna; Zakharova, Daria; Comsa, Iulia M.; Sakovych, Anastasiya; Logothetis, Isabella; Zhang, Zejia; Agüera y Arcas, Blaise; Birch, Jonathan. Can LLMs Make Trade-offs Involving Stipulated Pain and Pleasure States? arXiv:2411.02432v1, 2024. Preprint.
Claim: In a game that trades points against stipulated pain, some language models switch from maximising points to avoiding pain once the stipulated intensity passes a threshold, while others always avoid pain or respond gradually.

[bianco2026beyond]
Bianco, Francesca; Shiller, Derek. Beyond Behavioural Trade-Offs: Mechanistic Tracing of Pain-Pleasure Decisions in an LLM. arXiv:2602.19159v1, 2026. Preprint.
Claim: The study replicates the pain-pleasure trade-off paradigm of Keeling et al. and finds that the model's decisions depend on whether intensity is given as numbers or as verbal labels.

[masumori2025survival]
Masumori, Atsushi; Ikegami, Takashi. Do Large Language Model Agents Exhibit a Survival Instinct? An Empirical Study in a Sugarscape-Style Simulation. arXiv:2508.12920v1, 2025. Preprint.
Claim: LLM agents in a simulation with limited resources show survival-oriented behaviour.
```

## Paczka 4: preprinty (4)

```text
[tagliabue2025probing]
Tagliabue, Valen; Dung, Leonard. Probing the Preferences of a Language Model: Integrating Verbal and Behavioral Tests of AI Welfare. arXiv:2509.07961v2, 2025 (v2 dated 23 May 2026). Preprint.
Claim: A model's stated preferences do not have to agree with the choices it makes.

[li2023large]
Li, Cheng; Wang, Jindong; Zhang, Yixuan; Zhu, Kaijie; Hou, Wenxin; Lian, Jianxun; Luo, Fang; Yang, Qiang; Xie, Xing. Large Language Models Understand and Can Be Enhanced by Emotional Stimuli. arXiv:2307.11760v7, 2023. Preprint (technical report).
Claim: Adding emotional stimuli to a prompt changes the performance of large language models.
Extra question: the arXiv Comments field says a short version (v1) was accepted by LLM@IJCAI'23. Was that symposium peer-reviewed, and did it publish proceedings? If yes, give the reference of the short version.

[schulhoff2024prompt]
Schulhoff, Sander; Ilie, Michael; Balepur, Nishant; Kahadze, Konstantine; Liu, Amanda; Si, Chenglei; Li, Yinheng; Gupta, Aayush; Han, HyoJung; Schulhoff, Sevien; Dulepet, Pranav Sandeep; Vidyadhara, Saurav; Ki, Dayeon; Agrawal, Sweta; Pham, Chau Minh; Kroiz, Gerson C.; Li, Feileen; Tao, Hudson; Srivastava, Ashay; Da Costa, Hevander; Gupta, Saloni; Rogers, Megan L.; Goncearenco, Inna; Sarli, Giuseppe; Galynker, Igor; Peskoff, Denis; Carpuat, Marine; White, Jules; Anadkat, Shyamal; Hoyle, Alexander Miserlis; Resnik, Philip. The Prompt Report: A Systematic Survey of Prompt Engineering Techniques. arXiv:2406.06608v6, 2024 (v6 dated 26 February 2025). Preprint.
Claim: The survey defines a vocabulary for the components of a prompt, such as the role, the instruction and the output format.

[qwen2024qwen25]
Qwen Team. Qwen2.5 Technical Report. arXiv:2412.15115v2, 2024 (v2 dated 3 January 2025). Preprint (technical report).
Claim: The Qwen2.5 model family includes a model with 14 billion parameters.
Extra question: how does the paper itself name its authors (a team name or a list of individual authors)? Give the list exactly as on the first page.
```

## Co zrobić z odpowiedziami

| Wynik | Działanie |
|---|---|
| metadane zgodne, odnośnik do wydawcy podany i sprawdzony | status K albo „?” można podnieść do Z, ze źródłem i datą w polu `weryfikacja` |
| różnica w polu | sprawdzić u źródła z odnośnika; poprawkę nanosi Claude Code |
| „I don't know” albo brak odnośnika | status zostaje; pozycja wraca na listę „Do znalezienia lub decyzji” w docs/03 |
| znaleziona wersja recenzowana preprintu | sprawdzić u wydawcy; decyzja autora, czy cytować nową wersję (wtedy nowy klucz z rokiem tej wersji) |
| wskazana sekcja dla twierdzenia | wpisać do kolejki lektury jako wskazówkę; potwierdza dopiero notatka |
