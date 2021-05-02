import nltk
from nltk.book import *



#print(type(text1))
#print(len(text1))
#print(len(set(text1)))
#print(text1[:10])


from nltk.corpus import gutenberg
#print(gutenberg.fileids())
#print(len(gutenberg.fileids()))
#print(gutenberg.fileids()[15])

#### functions used in gutenberg corpus: .words - .sents - .paras = for paragraphs.

hamlet= gutenberg.words('shakespeare-hamlet.txt')
#print(len(hamlet))

hamlet_sentences= gutenberg.sents('shakespeare-hamlet.txt')
#print(len(hamlet_sentences))
#print(hamlet_sentences[1024])
#print(len(gutenberg.paras('shakespeare-hamlet.txt')))

#print(text1.count('horse'))
#print(text1.concordance('passion'))
#print(text2.concordance('passion'))

#vocab= nltk.FreqDist(text1)
#print(len(vocab))
#print(vocab.most_common(20))
#mc= sorted([w for w in vocab.most_common(80) if len(w[0])>3], key=lambda x: x[1], reverse=True)
#print(mc)

##### a dispersion plot shows you where in the document a word is used. you can pass in a list of words and you will git a figure.
#ext1.dispersion_plot(['capture', 'whale', 'life', 'death'])




#### a small dictionary:
from nltk.corpus import wordnet as wn
#w = wn.synsets("cold")[3]
#print(w)
#print(w.name(), ':', w.definition())
#print(w.examples())




## punctuation and stop words:

from string import punctuation
#print(punctuation)
#without_punct= [w for w in text1 if w not in punctuation]

from nltk.corpus import stopwords
#sw= stopwords.words('english')
#print(sw)
#without_sw= [w for w in without_punct if w not in sw]

#print(len(text1))
#print(len(without_punct))
#print(len(without_sw))





###Stemming and Lemmatization:

from nltk.stem.porter import PorterStemmer
#st= PorterStemmer()
#words= ['is', 'cooking', 'try', 'giving', 'birds', 'did']
#for word in words:
   # print(word, st.stem(word))

# wordnet lemmatizer:
from nltk.stem import WordNetLemmatizer
#wnl= WordNetLemmatizer()
#words= ['is', 'cooking', 'try', 'giving', 'birds', 'did']
#for word in words:
    #print(word, wnl.lemmatize(word))


## Sentence, words Tokenization:
from nltk.tokenize import sent_tokenize , word_tokenize
#s= 'hello. I am laith! what a nice day. 1993 is the year when I born'
#print(sent_tokenize(s))
#w= word_tokenize(s)
#print(w)


## POST, Part of Speech Tagging:
#print(nltk.pos_tag(w))
#print(nltk.pos_tag(w, tagset='universal'))


##Word to Vector:
from gensim.models import Word2Vec
#emma_vec= Word2Vec(gutenberg.sents('austen-emma.txt'))
#leaves_vec= Word2Vec(gutenberg.sents('whitman-leaves.txt'))
#print(emma_vec.wv.most_similar('pain', topn=6))
#print(leaves_vec.wv.most_similar('pain', topn=6))
# does not work, error: No module named 'gensim'

#GG

