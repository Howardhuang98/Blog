import sys

for line in sys.stdin:
    ops = line.split(";")
    pos = [0, 0]
    for op in ops:
        if 2 <= len(op) <= 3:
            if op[0] in ['A', 'S', 'W', 'D'] and op[1:].isdigit():
                if op[0] == 'A':
                    pos[0] -= int(op[1:])
                elif op[0] == 'D':
                    pos[0] += int(op[1:])
                elif op[0] == 'W':
                    pos[1] += int(op[1:])
                elif op[0] == 'S':
                    pos[1] -= int(op[1:])
    print(str(pos[0])+","+str(pos[1]))
