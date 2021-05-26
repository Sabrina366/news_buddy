import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_lg')
punctuation = punctuation + '\n'
punctuation

text ="""It began early on Friday, bringing to an end 11 days of fighting in which more than 250 people were killed, most of them in Gaza.

Both Israel and Hamas claimed victory in the conflict.

Fresh clashes broke out at the al-Aqsa mosque compound in occupied East Jerusalem on Friday, testing the truce.

Israeli police spokesman Micky Rosenfeld told AFP news agency that Palestinians had thrown stones at officers, and that ""riot"" suppressing measures had been taken in response.

But the ceasefire seemed to be holding on Friday night. Israel has temporarily opened a crossing into Gaza, allowing food, fuel and medicine into the territory. The country has also lifted emergency restrictions inside its own borders.

The ceasefire began early on Friday, bringing to an end 11 days of bombardment in which more than 240 people have died, most of them in Gaza.

Palestinians poured on to the streets of Gaza soon after the truce began, while a Hamas official warned that its hands ""are on the trigger"".

Both Israel and Hamas have claimed victory in the conflict.

US President Joe Biden said the ceasefire brought ""genuine opportunity"" for progress.

On Thursday, more than 100 Israeli air strikes targeted Hamas infrastructure in the north of Gaza. Militants launched more than 300 rockets towards Israel during the day, the Israeli military said.

The Israel-Palestinian conflict explained
Life in the Gaza Strip
The children who have died in the conflict
Fighting began in Gaza on 10 May after weeks of rising Israeli-Palestinian tension in occupied East Jerusalem that culminated in clashes at a holy site revered by both Muslims and Jews. Hamas began firing rockets after warning Israel to withdraw from the site, triggering retaliatory air strikes.

At least 232 people, including more than 100 women and children, have been killed in Gaza, according to its health ministry. Israel has said at least 150 militants are among those killed in Gaza. Hamas does not give casualty figures for fighters.

In Israel 12 people, including two children, have been killed, its medical service says. Israel says some 4,000 rockets have been fired towards its territory by militants in Gaza.

Adi Vaizel, looks at the damage caused to the kitchen of his house after it was hit by a rocket launched from the Gaza Strip
IMAGE COPYRIGHTREUTERS
image captionAn Israeli man inspects damage in the kitchen of his house
What have the two sides said?
The Israeli Political Security Cabinet said it had ""unanimously accepted the recommendation"" for a ceasefire.

""The political leaders emphasised that the reality on the ground will determine the future of the campaign,"" the statement said.

Israeli Defence Minister Benny Gantz said on Twitter that the Gaza offensive had yielded ""unprecedented military gains"".

What the law says about the fighting
Israel defends Gaza strategy as death toll mounts
Why is Gaza blurry on Google Maps?
A Hamas official told the Associated Press news agency that the ceasefire announced by Israel amounts to a ""victory"" for the Palestinian people and a defeat for Israeli Prime Minister Benjamin Netanyahu.

Soon after the ceasefire started at 02:00 on Friday (23:00 GMT Thursday), large numbers of Palestinians took to the streets of Gaza in cars and on foot to celebrate.

Loudspeakers from mosques pronounced ""the victory of the resistance achieved over the Occupation during the 'Sword of Jerusalem' battle"".

What is Hamas?
But Basem Naim, from the Hamas Council on International Relations, told the BBC he was sceptical about whether the truce would last.

""Without justice for Palestinians, without stopping the Israeli aggression and Israeli atrocities against our people in Jerusalem, the ceasefire will continue to be fragile,"" he said.

A member of Hamas's political bureau, Ezzat al-Reshiq, issued a warning to Israel.

""It's true that the battle ends today but Netanyahu and the whole world should know that our hands are on the trigger and we will continue to ramp up the capabilities of this resistance,"" he told the Reuters news agency.

""We tell Netanyahu and his army, if you come back, we will come back.
"""


def summarization(text):
#for article in result:
    doc = nlp(text)
    #tokens = [token.text for token in doc]

    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    max_frequency = max(word_frequencies.values())
    max_frequency

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    sentence_tokens = [sent for sent in doc.sents]

    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    from heapq import nlargest

    select_length = int(len(sentence_tokens)*0.1)

    summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    print((summary))


summarization(text)