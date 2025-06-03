from sys import stdin
#functions
def flip(matrix:list):
    matrix.reverse()
    return matrix

def rotate(matrix:list):
    new = []
    for col in range(len(matrix[0])):
        temp = []
        for row in range(len(matrix)):
            temp.append(matrix[row][col])
        new.append(temp)
    new = flip(new)
    return new

#inputs
for L in stdin:
    R, C, M = map(int,L.split())
    B = [list(map(int,input().split())) for _ in range(R)]
    m = list(map(int,input().split()))

    # process
    m.reverse()
    for i in m:
        if i:
            B = flip(B)
        else:
            B = rotate(B)

    #output
    print(len(B), len(B[0]))
    [print(*row) for row in B]