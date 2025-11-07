def matrix_union(m1, m2):
    return [[(k or l) for k, l in zip(i, j)] for i, j in zip(m1, m2)]

def matrix_xor(m1, m2):
    return [[(k ^ l) for k, l in zip(i, j)] for i, j in zip(m1, m2)]


MR1 = [[1, 1, 1], [1, 0, 1], [0, 1, 0]]
MR2 = [[1, 0, 1], [0, 1, 1], [1, 1, 0]]

Union_matrix = matrix_union(MR1, MR2)
Symmetric_dif = matrix_xor(MR1, MR2)

A = ['p', 'q', 'r']

print("Pairs in the Union matrix:")
print([(A[i], A[j]) for i in range(len(Union_matrix))
      for j in range(len(Union_matrix[i])) if Union_matrix[i][j] == 1])

print("Pairs in the Symmetric difference:")
print([(A[i], A[j]) for i in range(len(Symmetric_dif))
      for j in range(len(Symmetric_dif[i])) if Symmetric_dif[i][j] == 1])
