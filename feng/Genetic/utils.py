from __future__ import division



def fitness(population,aimFunction):
    value=[]
    for i in range(len(population)):
        value.append(aimFunction(population[i]))
        #weed out negative value
        if value[i]<0:
            value[i]=0
    return value