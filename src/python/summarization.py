import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_lg')
punctuation = punctuation + '\n'
punctuation

text ="""Russell Westbrook and Bradley Beal did what they do a near triple-double for one, 25 points in just 29 minutes for the other and the Washington Wizards reached the NBA playoffs as the Eastern Conference’s No 8 seed by overwhelming the Indiana Pacers 142-115 in the play-in round Thursday night.

Washington led by as many as 38 points and advanced to face Joel Embiid and the No 1 seed Philadelphia 76ers in the first round, marking quite a turnaround for coach Scott Brooks’ crew, who were 17-32 in early April.

Indiana’s run of five consecutive playoff appearances ended in coach Nate Bjorkgren’s debut season.

A little more than a week after breaking Oscar Robertson’s career record for most regular-season triple-doubles, Westbrook finished Thursday with 18 points, 15 rebounds and eight assists, and it was Beal second in the NBA in scoring two years in a row whose three-pointer opened up a 30-point lead at 98-68 with about four minutes left in the third quarter.

Beal skipped the fourth quarter entirely. Westbrook sat out the last eight minutes and tossed his shoes to a fan.
"""


def summarization(result):
  for article in result:
    doc = nlp(article)
  tokens = [token.text for token in doc]

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

  return(summary)