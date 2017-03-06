
import math as ma
import common as co



def sim_user(a, b):
    total1 = 0
    total2 = 0
    total3 = 0
    for i in range(len(a)):
        if a[i] is not None and b[i] is not None:
            total1 += (a[i] - co.mean_row(a)) * (b[i] - co.mean_row(b))
            total2 += ((a[i]) - co.mean_row(a)) ** 2
            total3 += ((b[i]) - co.mean_row(b)) ** 2
    return total1 / (ma.sqrt(total2) * ma.sqrt(total3))

def optimization_pred_user(pos_user,table,threshold):
    similarity = []
    for j in range(len(table)):
        if pos_user != j:
            similarity.append([sim_user(table[pos_user],table[j]),j])
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




def pred_user(a, p, table, threshold):
    total1 = 0
    total2 = 0
    sim_u = optimization_pred_user(a,table, threshold)
    total_mean = co.mean_row(table[a])
    for i in range(len(sim_u)):
        total1 += sim_u[i][0] * (table[sim_u[i][1]][p] - co.mean_row(table[sim_u[i][1]]))
        total2 += sim_u[i][0]
    return total_mean + (total1 / total2)
