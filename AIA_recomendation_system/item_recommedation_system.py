
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
"""

def pred_item(q, p):
    total1 = 0
    total2 = 0
    for i in range(len(q[p])):
        for j in range(len(q[p])):
            if i != j:
                total1 += sim_item(q[i], q[j]) * q[p][j]
                total2 += sim_item(q[i], q[j])
    return total1 / total2
"""