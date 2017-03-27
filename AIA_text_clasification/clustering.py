import random as ra
import numpy as np


class my_kmedias():
    def __init__(self, data):
        self.data = data
        self.groups = []

    # Mean of a vector
    def mean(self, list_elem):
        total = 0
        for i in list_elem:
            total += i
        return total / len(list_elem)

    # Euclidean distance of two vectors, an instance vector and a centroid vector
    def distance_euclidean(self, data, mean_value):
        total = 0
        for i in range(0, len(data)):
            total += (data[i] - mean_value[i]) ** 2
        return np.sqrt(total)

    # Manhattan distance of two vectors, an instance vector and a centroid vector
    def distance_manhattan(self, data, mean_value):
        total = 0
        for i in range(0, len(data)):
            total += np.fabs(data[i] - mean_value[i])
        return total

    # Maximo distance of two vectors, an instance vector and a centroid vector
    def distance_maximo(self, data, mean_value):
        total = 0
        for i in range(0, len(data)):
            aux = np.fabs(data[i] - mean_value[i])
            if total < aux:
                total = aux
        return total

    # Hamming distance of two vectors, an instance vector and a centroid vector
    def distance_hamming(self, data, mean_value):
        return (np.array(data) != np.array(mean_value)).mean()

    # K medias of group of samples, with k groups defined, a distance function and a number of iterations
    def my_kmedias(self, k, distance, iterations):
        centroids_list = []
        repeat = True
        group = 0

        # Initializing of a group centroids
        l = []
        size = len(self.data) - 1
        for i in range(k):
            centroids_list_ = []
            for j in range(len(self.data[0])):
                aux = ra.randint(0, size)
                boolean = True
                while boolean:
                    aux = ra.randint(0, size)
                    if aux not in l:
                        l.append(aux)
                        boolean = False
                centroids_list_.append(round(float(self.data[aux][j]), 1))
            centroids_list.append(centroids_list_)
        # Repeating of calculating samples and centroids distances and calculating new centroids
        cont = 0
        while repeat:
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
                # Adding number elements of the groups
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
            # Stopping the loop
            if iterations - 1 == cont:
                repeat = False
            if centroids_list == centroids_list2:
                repeat = False
            # Replacing from last groups of centroids to news
            centroids_list = centroids_list2.copy()
            cont += 1

        return centroids_list
