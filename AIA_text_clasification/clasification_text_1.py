from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


# cosine similarity of two vectors v and w
def simility_cosine(v, w):
    total = 0.0
    total1 = 0.0
    total2 = 0.0
    for i in range(len(v)):
        total += v[i] * w[i]
        total1 += v[i] * v[i]
        total2 += w[i] * w[i]
    if total1 != 0.0:
        if total2 != 0.0:
            return total / total1 * total2
        else:
            return 0.0
    else:
        return 0.0


# Training corpus with a vectorizer configured, and using a query to determine the relevant text order
def training(corpus, vectorizer, query):
    file = open("output1.txt", "a+")

    print("Final configuration of vectorizer:\n{}".format(vectorizer))
    file.write("\nFinal configuration of vectorizer:\n{}".format(vectorizer))
    vectorizer_ntrain = vectorizer.fit_transform(corpus).toarray()
    vectorizer_query = vectorizer.transform([query]).toarray()

    similarity = {}
    if len(vectorizer_ntrain) > 1:
        print("Query:\n{}".format(query))
        file.write("\nQuery:\n{}".format(query))

        for i in range(len(vectorizer_ntrain)):
            for j in range(len(vectorizer_query)):
                similarity[simility_cosine(vectorizer_ntrain[i], vectorizer_query[j])] = i
        keys = sorted(similarity, reverse=True)
        cad = "["
        list_aux = []
        for i in keys:
            elem = similarity[i]
            if elem not in list_aux:
                cad += str(elem) + ", "
                list_aux.append(elem)
        cad = cad[:len(cad) - 2] + "]"
        print("Text order importance: {}".format(cad))
        file.write("\nText order importance: \n{}".format(cad))

    print("ID vectorizer:\n{}".format(vectorizer_ntrain))
    file.write("\nID vectorizer:\n{}".format(vectorizer_ntrain))

    print("Names process in the corpus:\n{}".format(vectorizer.get_feature_names()))
    file.write("\nNames process in the corpus:\n{}".format(vectorizer.get_feature_names()))

    file.close()
    print()
    print()


# Simple model
def simple_configuation(vectorizer):
    print("Using simple way")
    vectorizer.use_idf = False
    vectorizer.norm = None
    return vectorizer


# Simple model with normalized euclidean distance
def euclidean_configuation(vectorizer):
    print("Using normalized euclidean distance")
    vectorizer.norm = 'l2'
    vectorizer.use_idf = False
    vectorizer.sublinear_tf = False
    return vectorizer


# Using stop words
def stop_words_configuration(vectorizer, configuration, lenguaje):
    print("Using stop words")
    vectorizer.stop_words = stopwords.words(lenguaje)
    vectorizer = configuration(vectorizer)
    return vectorizer


# Taking root words
def taking_root_words_configuration(vectorizer, configuration, lenguaje):
    print("Taking root words")
    vectorizer = stop_words_configuration(vectorizer, configuration, lenguaje)
    stemmer = SnowballStemmer(lenguaje)
    vectorizer.stop_words = set([stemmer.stem(i) for i in vectorizer.stop_words])

    vectorizer.vocabulary = set([stemmer.stem(i) for i in vectorizer.get_feature_names()])
    return vectorizer


# using weight tfidf
def tfidf_configuration(vectorizer, configuration, lenguaje):
    print("Using tfidf")
    vectorizer = taking_root_words_configuration(vectorizer, configuration, lenguaje)
    vectorizer.smooth_idf = True
    vectorizer.use_idf = True
    vectorizer.sublinear_tf = True
    return vectorizer
