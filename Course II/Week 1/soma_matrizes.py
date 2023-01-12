def soma_matrizes(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        new_matrix = []
        for i in range(len(m1)):
            new_matrix.append([])
            for j in range(len(m1[0])):
                sum = m1[i][j] + m2[i][j]
                new_matrix[i].append(sum)
        return new_matrix
    else:
        return False