import random

from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

import clasification_text_1 as cla1
import clasification_text_2 as cla2
import clustering as cl

# TASK 3

categories = ['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware',
              'comp.sys.mac.hardware', 'comp.windows.x', 'sci.space']
# Downloading the fetch_20newsgroup
twenty_new = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'), categories=categories)

twenty_new_test = fetch_20newsgroups(subset='test', remove=('headers', 'footers', 'quotes'), categories=categories)
# Extracting of a random post
ndata = len(twenty_new_test.data)
test_new_query = twenty_new_test.data[round(random.random()) * (ndata - 1)]

lenguaje = "english"
limit = 400

corpus_task3 = twenty_new.data[:limit]

# Creating of a model TfidfVectorizer, training and predicting
vectorizer_task3 = TfidfVectorizer(min_df=1, smooth_idf=False, use_idf=False)
vectorizer_task3.fit(corpus_task3)

file = open("output2.txt", "w+")
file.write("Numbers of elements: {}\n\n".format(len(corpus_task3)))
file.close()

# Configuration and execution
cla1.tfidf_configuration(vectorizer_task3, cla1.simple_configuation, lenguaje)
cla2.training_and_predict(corpus_task3, vectorizer_task3, test_new_query)
cla1.tfidf_configuration(vectorizer_task3, cla1.euclidean_configuation, lenguaje)
cla2.training_and_predict(corpus_task3, vectorizer_task3, test_new_query)

# TASK 2
lenguaje = "spanish"
corpus1 = ["Juan quiere comprar un coche. Ana no quiere comprar ningún coche"]
corpus2 = ["Cargamento de oro dañado por el fuego",
           "la entrega de la plata llegó en un  camión de plata",
           "El cargamento de oro llegó en un camión"]
corpus3 = ["Éste texto no tiene nada que ver con los demás",
           "la plata fue entregada en camiones color plata",
           "El cargamento de oro llegó en un camión. El cargamento de oro llegó en un camión."
           " El cargamento de oro llegó en un camión",
           "Cargamentos de oro dañados por el fuego",
           "El cargamento de oro llegó en un camión"]
query = "oro plata camión"

corpus_task2 = corpus3  # you should change de corpus for other executions

file = open("output1.txt", "w+")
file.write("Numbers of elements: {}\n\n".format(len(corpus_task2)))
file.close()

# Creating of a model TfidfVectorizer, training and predicting
vectorizer = TfidfVectorizer(min_df=1, smooth_idf=False, use_idf=False)
vectorizer.fit(corpus_task2)
# Configuration and execution
cla1.simple_configuation(vectorizer)
cla1.training(corpus_task2, vectorizer, query)

cla1.euclidean_configuation(vectorizer)
cla1.training(corpus_task2, vectorizer, query)

cla1.stop_words_configuration(vectorizer, cla1.simple_configuation, lenguaje)
cla1.training(corpus_task2, vectorizer, query)

cla1.stop_words_configuration(vectorizer, cla1.euclidean_configuation, lenguaje)
cla1.training(corpus_task2, vectorizer, query)

query = "oro plat camion"
cla1.taking_root_words_configuration(vectorizer, cla1.simple_configuation, lenguaje)
cla1.training(corpus_task2, vectorizer, query)

cla1.taking_root_words_configuration(vectorizer, cla1.euclidean_configuation, lenguaje)
cla1.training(corpus_task2, vectorizer, query)

cla1.tfidf_configuration(vectorizer, cla1.simple_configuation, lenguaje)
cla1.training(corpus_task2, vectorizer, query)

cla1.tfidf_configuration(vectorizer, cla1.euclidean_configuation, lenguaje)
cla1.training(corpus_task2, vectorizer, query)

# TASK 1

data = load_iris()
data2 = [[51], [43], [62], [64], [45], [42], [46], [45], [45], [62], [47], [52], [64], [51], [65], [48], [49],
         [46], [64], [51], [52], [62], [49], [48], [62], [43], [40], [48], [64], [51], [63], [43], [65], [66],
         [65], [46], [39], [62], [64], [52], [63], [64], [48], [64], [48], [51], [48], [64], [42], [48], [41]]

k = 4
iterations = 4
my = cl.my_kmedias(data2)
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
my2 = cl.my_kmedias(data['data'][:, 0:3])
print("Euclidean distance: {}".format(my2.my_kmedias(k, my2.distance_euclidean, iterations)))
print("Groups: {}".format(my2.groups))
print("Manhattan distance: {}".format(my2.my_kmedias(k, my2.distance_manhattan, iterations)))
print("Groups: {}".format(my2.groups))
print("Maximo distance: {}".format(my2.my_kmedias(k, my2.distance_maximo, iterations)))
print("Groups: {}".format(my2.groups))
print("Hamming distance: {}".format(my2.my_kmedias(k, my2.distance_hamming, iterations)))
print("Groups: {}".format(my2.groups))
