transactions = {}


def read_transactions_file_with_recommendation(route, limits):
    infile = open(route, 'r')
    cont = 0
    transactions_list = []
    for i in infile:
        if cont <= limits:
            if i != "":
                i = i.replace("\n", "")
                transactions_list.append(i)
                cont += 1
        else:
            continue
    return transactions_list


def first_candidate(transactions_list, support_min):
    set_transactions = set(transactions_list)
    dict_transactions = {}

    for i in set_transactions:
        line = i.split(" ")
        value = 0
        for l in line:
            if l != "":
                for k in range(len(transactions_list)):
                    value += transactions_list[k].count(l)
                if value >= support_min:
                    dict_transactions[l] = value

    return dict_transactions


def candidate_generator(candidates_list):
    generate = []
    if candidates_list is not None:
        for i in candidates_list.keys():
            for j in candidates_list.keys():
                generate.append(i + "-" + j)
    return generate


def candidate_filter(candidates_list, transactions_list, support_min):
    pass
