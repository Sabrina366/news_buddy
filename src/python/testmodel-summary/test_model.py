import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import spacy
import string
import gensim
import operator
import re

df_articles = pd.read_csv('articles.test.csv')
df_articles.head()

from spacy.lang.en.stop_words import STOP_WORDS

spacy_nlp = spacy.load('en_core_web_lg')

#create list of punctuations and stopwords
punctuations = string.punctuation
stop_words = spacy.lang.en.stop_words.STOP_WORDS

#function for data cleaning and processing
#This can be further enhanced by adding / removing reg-exps as desired.

def spacy_tokenizer(sentence):
 
    #remove distracting single quotes
    sentence = re.sub('\'','',sentence)

    #remove digits adnd words containing digits
    sentence = re.sub('\w*\d\w*','',sentence)

    #replace extra spaces with single space
    sentence = re.sub(' +',' ',sentence)

    #remove unwanted lines starting from special charcters
    sentence = re.sub(r'\n: \'\'.*','',sentence)
    sentence = re.sub(r'\n!.*','',sentence)
    sentence = re.sub(r'^:\'\'.*','',sentence)
    
    #remove non-breaking new line characters
    sentence = re.sub(r'\n',' ',sentence)
    
    #remove punctunations
    sentence = re.sub(r'[^\w\s]',' ',sentence)
    
    #creating token object
    tokens = spacy_nlp(sentence)
    
    #lower, strip and lemmatize
    tokens = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in tokens]
    
    #remove stopwords, and exclude words less than 2 characters
    tokens = [word for word in tokens if word not in stop_words and word not in punctuations and len(word) > 2]
    
    #return tokens
    return tokens

print ('Cleaning and Tokenizing...')
df_articles['text_tokenized'] = df_articles['text'].map(lambda x: spacy_tokenizer(x))

df_articles.head()

text_plot = df_articles['text_tokenized']
text_plot[0:5]

from gensim import corpora

#creating term dictionary
dictionary = corpora.Dictionary(text_plot)

#filter out terms which occurs in less than 4 documents and more than 20% of the documents.
#NOTE: Since we have smaller dataset, we will keep this commented for now.

#dictionary.filter_extremes(no_below=4, no_above=0.2)

#list of few which which can be further removed
stoplist = set('hello and if this can would should could tell ask stop come go')
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
dictionary.filter_tokens(stop_ids)

dict_tokens = [[[dictionary[key], dictionary.token2id[dictionary[key]]] for key, value in dictionary.items() if key <= 50]]
#print (dict_tokens)

corpus = [dictionary.doc2bow(desc) for desc in text_plot]

word_frequencies = [[(dictionary[id], frequency) for id, frequency in line] for line in corpus[0:3]]

#print(word_frequencies)

article_tfidf_model = gensim.models.TfidfModel(corpus, id2word=dictionary)
article_lsi_model = gensim.models.LsiModel(article_tfidf_model[corpus], id2word=dictionary, num_topics=300)

gensim.corpora.MmCorpus.serialize('article_tfidf_model_mm', article_tfidf_model[corpus])
gensim.corpora.MmCorpus.serialize('article_lsi_model_mm',article_lsi_model[article_tfidf_model[corpus]])

#Load the indexed corpus
article_tfidf_corpus = gensim.corpora.MmCorpus('article_tfidf_model_mm')
article_lsi_corpus = gensim.corpora.MmCorpus('article_lsi_model_mm')

from gensim.similarities import MatrixSimilarity

article_index = MatrixSimilarity(article_lsi_corpus, num_features = article_lsi_corpus.num_terms)


from operator import itemgetter

def search_similar_articles(search_term):

    query_bow = dictionary.doc2bow(spacy_tokenizer(search_term))
    query_tfidf = article_tfidf_model[query_bow]
    query_lsi = article_lsi_model[query_tfidf]

    article_index.num_best = 5

    article_list = article_index[query_lsi]

    article_list.sort(key=itemgetter(1), reverse=True)
    article_names = []

    for j, article in enumerate(article_list):

        article_names.append (
            {
                'relevance': round((article[1] * 100),2),
                'article_title': df_articles['title'][article[0]],
                'article': df_articles['text'][article[0]],
                #'summarization': summarization(article)
            }

        )
        if j == (article_index.num_best-1):
            break

    result = pd.DataFrame(article_names, columns=['relevance','article_title','article'])
    #print(type(result))
    #summary = (summarization(result))
    return result 
"""     for result.article in result:
      summary = summarization(result.article)

    final_result = result + summary
 """



# search for article tiles that are related to below search parameters
print(search_similar_articles('war and crime'))
print(search_similar_articles('social media and tech'))
print(search_similar_articles('love affair hate'))