
def mean_row(r):
    total = 0
    for i in r:
        if i is not None:
            total += i
    return total / len(r)
