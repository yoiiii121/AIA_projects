def read_transactions_file_with_recommendation(route, limits):
    infile = open(route, 'r')
    cont = 0
    transactions_list = []
    for i in infile:
        if cont <= limits:
            transactions_list.append(i[0:len(i) - 2])
            cont += 1
        else:
            continue
    return transactions_list


def first_candidate(transactions_list, support_min):
    set_transactions = set(transactions_list)
    dict_transactions = {}

    for i in set_transactions:
        line = i.split(" ")

        for l in line:
            value = 0
            for k in range(len(transactions_list)):
                value += transactions_list[k].count(l)
            if value >= support_min:
                dict_transactions[l] = value
    return dict_transactions


def string_sort(string):
    string_l = string.split(" ")
    size = len(string_l)
    cad = ""
    for i in range(size):
        minimum = 99999
        for k in range(len(string_l)):

            if str(string_l[k]) != "" and int(string_l[k]) <= int(minimum):
                minimum = string_l[k]
        string_l.remove(minimum)
        cad += str(minimum) + " "
    return cad[0:len(cad) - 1]


def candidate_generator(candidates_list):
    generate = []

    if candidates_list is not None:
        key_list = list(candidates_list.keys())
        for i in range(len(key_list) - 1):
            for j in range(i + 1, len(key_list)):
                generate.append(string_sort(str(key_list[i]) + " " + str(key_list[j])))
    for i in range(len(generate)):
        aux = []
        cad = ""
        for j in generate[i].split(" "):
            if j not in aux:
                aux.append(j)
                cad += j + " "

        generate[i] = cad[0:len(cad) - 1]
    return list(set(generate))


def candidates_filter(candidates_list, transactions_list, support_min, step):
    dict_transactions = {}
    list_match = []

    for i in candidates_list:
        for j in i.split(" "):
            list_match_line = []
            for k in range(len(transactions_list)):
                if j in transactions_list[k]:
                    list_match_line.append(k)
            list_match.append(list_match_line)

    for i in range(0, len(candidates_list), step):
        if i % step == 0:
            for j in list_match:
                cont = 1
                for k in range(step - 1):
                    if j in list_match:
                        cont += 1
                if cont >= support_min:
                    dict_transactions[candidates_list[i]] = cont
    return dict_transactions


def association_rules(candidates_all_matches, transactions_, confidence_min):
    dict_association = {}
    for i in range(len(candidates_all_matches)):
        for j in candidates_all_matches[i].keys():
            for k in candidates_all_matches[0].keys():
                if j != k:
                    dict_association[j] = k
    aux = []
    for i, j in dict_association.items():
        for i1 in i.split(" "):
            if i1 in j:
                aux.append(i)

    for i in aux:
        del dict_association[i]

    dict_support = {}

    for j, k in dict_association.items():
        cont_ext = 0
        for i in transactions_:

            cont = 0
            for i1 in i.split(" "):
                if i1 in j or i1 in k:
                    cont += 1
                else:
                    cont = 0
            if cont == len(j) + len(k) - 2:
                cont_ext += 1
        if confidence_min <= cont_ext:
            dict_support[j + " " + k] = cont_ext
    return dict_support


def apriori_algorithm(dir_name, f, limits_elements_reads, support_min, confidence_min, t):
    k = 0
    if t is None:
        transactions = read_transactions_file_with_recommendation(dir_name + f, limits_elements_reads)
    else:
        transactions = t
    print("Transactions: {}".format(transactions))
    candidates = {"a"}
    candidates_all_matches = []
    while candidates != {}:
        if k != 0:

            generator = candidate_generator(candidates)
            print("Candidate generator: {}".format(generator))
            candidates = candidates_filter(generator, transactions, support_min, k + 1)
            print("Candidate: {}".format(candidates))
            candidates_all_matches.append(candidates)
        else:
            print("Wait for the operations:")
            candidates = first_candidate(transactions, support_min)
            print("Candidate: {}".format(candidates))
            candidates_all_matches.append(candidates)
        k += 1
    print("Frequent values: {}".format(candidates_all_matches))
    association = association_rules(candidates_all_matches, transactions, confidence_min)
    print("Association rules: {}:".format(association))
    return association
