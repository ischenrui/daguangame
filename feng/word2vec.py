import pandas as pd, numpy as np
import gensim
import time
import pickle
from scipy.sparse import hstack,vstack
class MySentences(object):
    def __init__(self,x):
        self.time=0
        self.passage=x

    def __iter__(self):
        self.time+=1
        print(str(self.time)+'time')
        for line in self.passage:
            yield  line
def trainWord2vec():
    train = pd.read_csv('input/train_set.csv')
    column = "word_seg"

    x = train[column]
    print('开始训练')
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    sen = MySentences(x)
    model = gensim.models.Word2Vec(sen,size=50,window=10,iter=12)
    print('保存模型')
    model.save("data2/word2vec.txt")
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
def computer():
    model = gensim.models.Word2Vec.load("data2/word2vec.txt")
    word_vectors = model.wv
    dic = pickle.load(open('data2/dic.txt', 'rb'))
    similar={}
    i=0
    for d in dic:
        similar[d]=0
        print(str(i) +  ":"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        for t in dic:
            s= word_vectors.n_similarity(d, t)
            similar[d]+=s
        i += 1
    pickle.dump(similar, open('data2/similardic.txt', 'wb'))
if __name__ == '__main__':
    trainWord2vec()
    computer()
