import random as ra
import time

import numpy as np
import scipy.sparse
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

corpus1 = ["Juan quiere comprar un coche. Ana no quiere comprar ningún coche"]
corpus2 = ["Cargamento de oro dañado por el fuego",
           "la entrega de la plata llegó en un  camión de plata",
           "El cargamento de oro llegó en un camión"]
corpus3 = ["Éste texto no tiene nada que ver con los demás",
           "la plata fue entregada en camiones color plata",
           "El cargamento de oro llegó en un camión. El cargamento de oro llegó en un camión. El cargamento de oro llegó en un camión",
           "Cargamentos de oro dañados por el fuego",
           "El cargamento de oro llegó en un camión"]

categories = ['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware',
              'comp.sys.mac.hardware', 'comp.windows.x', 'sci.space']

twenty_new = fetch_20newsgroups(subset='train', categories=categories)

#       corpus = corpus1
# corpus = corpus2
# corpus = corpus3
# lenguage = "spanish"
lenguage = "english"
limit = 10
corpus = twenty_new.data[:limit]

file = open("output.txt", "w+")
file.write("Numbers of elements: {}\n\n".format(len(corpus)))
file.close()


def simility_cosine(v, w):
    total = 0.0
    total1 = 0.0
    total2 = 0.0
    for i in range(len(v)):
        total += (v[i] * w[i])
        total1 += v[i] ** 2
        total2 += w[i] ** 2
    return total / (np.sqrt(total1) * np.sqrt(total2))


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
    vectorizer.sublinear_tf = True
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
    stemmer = SnowballStemmer(lenguage)
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
    file = open("output.txt", "a+")

    print("Final configuration of vectorizer:\n{}".format(vectorizer))
    file.write("\nFinal configuration of vectorizer:\n{}".format(vectorizer))

    t0 = time.time()
    vectorizer_fit = vectorizer.fit_transform(corpus).toarray().tolist()
    kmeans = KMeans(n_clusters=3, init="k-means++", random_state=0, precompute_distances="auto", max_iter=100,
                    algorithm="auto", n_jobs=-2, tol=0.0).fit(vectorizer_fit)
    label = kmeans.labels_

    print("Cluster centers:\n{}".format(kmeans.cluster_centers_))
    # file.write("Cluster centers:\n{}".format(kmeans.cluster_centers_))

    print("ID vectorizer:\n{}".format(vectorizer_fit))
    # file.write("ID vectorizer:\n{}".format(vectorizer_fit))

    predict = kmeans.predict(vectorizer_fit)
    print("Predict class:\n{}".format(predict))
    file.write("\nPredict class:\n{}".format(predict))
    print("Names process in the corpus:\n{}".format(vectorizer.get_feature_names()))
    # file.write("Names process in the corpus:\n{}".format(vectorizer.get_feature_names()))

    print("Kmeans score: \n{}".format(kmeans.score(vectorizer_fit, predict)))
    file.write("\nKmeans score: \n{}".format(kmeans.score(vectorizer_fit, predict)))

    print("Adjusted score: \n{}".format(metrics.adjusted_rand_score(label, predict)))
    file.write("\nAdjusted score: \n{}".format(metrics.adjusted_rand_score(label, predict)))

    print("Adjusted mutual info score: \n{}".format(metrics.adjusted_mutual_info_score(label, predict)))
    file.write("\nAdjusted mutual info score: \n{}".format(metrics.adjusted_mutual_info_score(label, predict)))

    print("homogenity score: \n{}".format(metrics.homogeneity_score(kmeans.labels_, predict)))
    file.write("\nhomogenity score: \n{}".format(metrics.homogeneity_score(kmeans.labels_, predict)))

    print("V measure score: \n{}".format(metrics.v_measure_score(kmeans.labels_, predict)))
    file.write("\nV measure score: \n{}".format(metrics.v_measure_score(kmeans.labels_, predict)))

    print("Completeness score: \n{}".format(metrics.completeness_score(kmeans.labels_, predict)))
    file.write("\nCompleteness score: \n{}".format(metrics.completeness_score(kmeans.labels_, predict)))

    print("Operations performant\n{}".format(time.time() - t0))
    file.write("\nOperations performant\n{}\n".format(time.time() - t0))
    file.close()
    print()
    print()


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


