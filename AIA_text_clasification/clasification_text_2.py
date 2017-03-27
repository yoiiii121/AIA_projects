from sklearn.cluster import KMeans
import clasification_text_1 as cla1

def precision(true_positive, positive):
    if positive > 0:
        return true_positive/positive
    else:
        return -1


def recall(true_positive, true_positive_false_negative):
    if true_positive_false_negative > 0:
        return true_positive/true_positive_false_negative
    else:
        return -1

def training(corpus, vectorizer):
    file = open("output2.txt", "a+")

    print("Final configuration of vectorizer:\n{}".format(vectorizer))
    file.write("\nFinal configuration of vectorizer:\n{}".format(vectorizer))

    vectorizer_ntrain = vectorizer.fit_transform(corpus).toarray()
    kmeans = KMeans(n_clusters=6, init="k-means++", random_state=0, precompute_distances="auto", max_iter=100,
                    algorithm="auto", n_jobs=-2, tol=0.0).fit(vectorizer_ntrain)
    label = kmeans.labels_

    print("Cluster centers:\n{}".format(kmeans.cluster_centers_))
    # file.write("Cluster centers:\n{}".format(kmeans.cluster_centers_))

    print("ID vectorizer:\n{}".format(vectorizer_ntrain))
    # file.write("ID vectorizer:\n{}".format(vectorizer_fit))

    similarity = []
    for i in range(len(kmeans.cluster_centers_)):
        similarity_ = []
        for j in range(len(vectorizer_ntrain)):
            if label[j] == i:
                similarity_.append(cla1.simility_cosine(vectorizer_ntrain[j], kmeans.cluster_centers_[i]))
        similarity.append(sorted(similarity_, reverse=True))
        true_positive = 0
        cont_all = 0
        for i in range(len(similarity)):
            for j in range(len(similarity[i])):
                cont_all += 1
                if similarity[i][j] >= 0.5:
                    true_positive += 1

        print("Precision: {}".format(precision(true_positive, cont_all)))
        file.write("Precision:\n{}".format(precision(true_positive, cont_all)))

    # print(metrics.average_precision_score(label, predict))
    similarity = similarity[0:3]
    importance = {}
    for i in range(len(similarity)):
        total = sum(similarity[i])
        importance[total / len(similarity[i])] = i
    keys = sorted(importance)
    cad = "["
    for i in keys:
        cad += str(importance[i]) + ", "
    cad = cad[:len(cad) - 2] + "]"
    print("Text order importance: {}".format(cad))
    file.write("Text order importance: \n{}".format(cad))

    print("Names process in the corpus:\n{}".format(vectorizer.get_feature_names()))
    # file.write("Names process in the corpus:\n{}".format(vectorizer.get_feature_names()))

    file.close()
    print()
    print()


