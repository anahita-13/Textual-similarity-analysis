#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances

path='~/Desktop/Research Associate Assignment/Research-Aptitude-Test-Data/Q2_Dataset.xlsx'
df = pd.read_excel(path, dtype={'patentkey': int, 'text': str})

print(df.info())
print(df.text.head())

tokenizer = nltk.RegexpTokenizer(r"\w+")
df['tokenized_text'] = df.apply(lambda row: tokenizer.tokenize(row['text']), axis=1)
df['num_words'] = df.apply(lambda row: len(row['tokenized_text']), axis=1)
print(df.head())

df['friqDist'] = df.apply(lambda row: nltk.FreqDist(w.lower() for w in row['tokenized_text']), axis=1)
print(df.head())

nltk.download('stopwords') ##Run for first time download
stopwords = nltk.corpus.stopwords.words('english')

df['friqExceptStopDist'] = df.apply(lambda row: nltk.FreqDist(w.lower() for w in row['tokenized_text'] if w.lower() not in stopwords), axis=1)

print(df.head())

df['most_common'] = df.apply(lambda row: row['friqExceptStopDist'].most_common(10), axis=1)
print(df['most_common'].head())

df['text_cleaned'] = df.text.apply(lambda x: " ".join(re.sub(r'[^a-zA-Z]',' ',w).lower() for w in x.split() if re.sub(r'[^a-zA-Z]',' ',w).lower() not in stopwords) )

tfidfvectoriser = TfidfVectorizer()
tfidfvectoriser.fit(df.text_cleaned)
tfidf_vectors = tfidfvectoriser.transform(df.text_cleaned)

pairwise_similarities = np.dot(tfidf_vectors,tfidf_vectors.T).toarray()
pairwise_similarities_df = pd.DataFrame(pairwise_similarities)
pairwise_similarities_df.to_csv('~/Desktop/Research Associate Assignment/A2_cosine_similarity_scores.csv', index_label='patentkey')

def most_similar(patent_id, similarity_matrix, matrix):
    doc_id = df[df['patentkey'] == patent_id].index[0]
    print (f'Text: {df.iloc[doc_id]["text"]}')
    print ('\n')
    print ('Similar Text:')
    similar_ix = np.argsort(similarity_matrix[doc_id])[::-1]
    for ix in similar_ix:
        if ix == doc_id:
            continue
        print('\n')
        print (f'Patent Key: {df.iloc[ix]["patentkey"]}')
        print (f'Text: {df.iloc[ix]["text"]}')
        print (f'{matrix} : {similarity_matrix[doc_id][ix]}')

most_similar(4955066, pairwise_similarities, 'Cosine Similarity')

