import math as ma

import common as co


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]


def sim_item(p, q):
    total1 = 0
    total2 = 0
    total3 = 0
    for i in range(len(p)):
        if p[i] is not None and q[i] is not None:
            total1 += (p[i] - co.mean_row(p)) * (q[i] - co.mean_row(q))
            total2 += (p[i] - co.mean_row(p)) ** 2
            total3 += (q[i] - co.mean_row(q)) ** 2
    return total1 / (ma.sqrt(total2) * ma.sqrt(total3))


def optimization_prediction_item(pos_item, table, threshold):
    similarity = []
    for j in range(len(table)):
        if pos_item != j:
            value = sim_item(table[pos_item], table[j])
            if threshold <= value:
                similarity.append([value, j])
    # sort = []
    # size_similarity = len(similarity)

    # for i in range(size_similarity):
    #    max_number = -2.0
    #    position = -2
    #    for j in range(len(similarity)):
    #        value = similarity[j][0]
    #        if value >=max_number:
    #            max_number = value
    #            position = j
    #            if threshold <= value:
    #                sort.append([value,similarity[j][1]])
    #   similarity[position] = [-1.0,position]
    # return sort
    return similarity


def prediction_item(q, p, table, threshold):
    total1 = 0
    total2 = 0
    sim_i = optimization_prediction_item(q, table, threshold)
    for i in range(len(sim_i)):
        total1 += sim_i[i][0] * table[sim_i[i][1]][p]
        total2 += sim_i[i][0]
    if total2 == 0:
        print("threshold is too high")
        return None
    return total1 / total2
