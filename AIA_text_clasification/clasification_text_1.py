
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


def simility_cosine(v, w):
    total = 0.0
    total1 = 0.0
    total2 = 0.0
    for i in range(len(v)):
        total += (v[i] * w[i])
        total1 += v[i] ** 2
        total2 += w[i] ** 2
    if total1 != 0.0:
        if total2 != 0.0:
            return total / total1 * total2
        else:
            return 0.0
    else:
        return 0.0

def training(corpus, vectorizer):
    file = open("output1.txt", "a+")

    print("Final configuration of vectorizer:\n{}".format(vectorizer))
    file.write("\nFinal configuration of vectorizer:\n{}".format(vectorizer))

    vectorizer_ntrain = vectorizer.fit_transform(corpus).toarray()
    similarity = {}
    if(len(vectorizer_ntrain)>1):
        for i in range(len(vectorizer_ntrain)-1):
            for j in range(i+1,len(vectorizer_ntrain)):
                similarity[simility_cosine(vectorizer_ntrain[i],vectorizer_ntrain[j])] = [i,j]
        keys=sorted(similarity, reverse=True)
        cad = "["
        list_aux = []
        for i in keys:
            elem = similarity[i]
            if elem[0] not in list_aux:
                cad += str(elem[0]) + ", "
                list_aux.append(elem[0])
            elif elem[1] not in list_aux:
                cad += str(elem[1]) + ", "
                list_aux.append(elem[1])
        cad = cad[:len(cad) - 2] + "]"
        print("Text order importance: {}".format(cad))
        file.write("Text order importance: \n{}".format(cad))

    print("ID vectorizer:\n{}".format(vectorizer_ntrain))
    # file.write("ID vectorizer:\n{}".format(vectorizer_fit))


    print("Names process in the corpus:\n{}".format(vectorizer.get_feature_names()))
    # file.write("Names process in the corpus:\n{}".format(vectorizer.get_feature_names()))

    file.close()
    print()
    print()


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

# using weight tfidf
def tfidf_configuration(vectorizer, configuration):
    print("Using tfidf")
    vectorizer = taking_root_words_configuration(vectorizer, configuration)
    vectorizer.smooth_idf = True
    vectorizer.use_idf = True
    vectorizer.sublinear_tf = True
    return vectorizer