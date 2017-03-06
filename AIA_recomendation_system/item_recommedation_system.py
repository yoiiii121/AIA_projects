
import math as ma
import common as co

def transpuesta(matriz):
    rows = len(matriz)
    cols = len(matriz[0])
    return [[matriz[j][i] for j in range(rows)] for i in range(cols)]



def sim_item(p, q):
    total1 = 0
    total2 = 0
    total3 = 0
    for i in range(len(p)):
        if p[i] is not None and q[i]is not None:
            total1 += (p[i] - co.mean_row(p)) * (q[i] - co.mean_row(q))
            total2 += (p[i] - co.mean_row(p)) ** 2
            total3 += (q[i] - co.mean_row(q)) ** 2
    return total1 / (ma.sqrt(total2) * ma.sqrt(total3))

def optimization_pred_item(pos_item,table,threshold):
    similarity = []
    for j in range(len(table)):
        if pos_item != j:
            similarity.append([sim_item(table[pos_item],table[j]),j])
    sort = []
    size_similarity = len(similarity)

    for i in range(size_similarity):
        max_number = -2.0
        position = -2
#        value = 0.0
        for j in range(len(similarity)):
            value = similarity[j][0]
            if value >=max_number:
                max_number = value
                position = j
                if threshold <= value:
                    sort.append([value,similarity[j][1]])
        similarity[position] = [-1.0,position]
    return sort


def pred_item(q, p, table, threshold):
    total1 = 0
    total2 = 0
    sim_i = optimization_pred_item(q,table,threshold)
    for i in range(len(sim_i)):
        total1 += sim_i[i][0] * table[sim_i[i][1]][p]
        total2 += sim_i[i][0]
    return total1 / total2
