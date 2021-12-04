from prettytable import PrettyTable
from itertools import chain
import copy

def getFile():
    global text
    text = []

    with open("lab5.txt", "r") as file:
        lines = file.readlines()
        for i in lines:
            text.append(i.replace('\n', ''))
    for i in range(len(text)):
        text[i] = text[i].split(" ")

    global text1
    text1 = copy.deepcopy(text)

def simplify_max():
    mas = []

    for i in range(len(text1)):
        res = chain(range(0, i), range(i+1, len(text1)))
        for k in res:
            check = True
            for z in range(len(text1[k])):
                if int(text1[i][z]) >= int(text1[k][z]):
                    check = False
            if check:
                mas.append(i)

    counter = 0
    for i in mas:
        text1.pop(i-counter)
        mas_for_max.pop(i-counter)
        counter += 1

    if counter > 1:
        simplify_min()

def simplify_min():
    mas = []

    for i in range(len(text1[0])):
        res = chain(range(0, i), range(i+1, len(text1[0])))
        for k in res:
            check = True
            for z in range(len(text1)):
                if int(text1[z][i]) < int(text1[z][k]):
                    check = False
                    break
            if check:
                mas.append(i)

    mas = list(set(mas))
    counter = 0

    for i in mas:
        [j.pop(i-counter) for j in text1]
        mas_for_min.pop(i-counter)
        counter+=1

    if counter > 1:
        simplify_max()

def count_solution():
    global p1, p2, sum_p
    p1 = int(text1[1][0]) - int(text1[0][0])
    p2 = int(text1[0][1]) - int(text1[1][1])

    for i in range(1, p1+p2):
        if p1 % i == 0:
            if p2 % i == 0:
                p1 /= i
                p2 /= i

    sum_p = p1 + p2

    p1_counted = (sum_p - p1) / sum_p
    p2_counnted = (sum_p - p2) / sum_p

    solution = int(text1[0][0]) * p1_counted + int(text1[0][1]) * p2_counnted
    return solution

def other_strategy():
    p1_str = str(abs(int(sum_p - p1))) + "/" + str(abs(int(sum_p)))
    p2_str = str(abs(int(sum_p - p2))) + "/" + str(abs(int(sum_p)))

    global mas_for_max_zeros, mas_for_min_zeros
    mas_for_max_zeros = [0, 0, 0, 0, 0]
    mas_for_min_zeros = [0, 0, 0, 0, 0]
    mas_for_max_zeros[mas_for_max[0]] = p1_str
    mas_for_max_zeros[mas_for_max[1]] = p2_str
    mas_for_min_zeros[mas_for_min[0]] = p1_str
    mas_for_min_zeros[mas_for_min[1]] = p2_str


mas_for_max = [0, 1, 2, 3, 4]
mas_for_min = [0, 1, 2, 3, 4]
getFile()
simplify_max()
simplify_min()

text1.pop(1)
mas_for_max.pop(1)


solution = count_solution()
other_strategy()

table = PrettyTable(['Players', 'B1', 'B2', 'B3', 'B4','B5'])
for i in range(len(text)):
    table.add_row([f'A{i+1}', text[i][0], text[i][1], text[i][2], text[i][3], text[i][4]])
print(table)

if len(text1) > 1:
    table2 = PrettyTable(['Players', 'B1', 'B2', 'B3', 'B4','B5', 'Vector'])
    for i in range(len(text)):
        table2.add_row([f'A{i+1}', text[i][0], text[i][1], text[i][2], text[i][3], text[i][4], mas_for_max_zeros[i]])
    table2.add_row(['Vector', mas_for_min_zeros[0], mas_for_min_zeros[1], mas_for_min_zeros[2], mas_for_min_zeros[3], mas_for_min_zeros[4], ''])
    print('\n', table2)

    print("\nSimplified table 2x2:")
    table3 = PrettyTable(['Players', 'B1', 'B2'])
    for i in range(len(text1)):
            table3.add_row([f'A{i+1}', text1[i][0], text1[i][1]])
    print(table3)


    print("\nThe result of this matrix game =", round(solution, 3))
