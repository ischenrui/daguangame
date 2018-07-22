"""
Genetic Algorithm
"""

from __future__ import division
import numpy as np
from sklearn.metrics import silhouette_samples as score
from feng.Genetic.mutation import mutation
from feng.Genetic.selection import selection
from feng.Genetic.crossover import crossover
from feng.Genetic import utils
from scipy.sparse import hstack
from sklearn.decomposition import TruncatedSVD as pca
import pickle
trn_term_doc = pickle.load(open('../data2/tfidf.txt', 'rb'))
p=pca(n_components=5000,random_state=42)

y=pickle.load(open('../data2/label.txt', 'rb'))
trn_term_doc=p.fit_transform(trn_term_doc,y)
pickle.dump(trn_term_doc,open('../data2/pca.txt', 'wb'))
size=trn_term_doc.shape[1]

def aimFunction(list):
    r=[]
    for index,l in enumerate(list):
        if l=="1":
            r.append(trn_term_doc.getcol(index))
    temp=hstack(r)
    s=score(temp,y)
    print(s)
    return s



population=[]
for i  in range(5):
    entity=''
    for j in range(size):
        entity=entity+str(np.random.randint(0,2))
    population.append(entity)
t=[]
for i in range(1000):
    #selection
    value=utils.fitness(population,aimFunction)
    population_new=selection(population,value)
    #crossover
    offspring =crossover(population_new,0.7)
    #mutation
    population=mutation(offspring,0.05)
    result=[]
    for j in range(len(population)):
        result.append(aimFunction(population[j]))
    t.append(max(result))
