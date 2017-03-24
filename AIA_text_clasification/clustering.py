import random as ra

import numpy as np
from sklearn.datasets import load_iris
import scipy.sparse as sc


from nltk.corpus import stopwords
import re
import unicodedata
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

vectorizer = TfidfVectorizer(min_df=1,smooth_idf = False,strip_accents="ascii",lowercase=True)
corpus = ["Juan quiere comprar un coche. Ana no quiere comprar ningún coche"]
print(vectorizer)

print("Using simple way")
#Simple model
vectorizer.norm = None
#vectorizer.use_idf = False
vectorizer_fit = vectorizer.fit_transform(corpus)
print(vectorizer_fit)
print(vectorizer.get_feature_names())

#Simple model with normalized euclidean distance
vectorizer.norm ='l2'
vectorizer.use_idf = True
vectorizer.smooth_idf = True
vectorizer.sublinear_tf = False
vectorizer_fit = vectorizer.fit_transform(corpus)
print(vectorizer_fit)
print(vectorizer.get_feature_names())

#Simple model with normalized coseno distance
vectorizer.norm ='l1'
vectorizer_fit = vectorizer.fit_transform(corpus)
print(vectorizer_fit)
print(vectorizer.get_feature_names())



print()
print()
#Using stop words
print("Using stop words")
vectorizer.stop_words =stopwords.words('spanish')


#Simple model
vectorizer.norm = None
#vectorizer.use_idf = False
vectorizer_fit = vectorizer.fit_transform(corpus)
print(vectorizer_fit)
print(vectorizer.get_feature_names())

#Simple model with normalized euclidean distance
vectorizer.norm ='l2'
vectorizer.use_idf = True
vectorizer.smooth_idf = True
vectorizer.sublinear_tf = False
vectorizer_fit = vectorizer.fit_transform(corpus)
print(vectorizer_fit)
print(vectorizer.get_feature_names())

#Simple model with normalized coseno distance
vectorizer.norm ='l1'
vectorizer_fit = vectorizer.fit_transform(corpus)
print(vectorizer_fit)
print(vectorizer.get_feature_names())

print()
print("TO-DO: tomando raices de palabras")
print("TO-DO: tomando raices de palabras")
print("TO-DO: tomando raices de palabras")

#Using tfidf
print()
print()
print("Using tfidf")
vectorizer.tfidf =True


#Simple model
vectorizer.norm = None
#vectorizer.use_idf = False
vectorizer_fit = vectorizer.fit_transform(corpus)
print(vectorizer_fit)
print(vectorizer.get_feature_names())

#Simple model with normalized euclidean distance
vectorizer.norm ='l2'
vectorizer.use_idf = True
vectorizer.smooth_idf = True
vectorizer.sublinear_tf = False
vectorizer_fit = vectorizer.fit_transform(corpus)
print(vectorizer_fit)
print(vectorizer.get_feature_names())

#Simple model with normalized coseno distance
vectorizer.norm ='l1'
vectorizer_fit = vectorizer.fit_transform(corpus)
print(vectorizer_fit)
print(vectorizer.get_feature_names())


#def elimina_tildes(s):
#    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))


#text = re.findall(r"[A-Za-zÁ-Úá-ú]+", elimina_tildes(str(corpus)))

# In the python console, you need to input nltk.download()
#print(stopwords.words('spanish'))
#stw = [ word for word in text if word not in stopwords.words('spanish') ]
#print(stw)

print()





data = load_iris()
data2 = [[51], [43], [62], [64], [45], [42], [46], [45], [45], [62], [47], [52], [64], [51], [65], [48], [49],
         [46], [64], [51], [52], [62], [49], [48], [62], [43], [40], [48], [64], [51], [63], [43], [65], [66],
         [65], [46], [39], [62], [64], [52], [63], [64], [48], [64], [48], [51], [48], [64], [42], [48], [41]]


def distance_euclidean(data, mean_value):
    total = 0
    for i in range(0, len(data)):
        total += (data[i] - mean_value[i]) ** 2
    return np.sqrt(total)


def distance_manhattan(data, mean_value):
    total = 0
    for i in range(0, len(data)):
        total += np.fabs(data[i] - mean_value[i])
    return total


def distance_maximo(data, mean_value):
    total = 0
    for i in range(0, len(data)):
        aux = np.fabs(data[i] - mean_value[i])
        if total < aux:
            total = aux
    return total


def distance_hamming(data, mean_value):
    return (np.array(data) != np.array(mean_value)).mean()


print("Number of elements: {}".format(len(data['data'])))


def mean(list_elem):
    total = 0
    for i in list_elem:
        total += i
    return total / len(list_elem)


def k_my_kmedias(k, data, distance, iterations):
    centroids_list = []
    repeat = True
    group = 0

    # Inicializate
    l = []
    size = len(data) - 1
    for i in range(k):
        centroids_list_ = []
        for j in range(len(data[0])):
            aux = ra.randint(0, size)
            boolean = True
            while (boolean):
                aux = ra.randint(0, size)
                if aux not in l:
                    l.append(aux)
                    boolean = False
            centroids_list_.append(round(float(data[aux][j]), 1))
        centroids_list.append(centroids_list_)
    # Repeat
    cont = 0
    while (repeat):
        fill_list = []
        for j in range(k):
            fill_list.append([])
        for i in range(len(data)):
            minimum = 9999.
            for j in range(k):

                aux = distance(data[i], centroids_list[j])
                if minimum > aux:
                    minimum = aux
                    group = j
            fill_list[group].extend(data[i])
        centroids_list2 = []
        for i in range(k):
            centroids_list2_ = []
            for k1 in range(len(data[0])):
                l = []

                for j in range(0, len(fill_list[i]), len(data[0]) + k1):
                    l.append(round(fill_list[i][j], 1))
                value = 0.0
                if l:
                    value = np.mean(l)
                centroids_list2_.append(round(float(value), 1))
            centroids_list2.append(centroids_list2_)
        if iterations - 1 == cont:
            repeat = False
        if centroids_list == centroids_list2:
            repeat = False
        centroids_list = centroids_list2.copy()

        cont += 1

    return centroids_list


k = 2
iterations = 3
print("Euclidean distance: {}".format(k_my_kmedias(k, data2, distance_euclidean, iterations)))

k = 3
iterations = 6
print("Euclidean distance: {}".format(k_my_kmedias(k, data['data'][:, 0:3], distance_euclidean, iterations)))
print("Manhattan distance: {}".format(k_my_kmedias(k, data['data'][:, 0:3], distance_manhattan, iterations)))
print("Maximo distance: {}".format(k_my_kmedias(k, data['data'][:, 0:3], distance_maximo, iterations)))
print("Hamming distance: {}".format(k_my_kmedias(k, data['data'][:, 0:3], distance_hamming, iterations)))

