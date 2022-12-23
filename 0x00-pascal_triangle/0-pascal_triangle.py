#!/usr/bin/python3
def pascal_triangle(n):
    # return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # initialize the result with a single 1 at the top
    result = [[1]]
    
    # loop through the rows, starting from the second row
    for i in range(1, n):
        # add a new row to the result
        result.append([])
        # loop through the columns of the current row
        for j in range(i + 1):
            # add the value at the current position to the result
            # the value is the sum of the values above and to the left and above and to the right
            if j == 0 or j == i:
                # add 1 for the edges of the row
                result[i].append(1)
            else:
                # add the sum of the values above and to the left and above and to the right
                result[i].append(result[i-1][j-1] + result[i-1][j])
    
    # return the result
    return result

