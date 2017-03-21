import random as ra
import math as ma
import numpy as np
from nltk.corpus import stopwords
from sklearn.datasets import load_iris

data = load_iris()


#stopwords.download()
#stw = [ word for word in palabras if word not in stopwords.words('spanish') ]
def distance_euclidean(data,mean_value):
    total = 0
    for i in range(0,len(data)):
        total += (data[i]-mean_value[i])**2
    return np.sqrt(total)

def distance_manhattan(data,mean_value):
    total = 0
    for i in range(0,len(data)):
        total += np.fabs(data[i]-mean_value[i])
    return total

def distance_maximo(data,mean_value):
    total = 0
    for i in range(0, len(data)):
        aux = np.fabs(data[i] - mean_value[i])
        if total > aux:
            total = aux
    return total


def distance_hamming(data,mean_value):
    return (np.array(data)!=np.array(mean_value)).mean()

#print(distance_euclidea(data['data'],np.array([1.,2.,3.,4.])))
data_values = np.array([[1., 2., 4.],[2.,3.,3.]])


mean_value = np.array([2., 5., 2.])

#print(distance_euclidean(data_values[0],mean_value))
#print(distance_manhattan(data_values[0],mean_value))

print("Number of elements: {}".format(len(data['data'])))

def k_my_kmedias(k,data,distance):
    centroids_list = []
    repeat = True
    group = 0

    # Inicializate
    size = len(data) - 1
    for i in range(k):
        centroids_list_ = []
        for j in range(len(data[0])):
            centroids_list_.append(data[ra.randint(0,size)][j])
        centroids_list.append(centroids_list_)

    # Repeat
    cont = 0
    while(repeat):
        cont +=1
        fill_list = []
        for i in range(len(data)):
            minimum = 9999.
            for j in range(k):
               aux = distance(data[i],centroids_list[j])
               if minimum > aux:
                   minimum = aux
                   group = j
            fill_list.append([data[i],group])
        centroids_list2 = []
        for i in range(k):
            centroids_list2_ = []
            for j in range(len(fill_list[0][0])):
                classify_ = []
                for k1 in range(len(fill_list)):
                    if fill_list[k1][1] == i:
                        classify_.append(fill_list[k1][0][j])
                if classify_ != []:
                    centroids_list2_.append(np.mean(classify_))
                else:
                    centroids_list2_.append(0.)
            centroids_list2.append(centroids_list2_)

        if centroids_list == centroids_list2:
            repeat = False
        centroids_list = centroids_list2.copy()
    return centroids_list

k = 10
print("Euclidean distance: {}".format(k_my_kmedias(k,data['data'],distance_euclidean)))
print("Manhattan distance: {}".format(k_my_kmedias(k,data['data'],distance_manhattan)))
print("Maximo distance: {}".format(k_my_kmedias(k,data['data'],distance_maximo)))
print("Hamming distance: {}".format(k_my_kmedias(k,data['data'],distance_hamming)))
