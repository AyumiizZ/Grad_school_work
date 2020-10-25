def search(matrix, lower_row, upper_row, lower_col, upper_col, key):
    mid_row = lower_row + (upper_row - lower_row) // 2
    mid_col = lower_col + (upper_col - lower_col) // 2
    if (matrix[mid_row][mid_col] == key):  # If key is present at middle
        print("Found ", key, " at ", mid_row, " ", mid_col)
    else:
        if (mid_row != upper_row or mid_col != lower_col):
            search(matrix, lower_row, mid_row, mid_col, upper_col, key)
        if (lower_row == upper_row and lower_col + 1 == upper_col):
            if (matrix[lower_row][upper_col] == key):
                print("Found ", key, " at ", lower_row, " ", upper_col)
        if (matrix[mid_row][mid_col] < key):
            if (mid_row + 1 <= upper_row):
                search(matrix, mid_row + 1, upper_row,
                       lower_col, upper_col, key)
        else:
            if (mid_col - 1 >= lower_col):
                search(matrix, lower_row, upper_row,
                       lower_col, mid_col - 1, key)


if __name__ == '__main__':
    matrix = [[10, 20, 30, 40],
              [15, 25, 35, 45],
              [27, 29, 37, 48],
              [32, 33, 39, 50]]
    rowcount = 4
    colCount = 4
    key = 50
    for i in range(rowcount):
        for j in range(colCount):
            search(matrix, 0, rowcount - 1, 0, colCount - 1, matrix[i][j])
