import spacy
from spacy.matcher import PhraseMatcher

print()
nlp = spacy.load("en_core_web_lg")
matcher = PhraseMatcher(nlp.vocab, attr= 'LOWER')

### list to store the search words from user and be able to match the texts from the DB.
terms = []

### raw search input getting parsed to spacy.Doc object
search_input = "she is a human and she apple played chess against rita and when or what if she likes playing chess. Rita loves movies."

### Lemmatization of the search input , added to tveek matching slightly further.

lem_doc = nlp(search_input)
for token in lem_doc:
    lem_string = token.lemma_
    search_input = search_input + ' ' + lem_string

print(search_input + '\n')
search_string = nlp(search_input)


### cleans the search from stop words and punctuation and adds to terms list for matching processing of texts.

search_string_cleaned = [token for token in search_string if not token.is_stop and not token.is_punct]

for token in search_string_cleaned:
    terms.append(token.text)

    
patterns = [nlp.make_doc(text) for text in terms]
matcher.add("TerminologyList", patterns)

### take in texts as a list..
doc1 = """I liked the movies etc The movie had good direction APPLE The movie was amazing i.e.
            The movie was average direction was not bad The cinematography was nice. i.e.
            The movie was a bit lengthy  otherwise fantastic  etc etc """

doc2 = """Chess is a great game, they play the game with two players. The game against Rita is a famous one and when if they were playing and likes playing chess."""


doc3 = """But they're still human, which has meant some poorly played games throughout the years, by both champions and challengers, players who won the match or lost it. Here are five of the worst World Chess Championship games ever played """
print("We are Matches: \n")
text_list = [] 
text_list.append(doc1)
text_list.append(doc2)
text_list.append(doc3)
for texts in text_list:
    doc = nlp(texts)
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        
        print(span.text)
    
    










