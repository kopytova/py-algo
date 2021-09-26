def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end="\t")
        print()


matrix = []
for i in range(4):
    row = []
    for j in range(4):
        num = int(input(f"{[i, j]}: "))
        row.append(num)
    row.append(sum(row))
    matrix.append(row)

print_matrix(matrix)