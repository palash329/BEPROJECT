from preprocess import preprocess
import operator 
import json
from collections import Counter
from nltk.corpus import stopwords
import string
#        terms_all = [term for term in preprocess(tweet['text'])if term not in stop]
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['RT', 'via']
fname = 'file.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line.strip())
        terms_all=list()
        try:
            temp=tweet['text']
        except:
            pass
        for term in preprocess(temp):
            if term not in stop:
                terms_all.append(term)
        # Update the counter
        count_all.update(terms_all)
    # Print the first 5 most frequent words
    for i in count_all.most_common(100):
        print i[0],i[1]
    
    

