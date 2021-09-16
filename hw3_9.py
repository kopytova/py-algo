m = [
    [9, 10, 11, 12, 42],
    [1, 2, 3, 4, 10],
    [5, 6, 7, 8, 26],
    [13, 14, 15, 16, 58],
    [0, 4, 5, 2, 3]
]

def find_max_in_mins(matrix):
    height = len(matrix)     # высота матрицы (кол-во строк)
    width = len(matrix[0])   # ширина матрицы (кол-во элементов в строке)
    min_nums_in_columns = []
    for j in range(width):
        min_num = matrix[0][j]
        for i in range(1, height):
            num = matrix[i][j]
            if num < min_num:
                min_num = num
        min_nums_in_columns.append(min_num)
    max_in_mins = max(min_nums_in_columns)
    return max_in_mins

print(find_max_in_mins(m))