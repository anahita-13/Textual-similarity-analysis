# Textual-similarity-analysis

My professor had a dataset that contained the title and abstract texts of a set of 100 patent documents (or corpus). He asked me to provide him with some information about the corpus and eventually calculate pair-wise similarity between all patent documents. 

Firstly, I provided him the list of the most commonly occurring words(or tokens)in it. Further, I identified if these most common keywords were relevant and added  value/meaning to the documents. As many tokens were stop words which did not add any value, I cleaned the corpus to obtain a set of relevant keywords for further analysis on it. Furthermore, I used TF-IDF vectors to work with textual data and eventually calculated the textual similarity between any two patent documents numerically in this corpus.

Conclusion: I calculated pairwise cosine similarity of 100 patent documents. I used natural language processing techniques to tokenize data in the corpus, remove stop words and create TF-IDF (Term frequency–inverse document frequency) vectors of text and finally calculated the similarity matrix.

Summary: Summary is contained in the file [Summary.docx](https://github.com/anahita-13/Textual-similarity-analysis/blob/main/Summary.docx) and solution code is in the [A2.py](https://github.com/anahita-13/Textual-similarity-analysis/blob/main/A2.py) file. The [A2.ipynb](https://github.com/anahita-13/Textual-similarity-analysis/blob/main/A2.ipynb) file is the Jupyter notebook associated with the solution code and its execution line by line. [A2.pdf](https://github.com/anahita-13/Textual-similarity-analysis/blob/main/A2.pdf) is the pdf version of the same. 

The pairwise cosine similarities have been calculated and dumped in the csv file named [Cosine_similarity_scores.csv](https://github.com/anahita-13/Textual-similarity-analysis/blob/main/Cosine_similarity_scores.csv) 
