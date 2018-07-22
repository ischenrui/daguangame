import pandas as pd
import pickle
from sklearn.feature_extraction.text import  TfidfVectorizer
import time
t1=time.time()
column="word_seg"
train = pd.read_csv('input/train_set.csv')
vec = TfidfVectorizer(ngram_range=(1,1),min_df=3, max_df=0.9,use_idf=1,smooth_idf=1, sublinear_tf=1)
trn_term_doc = vec.fit_transform(train[column])
pickle.dump(trn_term_doc, open('data2/1_tfidf.txt', 'wb'))