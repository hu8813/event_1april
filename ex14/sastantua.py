#!/usr/bin/python3
import sys

def sastantua(size):
    for i in range(size):
        base = i * 2 + 5 if i % 2 == 0 else i * 2 + 4
        for j in range(i + 2):
            width = base + j * 2
            door = i if j == i + 1 else -1
            for k in range(i + 3):
                row_width = width + k * 2
                if door >= 0 and k == i + 2 - door // 2:
                    print('|' + '$' * door + '|' + '*' * (row_width - door - 2) + '|')
                else:
                    print('|' + '*' * (row_width - 2) + '|')
        print('-' * (width + 2))

try:
    n = sys.argv[1]
    if len(sys.argv) != 2 or n == "" or n.strip() == "" or int(n) < 0:
        exit()
    n = int(n)
    sastantua(n)
    
except:
    exit()