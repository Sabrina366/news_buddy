import spacy
from spacy.matcher import PhraseMatcher
from collections import Counter

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




