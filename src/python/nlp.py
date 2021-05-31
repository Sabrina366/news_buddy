import spacy
from spacy.matcher import PhraseMatcher
from collections import Counter
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

print()
nlp = spacy.load("en_core_web_lg")
matcher = PhraseMatcher(nlp.vocab, attr= 'LOWER')

### raw search input getting parsed to spacy.Doc object
doc = """The "Greek Gift" is a common chess theme, but the player making the sacrifice usually has more than one piece developed. Pro tip: If ...Ng4+ just hangs the knight and ...Qh4+ isn't possible, don't waste your time even thinking about playing ...Bxh2+. An attacking master like Marshall had no chance either.

On top of that, everyone recognizes the importance of piece activity and development, yet Marshall did not touch a piece on his queenside until move 17. Four moves later, he resigned.

Some miniatures feature brilliant attacks, and some... do not. Marshall lost the next game as well, and his championship efforts were over.

Game 1, Emanuel Lasker vs. David Janowsky, 1910
In his match vs. David Janowsky, Lasker somehow won even more easily than against Marshall, again 8-0 but this time with just three draws. And Janowsky's troubles started right in game one.

An aggressive player, Janowsky played Siegbert Tarrasch's defense to the Queen's Gambit (3...c5), where Black accepts an isolated d-pawn in exchange for piece activity. After 16 moves, however, Janowsky ended up with two isolated pawns on the queenside. Facing a difficult defensive task in the heavy piece endgame, Janowsky tried to shore up the position with the blunderous 19...Rd6??

This move simply loses a piece, in a tactic that appeared on the board prior to Janowsky throwing in the towel."""

search_input = """information about chess and the player named Janowsky"""

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
### list containing the counter values of the words matched only for debugging
    d = []

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
        if matches:
            sim_result = search_string.similarity(doc)
            #text_matches.append((sim_result, doc))
            #print("SimResult: {} \nMatch ID: {}\nString ID: {}\nStart: {}\nEnd: {}\nText: {}\nSentence: {}\nFull Text: {} ".format(
            #sim_result, match_id, string_id, start, end, span.text, span.sent, doc))
            print("\n".join(f'{i[0]} {i[1]} ({j})' for i,j in Counter(d).items()))             
        else:
            sim_result = 0.0
    #for every_match in text_matches:
    #    print(every_match)                       
    return sim_result

res = sim_res_search(search_input, doc)

print(res)


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
    select_length = int(len(sentence_tokens)*0.3)

#! Get summary of text
    summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    print((summary))

#! run function
GetSummary(doc)