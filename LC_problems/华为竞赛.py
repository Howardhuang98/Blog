import numpy as np
import matplotlib.pyplot as plt
import re

host = {}
VM = {}
operations = {}

with open(r"G:\华为比赛\training-1.txt") as f:
    data = f.readlines()
    for row in data[1:81]:
        host[row[1:10]] = row[12:].strip(')\n').split(', ')
    for row in data[82:882]:
        VM[row[1:8]] = row[10:].strip(')\n').split(', ')
    day = 0
    for row in data[883:]:
        if re.match(r'^\d+$', row):
            day += 1
            operations[day] = []
        else:

            operations[day].append(row[1:].strip(')\n').split(', '))

print(host)
print(VM)
print(operations[4])


def operate(day, operations,installed_VM={}):
    operations_in_one_day = operations[day]
    for operation in operations_in_one_day:
        if operation[0] == 'add':
            installed_VM[operation[2]] = operation[1]
        if operation[0] == 'del':
            installed_VM.pop(operation[1])
    return installed_VM


if __name__ == '__main__':
    installed_VM = {}
    num_of_VM = []
    CPU = []
    mem = []
    for i in range(1,801):
        new = operate(i, operations,installed_VM)
        installed_VM.update(new)
        num_of_VM.append(len(installed_VM))
        num = 0
        for d in installed_VM.values():
            num += int(VM[d][0])
        CPU.append(num)
        num = 0
        for d in installed_VM.values():
            num += int(VM[d][1])
        mem.append(num)
    plt.figure()
    plt.subplot(131)
    plt.plot(num_of_VM)
    plt.subplot(132)
    plt.plot(CPU)
    plt.subplot(133)
    plt.plot(mem)
    plt.show()


