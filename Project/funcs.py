from prettytable import PrettyTable

def getSDNFarray(strr):
    res = []
    pos = 0

    for x in range(-1, 2, 2):
        for y in range(-1, 2, 2):
            for z in range(-1, 2, 2):
                for w in range(-1, 2, 2):
                    if strr[pos] == '1':
                        res.append([x,y,z,w])

                    pos += 1

    return res

def getSKNFarray(strr):
    res = []
    pos = 0

    for x in range(-1, 2, 2):
        for y in range(-1, 2, 2):
            for z in range(-1, 2, 2):
                for w in range(-1, 2, 2):
                    if strr[pos] == '0':
                        res.append([x, y, z, w])

                    pos += 1

    return res


def getStringValue(arr):
    res = ''

    for i in range(4):
        if arr[i] != 0:
            match i:
                case 0:
                    res += 'x'
                case 1:
                    res += 'y'
                case 2:
                    res += 'z'
                case 3:
                    res += 'w'

            if arr[i] == -1:
                res += '\u0305'

    return res

def printOne(arr):
    print(getStringValue(arr), end='')


def printStatment(arr):
    for sub in arr[:-1]:
        printOne(sub)
        print(' V ', end='')

    printOne(arr[-1])
    print()

def printOneSKNF(arr):
    for i in range(4):
        if arr[i] != 0:
            match i:
                case 0:
                    print('x', end='')
                case 1:
                    print('y', end='')
                case 2:
                    print('z', end='')
                case 3:
                    print('w', end='')

            if arr[i] == 1:
                print('\u0305', end='')

            if i != 3:
                print(' V ', end='')


def printSKNF(arr):
    print('СКНФ: ', end='')

    for sub in arr:
        print('(', end='')
        printOneSKNF(sub)
        print(')', end='')

    print()

def connect(arr1, arr2):
    count = 0
    res = []
    for i in range(4):

        if arr1[i] == 0 or arr2[i] == 0:
            if arr1[i] == 0 and arr2[i] == 0:
                res.append(0)
            else:
                return False, []

        elif arr1[i] != arr2[i]:
            count += 1
            res.append(0)
        else:
            res.append(arr1[i])

    if count == 1:
        return True, res

    return False, []


def minimize_step(arr):
    new_arr = []

    was_used = [0 for _ in range(len(arr))]

    minimize_possible = False
    for i in range(len(arr)):

        j = i + 1

        while j < len(arr):

            par = connect(arr[i], arr[j])

            if par[0]:
                was_used[i] = 1
                was_used[j] = 1
                minimize_possible = True
                new_arr.append(par[1])

            j += 1

        if j == len(arr) and was_used[i] == 0:
            new_arr.append(arr[i])

    return minimize_possible, new_arr


def compress_duplicate(arr):
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                arr.pop(j)
            else:
                j += 1

        i += 1


def minimize(arr):
    res = arr

    minimize_possible = True

    while minimize_possible:
        sub_res = minimize_step(res)

        if not sub_res[0]:
            minimize_possible = False
        else:
            res = sub_res[1]

    compress_duplicate(res)

    return res

def compare(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] != 0 and arr2[i] != 0 and arr1[i] != arr2[i]:
            return False

    return True


def form_content(arr):
    content = []

    pos = 0

    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    content.append([x, y, z, w, arr[pos]])
                    pos += 1

    return content

def print_value_table(arr):
    table_content = form_content(arr)

    header_values = ['x', 'y', 'z', 'w', 'func']

    columns = len(header_values)

    table = PrettyTable(header_values)

    while table_content:
        table.add_rows(table_content[:columns])
        table_content = table_content[columns:]

    print(table)


def get_implication_table(base, res):
    compare_data = []
    for res_obj in res:
        single_data = [getStringValue(res_obj)]

        for base_obj in base:
            if compare(res_obj, base_obj):
                single_data.append('+')
            else:
                single_data.append('')

        compare_data.append(single_data)

    return compare_data


def print_implication_table(base, res):
    table_content = get_implication_table(base, res)

    header_values = ['Values']

    for base_obj in base:
        header_values.append(getStringValue(base_obj))

    columns = len(header_values)

    table = PrettyTable(header_values)

    while table_content:
        table.add_rows(table_content[:columns])
        table_content = table_content[columns:]

    print(table)