class my_kmedias():
    def __init__(self, data):
        self.data = data
        self.groups = []

    def mean(self, list_elem):
        total = 0
        for i in list_elem:
            total += i
        return total / len(list_elem)

    def distance_euclidean(self, data, mean_value):
        total = 0
        for i in range(0, len(data)):
            total += (data[i] - mean_value[i]) ** 2
        return np.sqrt(total)

    def distance_manhattan(self, data, mean_value):
        total = 0
        for i in range(0, len(data)):
            total += np.fabs(data[i] - mean_value[i])
        return total

    def distance_maximo(self, data, mean_value):
        total = 0
        for i in range(0, len(data)):
            aux = np.fabs(data[i] - mean_value[i])
            if total < aux:
                total = aux
        return total

    def distance_hamming(self, data, mean_value):
        return (np.array(data) != np.array(mean_value)).mean()

    def my_kmedias(self, k, distance, iterations):
        centroids_list = []
        repeat = True
        group = 0

        # Inicializate
        l = []
        size = len(self.data) - 1
        for i in range(k):
            centroids_list_ = []
            for j in range(len(self.data[0])):
                aux = ra.randint(0, size)
                boolean = True
                while (boolean):
                    aux = ra.randint(0, size)
                    if aux not in l:
                        l.append(aux)
                        boolean = False
                centroids_list_.append(round(float(self.data[aux][j]), 1))
            centroids_list.append(centroids_list_)
        # Repeat
        cont = 0
        while (repeat):
            self.groups = []
            fill_list = []
            for j in range(k):
                fill_list.append([])
            for i in range(len(self.data)):
                minimum = 9999.
                for j in range(k):

                    aux = distance(self.data[i], centroids_list[j])
                    if minimum > aux:
                        minimum = aux
                        group = j
                fill_list[group].extend(self.data[i])
            centroids_list2 = []
            for i in range(k):
                self.groups.append(round(len(fill_list[i]) / len(self.data[0])))
                centroids_list2_ = []
                for k1 in range(len(self.data[0])):
                    l = []

                    for j in range(0, len(fill_list[i]), len(self.data[0]) + k1):
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


k = 4
iterations = 4
my = my_kmedias(data2)
print("Number of elements: {}".format(len(data2)))
print("Number of groups: {}".format(k))
print("Number of iterations: {}".format(iterations))
print("Euclidean distance: {}".format(my.my_kmedias(k, my.distance_euclidean, iterations)))
print("Groups: {}".format(my.groups))
print("Manhattan distance: {}".format(my.my_kmedias(k, my.distance_manhattan, iterations)))
print("Groups: {}".format(my.groups))
print("Maximo distance: {}".format(my.my_kmedias(k, my.distance_maximo, iterations)))
print("Groups: {}".format(my.groups))
print("Hamming distance: {}".format(my.my_kmedias(k, my.distance_hamming, iterations)))
print("Groups: {}".format(my.groups))

print()
k = 3
iterations = 200
print("Number of elements: {}".format(len(data['data'][:, 0:3])))
print("Number of groups: {}".format(k))
print("Number of iterations: {}".format(iterations))
my2 = my_kmedias(data['data'][:, 0:3])
print("Euclidean distance: {}".format(my2.my_kmedias(k, my2.distance_euclidean, iterations)))
print("Groups: {}".format(my2.groups))
print("Manhattan distance: {}".format(my2.my_kmedias(k, my2.distance_manhattan, iterations)))
print("Groups: {}".format(my2.groups))
print("Maximo distance: {}".format(my2.my_kmedias(k, my2.distance_maximo, iterations)))
print("Groups: {}".format(my2.groups))
print("Hamming distance: {}".format(my2.my_kmedias(k, my2.distance_hamming, iterations)))
print("Groups: {}".format(my2.groups))
#print(simility_cosine(v1, w1))
