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
def count():
    train = pd.read_csv('input/train_set.csv')
    y = pickle.load(open('data2/label.txt', 'rb'))
    column = "word_seg"
    x = train[column]
    classDic={}
    passDic={}
    for i,value in enumerate(x):
        print(i)
        words=value.split(" ")
        passDic[i]={}
        for w in words:
            if w in passDic[i]:
                passDic[i][w]+=1
            else:
                passDic[i][w]= 1
            if y[i] not in classDic:
                classDic[y[i]]={}
            if w in classDic[y[i]]:
                classDic[y[i]][w]+=1
            else:
                classDic[y[i]][w]= 1
    pickle.dump(passDic, open('data2/passDic.txt', 'wb'))
    pickle.dump(classDic, open('data2/classDic.txt', 'wb'))
def sort(rate,n_word):
    passDic=pickle.load(open('data2/passDic.txt', 'rb'))
    num=0
    passid={}
    for id in passDic:
        dic=passDic[id]
        maxd=None
        all=0
        for d in dic:
            all+=dic[d]
            if maxd is None or dic[d]>dic[maxd]:
                maxd=d
        if dic[maxd]/all>=rate:
            num+=1
            passid[id]=1
            # print("pass:"+str(id)+"---word:"+str(maxd))
    sum=0
    for id in passDic:
        dic = passDic[id]
        if len(dic)<=n_word:
            sum+=1
            passid[id] = 1
    list=[k for k in passid]
    pickle.dump(list, open('data2/delpass.txt', 'wb'))
def findWord():
    classDic = pickle.load(open('data2/classDic.txt', 'rb'))
    alldic=pickle.load(open('data2/dic.txt', 'rb'))
    classRate={}
    for cla in classDic:
        dic=classDic[cla]
        classRate[cla]=[]
        for d in dic:
            rate=dic[d]/alldic[d]
            if rate>=0.5 and alldic[d]>=1000:
                classRate[cla].append(d)
        print(str(cla)+":"+str(len(classRate[cla])))
def delpass():
    train = pd.read_csv('input/train_set.csv')
    list=pickle.load(open('data2/delpass.txt', 'rb'))
    train.drop(train.index[list],inplace=True)
    train.to_csv('data2/delpass_train.csv',index=None)
def check():
    train = pd.read_csv('data2/delpass_train.csv')
    column = "word_seg"
    x = train[column]
    passDic = {}
    for i, value in enumerate(x):
        words = value.split(" ")
        passDic[i] = {}
        for w in words:
            if w in passDic[i]:
                passDic[i][w] += 1
            else:
                passDic[i][w] = 1
    num = 0
    passid = {}
    rate=0.3
    n_word=20
    for id in passDic:
        dic = passDic[id]
        maxd = None
        all = 0
        for d in dic:
            all += dic[d]
            if maxd is None or dic[d] > dic[maxd]:
                maxd = d
        if dic[maxd] / all >= rate:
            num += 1
            passid[id] = 1
            # print("pass:"+str(id)+"---word:"+str(maxd))
    sum = 0
    for id in passDic:
        dic = passDic[id]
        if len(dic) <= n_word:
            sum += 1
            passid[id] = 1
    list = [k for k in passid]
    print(list)
if __name__ == '__main__':
    check()