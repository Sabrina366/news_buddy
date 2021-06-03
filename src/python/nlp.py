import spacy
from spacy.matcher import PhraseMatcher
from collections import Counter
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

print()
nlp = spacy.load("en_core_web_lg", disable=['ner', 'parser', 'textcat'])
nlp.add_pipe('sentencizer')
matcher = PhraseMatcher(nlp.vocab, attr= 'LOWER')

### raw search input getting parsed to spacy.Doc object




def sim_res_search(search_input, doc):
### list to store the search words from user and be able to match the texts from the DB.
    terms = []
    
### Lemmatization of the search input , added to tweek the matching slightly further.

    lem_doc = nlp(search_input)
    for token in lem_doc:
        lem_string = token.lemma_
        search_input = search_input + ' ' + lem_string

    #print(search_input + '\n')
    search_string = nlp(search_input)
        
### cleans the search from stop words and punctuation and adds to terms list for matching processing of texts.
    search_string_cleaned = [token for token in search_string if not token.is_stop and not token.is_punct]    

    for token in search_string_cleaned:
        terms.append(token.text)
    
    patterns = [nlp.make_doc(text) for text in terms]
    matcher.add("TerminologyList", patterns)
### take in texts as a list..    
    text_list = [] 
    text_list.append(doc)
### list containing the counter values of the words matched only for debugging/testing
    d = []
    sim_result = 0.0
    #text_matches = []
    ### looping trough the texts to look for matches using the phrasematcher instanced with the variable matcher.
    for texts in text_list:
        doc = nlp(texts)
        matches = matcher(doc)
        
        ### for loop for prints only
        for match_id, start, end in matches:
            span = doc[start:end]
            string_id = nlp.vocab.strings[match_id]       
            d.append((string_id, span.text))        
        # If there is a match in words from the search the object will be given a score from 0-1 if not the score will remain at 0.0
        if matches:
            sim_result = search_string.similarity(doc)
            print(sim_result)
            # .........Prints For Testing..........
            # text_matches.append((sim_result, doc))
            #print("SimResult: {} \nMatch ID: {}\nString ID: {}\nStart: {}\nEnd: {}\nText: {}\nSentence: {}\nFull Text: {} ".format(
            #sim_result, match_id, string_id, start, end, span.text, span.sent, doc))
            #print("\n".join(f'{i[0]} {i[1]} ({j})' for i,j in Counter(d).items()))             
        
    #for every_match in text_matches:
    #    print(every_match)                       
    return sim_result

#res = sim_res_search(search_input, doc)

#print(res)

#! Redingtime section
def readingTime(doc):
  total_words = len([ token.text for token in nlp(doc) ])
  estimated_time = total_words / 200.0
  print(estimated_time)
  return estimated_time

#! Here we will create a list of stopwords.
stopwords = list(STOP_WORDS)
punctuation = punctuation + '\n'
punctuation

def GetSummary(text):

#! transform the text into an nlp doc
    doc = nlp(text)

#! Calculate word frequencies after removing stopwords and punctuations   
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    max_frequency = max(word_frequencies.values())

#! Calculate the maximum frequency and divide it by all frequencies to get normalized word frequencies
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    sentence_tokens = [sent for sent in doc.sents]

#! Calculate the most important sentences by adding the word frequencies in each sentence
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    from heapq import nlargest

#! calculate % of the text with maximum score
    select_length = int(len(sentence_tokens)*0.1)

#! Get summary of text
    summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    #print((summary))
    return summary
#! run function
#GetSummary(doc)