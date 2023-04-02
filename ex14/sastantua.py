#!/usr/bin/python3
import sys

def calc_base(size):
    floor = 1
    width = 1
    floor_step = 4
    while floor <= size:
        width += 2 * (2 + floor)
        floor += 1
        width += floor_step
        if floor % 2 and floor < size:
            floor_step += 2
    width -= floor_step
    return width

def put_line(space):
    pos = 0
    while pos < space:
        print(' ', end='')
        pos += 1

def put_blocks(size, floor, width, step):
    door = 1 + 2 * ((floor - 1) // 2)
    pos = 0
    while pos < width:
        if pos == 0:
            print('/', end='')
        elif pos == width - 1:
            print('\\', end='')
        else:
            if floor == size and (width - door) // 2 <= pos < (width + door) // 2 and 2 + floor - step <= door:
                if door >= 5 and step == 2 + floor - door // 2 - 1 and pos == (width + door) // 2 - 2:
                    print('$', end='')
                else:
                    print('|', end='')
            else:
                print('*', end='')
        pos += 1

def sastantua(size):
    if size < 1:
        return
    floor = 1
    width = 1
    while floor <= size:
        height = 2 + floor
        step = 0
        while step < height:
            width += 2
            put_line((calc_base(size) - width) // 2)
            put_blocks(size, floor, width, step)
            print()
            step += 1
        floor += 1
        width += 4 + 2 * ((floor - 2) // 2)

try:
    n = sys.argv[1]
    if len(sys.argv) != 2 or n == "" or n.strip() == "" or int(n) < 0:
        exit()
    n = int(n)
    sastantua(n)
    
except:
    exit()