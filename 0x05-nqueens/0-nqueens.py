#!/usr/bin/python3
'''N-Queens Challenge'''

import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    queens_cord = []  # coordinates format [row, column]
    stop = False
    row = 0
    column = 0

    # iterate through rows
    while row < n:
        goback = False
        # iterate through columns
        while column < n:
            # check is current column is safe
            safe = True
            for cordinate in queens_cord:
                col = cordinate[1]
                if(col == column or col + (row-cordinate[0]) == column or
                        col - (row-cordinate[0]) == column):
                    safe = False
                    break

            if not safe:
                if column == n - 1:
                    goback = True
                    break
                column += 1
                continue

            # place queen
            cordinates = [row, column]
            queens_cord.append(cordinates)
            # if last row, append solution and reset all to last unfinished row
            # and last safe column in that row
            if row == n - 1:
                solutions.append(queens_cord[:])
                for cordinate in queens_cord:
                    if cordinate[1] < n - 1:
                        row = cordinate[0]
                        column = cordinate[1]
                for i in range(n - row):
                    queens_cord.pop()
                if row == n - 1 and column == n - 1:
                    queens_cord = []
                    stop = True
                row -= 1
                column += 1
            else:
                column = 0
            break
        if stop:
            break
        # on fail: go back to previous row
        # and continue from last safe column + 1
        if goback:
            row -= 1
            while row >= 0:
                column = queens_cord[row][1] + 1
                del queens_cord[row]  # delete previous queen coordinates
                if column < n:
                    break
                row -= 1
            if row < 0:
                break
            continue
        row += 1

    for index, val in enumerate(solutions):
        if index == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)