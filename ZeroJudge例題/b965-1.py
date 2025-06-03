def filp(matrix:list):
    matrix.reverse()
    return matrix

def rotate(matrix:list):
    new_matrix = []

    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        new_matrix.append(row)

    new_matrix = filp(new_matrix)
    return new_matrix

R, C, M = list(map(int, input().split()))
B = []
for i in range(R):
    row = list(map(int, input().split()))
    B.append(row)
m = list(map(int, input().split()))

m.reverse()
for i in m:
    if i == 0:
        B = rotate(B)
    else:
        B = filp(B)

print('%d %d' % (len(B), len(B[0])))

for row in B:
    print(*row)