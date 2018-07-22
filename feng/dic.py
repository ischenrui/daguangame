import pickle
import pandas as pd, numpy as np
import time
def getDic():
    train = pd.read_csv('input/train_set.csv')
    column = "word_seg"
    x = train[column]
    dic={}
    for line in x:
        words=line.split(" ")
        for w in words:
            if w in dic:
                dic[w]+=1
            else:
                dic[w]=1
    pickle.dump(dic, open('data2/dic.txt', 'wb'))

if __name__ == '__main__':
    getDic()
    sentence = pickle.load(open('data2/dic.txt', 'rb'))
    list=[]
    for k in sentence:
        list.append(k)
    print(len(sentence))
    print(max(list))
    print(min(list))