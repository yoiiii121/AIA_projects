from sklearn.cluster import KMeans

import clasification_text_1 as cla1


# Training corpus with a vectorizer configured, and using a kmeans classification to determine the relevant
#  text order and prediction of a random post in similary post of the corpus
def training_and_predict(corpus, vectorizer, query):
    file = open("output2.txt", "a+")

    print("Final configuration of vectorizer:\n{}".format(vectorizer))
    file.write("\nFinal configuration of vectorizer:\n{}".format(vectorizer))

    vectorizer_ntrain = vectorizer.fit_transform(corpus).toarray()
    query_train = vectorizer.transform([query]).toarray()
    kmeans = KMeans(n_clusters=30, init="k-means++", random_state=0, precompute_distances="auto", max_iter=100,
                    algorithm="auto", n_jobs=-2, tol=0.0).fit(vectorizer_ntrain)
    print("Final configuration of kmeans:\n{}".format(kmeans))
    file.write("\nFinal configuration of kmeans:\n{}".format(kmeans))

    kmeans_query = kmeans.predict(query_train)[0]
    print("kmeans Prediction of the random query:\n{}".format(kmeans_query))
    file.write("\n kmeans Prediction of the random query:\n{}".format(kmeans_query))
    list_aux = []
    similarity = {}
    if len(vectorizer_ntrain) > 1:
        for i in range(len(vectorizer_ntrain)):
            similarity[cla1.simility_cosine(vectorizer_ntrain[i], kmeans.cluster_centers_[kmeans_query])] = i
        keys = sorted(similarity, reverse=True)
        keys = keys[0:10]
        cad = "["
        for i in keys:
            elem = similarity[i]
            if elem not in list_aux:
                cad += str(elem) + ", "
                list_aux.append(elem)
        cad = cad[:len(cad) - 2] + "]"

        print("Text order importance: {}".format(cad))
        file.write("Text order importance: \n{}".format(cad))

    print("Names of the texts select in corpus:\n{}".format(query))
    file.write("Names of the text in select in the corpus:\n{}".format(query))
    for i in list_aux[0:4]:
        print("POST {}".format(i))
        print("Names of the texts select in corpus:\n{}".format(corpus[i]))
        file.write("POST {}".format(i))
        file.write("Names of the text in select in the corpus:\n{}".format(corpus[i]))
    file.close()
    print()
    print()
