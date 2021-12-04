from prettytable import PrettyTable

def getFile():
    text = []
    with open("lab4.txt", "r") as file:
        lines = file.readlines()
        for i in lines:
            text.append(i.replace('\n', ''))
    for i in range(len(text)):
        text[i] = text[i].split(" ")
    return text

def evaluate(array):
    for i in array:
        for j in range(1, len(i)):
            i[j] = round(i[j] * i[0], 2)
    return array

def sum_of_column(array):
    return [sum(col) for col in zip(*array)]

array = getFile()
array = [[int(j) if '.' not in j else float(j) for j in i] for i in array]

table = PrettyTable(['№', 'Parameter', 'Weight', 'A Croatia', 'B Turkey', 'C Egypt', 'D OAE', 'E Portugal'])
table.add_row([1, 'Arrival', array[0][0], array[0][1], array[0][2], array[0][3], array[0][4], array[0][5]])
table.add_row([2, 'Cost', array[1][0], array[1][1], array[1][2], array[1][3], array[1][4], array[1][5]])
table.add_row([3, 'Avg sea temperature',       array[2][0], array[2][1], array[2][2], array[2][3], array[2][4], array[2][5]])
table.add_row([4, 'Scenery', array[3][0], array[3][1], array[3][2], array[3][3], array[3][4], array[3][5]])
table.add_row([5, 'Architecture', array[4][0], array[4][1], array[4][2], array[4][3], array[4][4], array[4][5]])
table.add_row(['Sum', '', 1, '', '', '', '', ''])

print(table)

print("\n Calculated table:")
array = evaluate(array)
total = [round(i, 3) for i in sum_of_column(array)]

table = PrettyTable(['№', 'Parameter', 'Weight', 'A Croatia', 'B Turkey', 'C Egypt', 'D OAE', 'E Portugal'])
table.add_row([1, 'Arrival', array[0][0], array[0][1], array[0][2], array[0][3], array[0][4], array[0][5]])
table.add_row([2, 'Cost', array[1][0], array[1][1], array[1][2], array[1][3], array[1][4], array[1][5]])
table.add_row([3, 'Avg sea temperature',       array[2][0], array[2][1], array[2][2], array[2][3], array[2][4], array[2][5]])
table.add_row([4, 'Scenery', array[3][0], array[3][1], array[3][2], array[3][3], array[3][4], array[3][5]])
table.add_row([5, 'Architecture', array[4][0], array[4][1], array[4][2], array[4][3], array[4][4], array[4][5]])
table.add_row(['Sum', '', total[0], total[1], total[2], total[3], total[4], total[5]])
print(table)

objects = ['A Croatia', 'B Turkey', 'C Egypt', 'D OAE', 'E Portugal']
total.pop(0)
print("\tChoice:", objects[total.index(max(total))], 'with mark -', max(total))
