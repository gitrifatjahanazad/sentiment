import nltk
import numpy
from nltk.book import text1
brown = nltk.corpus.brown
print text1.__dict__()
print len(brown.words())
# for word in brown.words():
#     print word