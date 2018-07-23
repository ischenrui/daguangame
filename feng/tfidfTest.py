import pandas as pd, numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import time
t1=time.time()
train = pd.read_csv('data2/delpass_train.csv')
test = pd.read_csv('input/test_set.csv')
test_id = pd.read_csv('input/test_set.csv')[["id"]].copy()

column="word_seg"
n = train.shape[0]
vec = TfidfVectorizer(ngram_range=(1,2),min_df=4, max_df=0.85,use_idf=1,smooth_idf=1, sublinear_tf=1)
trn_term_doc = vec.fit_transform(train[column])
print(trn_term_doc.shape[1])
test_term_doc = vec.transform(test[column])

y=(train["class"]-1).astype(int)
clf =svm.LinearSVC()
clf.fit(trn_term_doc, y)
preds=clf.predict(test_term_doc)


#生成提交结果
fid0=open('sub/sub_lr_baseline.csv','w')
i=0
fid0.write("id,class"+"\n")
for item in preds:
    fid0.write(str(i)+","+str(item+1)+"\n")
    i=i+1
fid0.close()
t2=time.time()
print("time use:",t2-t1)