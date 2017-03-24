import random as ra

import numpy as np
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.datasets import load_iris
from sklearn.feature_extraction.text import TfidfVectorizer

corpus1 = ["Juan quiere comprar un coche. Ana no quiere comprar ningún coche"]
corpus2 = ["Cargamento de oro dañado por el fuego",
           "la entrega de la plata llegó en un  camión de plata",
           "El cargamento de oro llegó en un camión"]
corpus3 = ["Éste texto no tiene nada que ver con los demás",
           "la plata fue entregada en camiones color plata",
           "El cargamento de oro llegó en un camión. El cargamento de oro llegó en un camión. El cargamento de oro llegó en un camión",
           "Cargamentos de oro dañados por el fuego",
           "El cargamento de oro llegó en un camión"]

corpus = corpus3


# Simple model
def simple_configuation(vectorizer):
    print("Using simple way")
    vectorizer.use_idf = False
    vectorizer.norm = None
    return vectorizer


def euclidean_configuation(vectorizer):
    # Simple model with normalized euclidean distance
    print("Using normalized euclidean distance")
    vectorizer.norm = 'l2'
    vectorizer.use_idf = False
    vectorizer.sublinear_tf = False
    return vectorizer


def cosine_configuration(vectorizer):
    # Simple model with normalized cosino distance
    print("Using normalized cosino distance")
    vectorizer.norm = 'l1'
    vectorizer.use_idf = False
    vectorizer.sublinear_tf = False
    return vectorizer


def stop_words_configuration(vectorizer, configuration):
    # Using stop words
    print("Using stop words")
    vectorizer.stop_words = stopwords.words('spanish')
    vectorizer = configuration(vectorizer)
    return vectorizer


# Taking root words
def taking_root_words_configuration(vectorizer, configuration):
    print("Taking root words")
    vectorizer = stop_words_configuration(vectorizer, configuration)
    stemmer = SnowballStemmer("spanish")
    vectorizer.vocabulary = set([stemmer.stem(i) for i in vectorizer.get_feature_names()])
    return vectorizer


def tfidf_configuration(vectorizer, configuration):
    print("Using tfidf")
    vectorizer = taking_root_words_configuration(vectorizer, configuration)
    vectorizer.smooth_idf = True
    vectorizer.use_idf = True
    vectorizer.sublinear_tf = True
    return vectorizer


def training(corpus, vectorizer):
    print("Final configuration of vectorizer: \n{}".format(vectorizer))
    vectorizer_fit = vectorizer.fit_transform(corpus)
    print("ID vectorizer: \n{}".format(vectorizer_fit))
    print("names process in the corpus: \n{}".format(vectorizer.get_feature_names()))


vectorizer = TfidfVectorizer(min_df=1, smooth_idf=False, use_idf=False)

simple_configuation(vectorizer)
training(corpus, vectorizer)

euclidean_configuation(vectorizer)
training(corpus, vectorizer)

cosine_configuration(vectorizer)
training(corpus, vectorizer)

stop_words_configuration(vectorizer, simple_configuation)
training(corpus, vectorizer)

stop_words_configuration(vectorizer, euclidean_configuation)
training(corpus, vectorizer)

stop_words_configuration(vectorizer, cosine_configuration)
training(corpus, vectorizer)

taking_root_words_configuration(vectorizer, simple_configuation)
training(corpus, vectorizer)

taking_root_words_configuration(vectorizer, euclidean_configuation)
training(corpus, vectorizer)

taking_root_words_configuration(vectorizer, cosine_configuration)
training(corpus, vectorizer)

tfidf_configuration(vectorizer, simple_configuation)
training(corpus, vectorizer)

tfidf_configuration(vectorizer, euclidean_configuation)
training(corpus, vectorizer)

tfidf_configuration(vectorizer, cosine_configuration)
training(corpus, vectorizer)

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
