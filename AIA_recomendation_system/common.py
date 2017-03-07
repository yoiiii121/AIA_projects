def mean_row(r):
    total = 0
    for i in r:
        if i is not None:
            total += i
    return total / len(r)


def read_data_file_with_recommendation(route, limits):
    infile = open(route, 'r')
    users = []
    items = []
    validations = []
    cont = 0
    for i in infile:
        values = i.split("\t")
        if cont <= limits:
            for j in range(len(values) - 1):
                if j == 0:
                    users.append(values[j])
                elif j == 1:
                    items.append(values[j])
                elif j == 2:
                    validations.append(values[j])
            cont += 1
        else:
            continue
    infile.close()
    set_users = list(set(users))
    set_items = list(set(items))
    u = {}
    item = {}
    cont = 0
    for i in set_users:
        u[i] = cont
        cont += 1
    cont = 0
    for i in set_items:
        item[i] = cont
        cont += 1
    create_table = []
    for _ in set_items:
        create_table_line = []
        for _ in set_users:
            create_table_line.append(0)
        create_table.append(create_table_line)
    for _ in users:
        for j in range(len(items)):
            index_u = u[users[j]]
            index_i = item[items[j]]
            create_table[index_i][index_u] = int(validations[j])
    return create_table


transactions = {}


def read_transactions_file_with_recommendation(route, limits, support_min):
    infile = open(route, 'r')
    cont = 0
    read_transactions = []
    for i in infile:
        if cont <= limits:
            line = i.split(" ")
            for j in line:
                read_transactions.append(j)
            cont += 1
        else:
            continue
    set_transactions = set(read_transactions)
    dict_transactions = {}
    for i in set_transactions:
        value = read_transactions.count(i)
        if value <= support_min:
            dict_transactions[i] = value

    return dict_transactions
