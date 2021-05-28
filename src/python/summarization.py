import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# Here we will create a list of stopwords.
stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_lg')
punctuation = punctuation + '\n'
punctuation

text ="""It began early on Friday, bringing to an end 11 days of fighting in which more than 250 people were killed, most of them in Gaza.
Both Israel and Hamas claimed victory in the conflict.
Fresh clashes broke out at the al-Aqsa mosque compound in occupied East Jerusalem on Friday, testing the truce.
Israeli police spokesman Micky Rosenfeld told AFP news agency that Palestinians had thrown stones at officers, and that ""riot"" suppressing measures had been taken in response.
But the ceasefire seemed to be holding on Friday night. Israel has temporarily opened a crossing into Gaza, allowing food, fuel and medicine into the territory. 
The country has also lifted emergency restrictions inside its own borders.
The ceasefire began early on Friday, bringing to an end 11 days of bombardment in which more than 240 people have died, most of them in Gaza.
Palestinians poured on to the streets of Gaza soon after the truce began, while a Hamas official warned that its hands ""are on the trigger"".
Both Israel and Hamas have claimed victory in the conflict.
US President Joe Biden said the ceasefire brought ""genuine opportunity"" for progress.
On Thursday, more than 100 Israeli air strikes targeted Hamas infrastructure in the north of Gaza. 
Militants launched more than 300 rockets towards Israel during the day, the Israeli military said.
"""


def summarization(text):
#for article in result:
#! transform the text into an nlp doc
    doc = nlp(text)
    #tokens = [token.text for token in doc]

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
summarization(text)