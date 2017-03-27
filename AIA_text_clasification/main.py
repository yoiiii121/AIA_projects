import clustering as cl
import clasification_text_1 as cla1
import clasification_text_2 as cla2
from sklearn.datasets import load_iris,fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

# TASK 3

categories = ['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware',
              'comp.sys.mac.hardware', 'comp.windows.x', 'sci.space']
twenty_new = fetch_20newsgroups(subset='train',remove=('headers', 'footers', 'quotes'), categories=categories)

lenguage = "english"
limit = 100
corpus_task3 = twenty_new.data[:limit]

file = open("output2.txt", "w+")
file.write("Numbers of elements: {}\n\n".format(len(corpus_task3)))
file.close()



# TASK 2

corpus1 = ["Juan quiere comprar un coche. Ana no quiere comprar ningún coche"]
corpus2 = ["Cargamento de oro dañado por el fuego",
           "la entrega de la plata llegó en un  camión de plata",
           "El cargamento de oro llegó en un camión"]
corpus3 = ["Éste texto no tiene nada que ver con los demás",
           "la plata fue entregada en camiones color plata",
           "El cargamento de oro llegó en un camión. El cargamento de oro llegó en un camión. El cargamento de oro llegó en un camión",
           "Cargamentos de oro dañados por el fuego",
           "El cargamento de oro llegó en un camión"]

corpus_task2 = corpus3  # you should change de corpus for other executions

file = open("output1.txt", "w+")
file.write("Numbers of elements: {}\n\n".format(len(corpus_task2)))
file.close()


vectorizer = TfidfVectorizer(min_df=1, smooth_idf=False, use_idf=False)

cla1.simple_configuation(vectorizer)
cla1.training(corpus_task2, vectorizer)

cla1.euclidean_configuation(vectorizer)
cla1.training(corpus_task2, vectorizer)

cla1.stop_words_configuration(vectorizer, cla1.simple_configuation)
cla1.training(corpus_task2, vectorizer)

cla1.stop_words_configuration(vectorizer, cla1.euclidean_configuation)
cla1.training(corpus_task2, vectorizer)


cla1.taking_root_words_configuration(vectorizer, cla1.simple_configuation)
cla1.training(corpus_task2, vectorizer)

cla1.taking_root_words_configuration(vectorizer, cla1.euclidean_configuation)
cla1.training(corpus_task2, vectorizer)

cla1.tfidf_configuration(vectorizer, cla1.simple_configuation)
cla1.training(corpus_task2, vectorizer)

cla1.tfidf_configuration(vectorizer, cla1.euclidean_configuation)
cla1.training(corpus_task2, vectorizer)


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