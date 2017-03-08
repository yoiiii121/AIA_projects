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
    string = string.split(" ")
    size = len(string)
    cad = ""
    for i in range(size):
        minimun = 99999
        for k in range(len(string)):

            if str(string[k]) != "" and int(string[k]) <= int(minimun):
                minimun = string[k]
        string.remove(minimun)
        cad += str(minimun) + " "
    return cad[0:len(cad) - 1]


def candidate_generator(candidates_list):
    generate = []

    if candidates_list is not None:
        key_list = list(candidates_list.keys())
        for i in range(len(key_list) - 1):
            for j in range(i + 1, len(key_list)):
                generate.append(string_sort(str(key_list[i]) + " " + str(key_list[j])))
    aux = []
    for i in range(len(generate)):
        aux = []
        cad = ""
        for j in generate[i].split(" "):
            if not j in aux:
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


def Apriori_algorithm(dir, f, limits_elements_reads, support_min, t):
    k = 0
    transactions = []
    candidates = ["a"]
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

            if t is None:
                transactions = read_transactions_file_with_recommendation(dir + f, limits_elements_reads)
            else:
                transactions = t
            print("transactions: {}".format(transactions))
            candidates = first_candidate(transactions, support_min)
            print("Candidate: {}".format(candidates))
            candidates_all_matches.append(candidates)
        k += 1
    return candidates_all_matches
