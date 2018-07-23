import pandas as pd,numpy as np
from sklearn import svm
from scipy.stats import rv_continuous
from sklearn.feature_extraction.text import  TfidfVectorizer
import time,pickle
t1=time.time()

def getData():
    train = pd.read_csv('data2/delpass_train.csv')
    column = "word_seg"
    vec = TfidfVectorizer(ngram_range=(1, 2), min_df=4, max_df=0.85, use_idf=1, smooth_idf=1, sublinear_tf=1)
    trn_term_doc = vec.fit_transform(train[column])
    y = (train["class"] - 1).astype(int)
    pickle.dump({"x":trn_term_doc,"y":y}, open('data2/delx,y', 'wb'))
def test(trn_term_doc,y):

    clf =svm.LinearSVC()
    clf.fit(trn_term_doc, y)

def getDic():
    # temp=pickle.load(open('data2/delx,y', 'rb'))
    # x=temp['x']
    # y=temp['y']
    # r={}
    # for i,yi in enumerate(y):
    #     if yi in r:
    #         r[yi].append(x.getrow(i))
    #     else:
    #         r[yi]=[x.getrow(i)]
    # result={k:{"matrix":vstack(r[k])} for k in r}
    # pickle.dump(result, open('data2/class_mat', 'wb'))
    # result={}
    # for k in r:
    #     result[k]={"matrix":vstack(r[k])}
    result=pickle.load(open('data2/class_mat', 'rb'))
    rv=rv_continuous()
    for k in result:
        print(str(k) + ":" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        list=[]
        for i in range(result[k]["matrix"].shape[1]):
            stds=np.std(result[k]["matrix"].getcol(i).todense(), axis=0)
            list.append(stds[0][0])
            if i%10000==0:
                print("i:"+str(i) + ":" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print(str(k)+":"+str(len(list)))
        pickle.dump(list, open('data2/std_'+str(k), 'wb'))

if __name__ == '__main__':
    # getData()
    getDic()