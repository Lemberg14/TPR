from prettytable import PrettyTable

def getFile():
    global text
    text = []
    with open("lab3.txt", "r") as file:
        lines = file.readlines()
        for i in lines:
            text.append(i.replace('\n', ''))
    for i in range(len(text)):
        text[i] = text[i].split(" ")

def List_Cand():
    global list_of_candidates
    list_of_candidates = []
    for i in range(1, len(text[0])):
        list_of_candidates.append(text[0][i])
    list_of_candidates.sort()


def Condorcet():
    global list_of_results_condorce
    list_of_results_condorce = []
    global result_condorce
    result_condorce = [0, 0]

    for i in list_of_candidates:
        compare = list_of_candidates.copy()
        compare.remove(i)
        amount_general = []

        for k in compare:
            amount = 0
            for z in range(len(text)):
                if text[z].index(i) < text[z].index(k):
                    amount += int(text[z][0])
            amount_general.append(amount)
        amount_general.sort()
        if amount_general[-1] > result_condorce[1]:
            result_condorce = [i, amount_general[-1]]
        list_of_results_condorce.append([i, amount_general[-1]])


def Borde():
    number_of_candidates = len(text[1])
    global list_of_results_borde
    list_of_results_borde = []
    global result_borde
    result_borde = [0, 0]

    for k in list_of_candidates:
        amount = 0
        for i in range(len(text)):
            amount += int(text[i][0]) * (number_of_candidates-text[i].index(k))
        if amount > result_borde[1]:
            result_borde = [k, amount]
        list_of_results_borde.append([k, amount])


getFile()
List_Cand()
Condorcet()
Borde()

table = PrettyTable(['Num of voters', 'A', 'B', 'C', "Results"])
for i in range(len(text)):
    row = []
    row.extend(text[i])
    row.append("")
    table.add_row(row)
table.add_row(['Condorce', list_of_results_condorce[0][1], list_of_results_condorce[1][1], list_of_results_condorce[2][1], result_condorce[0]])
table.add_row(['Borde', list_of_results_borde[0][1], list_of_results_borde[1][1], list_of_results_borde[2][1], result_borde[0]])
print(table)
