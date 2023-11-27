def min_multiplications(matrices_dimensiones):
    n = len(matrices_dimensiones)

    # m[i][j] es el número mínimo de multiplicaciones escalares necesarias para
    # calcular el producto de las matrices i a j.
    # m[i][i] es 0 porque solo hay una matriz.
    m = [[0 for _ in range(n)] for _ in range(n)]

    # L es la longitud de la cadena de matrices
    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i+L-1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + matrices_dimensiones[i][0]*matrices_dimensiones[k][1]*matrices_dimensiones[j][1]
                if q < m[i][j]:
                    m[i][j] = q

    return m[0][n-1]

#matrices_dimensiones = [(2, 3), (3, 5), (5, 2)]
matrices_dimensiones = [(5, 2), (2, 3), (3, 5)]
#np-dificil para el orden que sea
print(min_multiplications(matrices_dimensiones))
