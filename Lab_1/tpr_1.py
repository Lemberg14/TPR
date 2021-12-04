from prettytable import PrettyTable

def read_file():
    with open('lab1.txt', 'r') as f:
        arr1 = [[float(num) for num in line.split(' ')] for line in f]
    return arr1

def valds_method(array1, array2, best_option):
    arr = []
    for i in range(len(array1)):
        array2[i].append(min(array1[i]))
        arr.append(array2[i][-1])
    best_option.append(arr.index(max(arr))+1)

def laplas_method(array1, array2, best_option):
    arr = []
    for i in range(len(array1)):
        array2[i].append(round(sum(array1[i])/3, 1))
        arr.append(array2[i][-1])
    best_option.append(arr.index(max(arr))+1)


def gurvic_method(array1, array2, best_option):
    arr = []
    for i in range(len(array1)):
        array2[i].append(min(array1[i])*0.6+max(array1[i])*0.4)
        arr.append(array2[i][-1])
    best_option.append(arr.index(max(arr))+1)


def baes_laplas_method(array1, array2, best_option):
    arr = []
    for i in range(len(array1)):
        array2[i].append(array1[i][0]*0.55 + array1[i][1] * 0.3 + array1[i][2] * 0.15)
        arr.append(array2[i][-1])
    best_option.append(arr.index(max(arr))+1)

array1 = read_file()
array2 = read_file()
best_option = []
valds_method(array1, array2, best_option)
laplas_method(array1, array2, best_option)
gurvic_method(array1, array2, best_option)
baes_laplas_method(array1, array2, best_option)

print("Matrix")
table = PrettyTable()
table.field_names = ("A/P", "P1", "P2", "P3", "Valda", "Laplasa", "Gurvica", "Baesa")
for i in range(len(array2)):
    row = [f"A{i}"]
    row.extend(array2[i])
    table.add_row(row)
table.add_row(["", "", "", "", best_option[0], best_option[1], best_option[2],best_option[3]])
print(table)

