from itertools import permutations

def min_multiplications(matrices_dimensiones, memo):
    n = len(matrices_dimensiones)

    if n in memo:
        return memo[n]

    if n == 1:
        return 0

    min_cost = float('inf')

    for k in range(1, n):
        q = min_multiplications(matrices_dimensiones[:k], memo) + min_multiplications(matrices_dimensiones[k:], memo) + matrices_dimensiones[0][0] * matrices_dimensiones[k-1][1] * matrices_dimensiones[-1][1]
        min_cost = min(min_cost, q)

    memo[n] = min_cost
    return min_cost


def is_valid_permutation(perm):
    return all(perm[i][1] == perm[(i + 1) % len(perm)][0] for i in range(len(perm)))


def min_mat_mult_norder(matrices_dimensiones):
    perms = permutations(matrices_dimensiones)
    valids = []
    outputs = []

    for perm in perms:
        if is_valid_permutation(perm):
            valids.append(list(perm))

    if not valids:
        print("Permutaciones no validas")
        return

    for valid_permutation in valids:
        print(valid_permutation)
        outputs.append(min_multiplications(valid_permutation, {}))

    min_cost = min(outputs)
    print("Minimum cost:", min_cost)


# Matrices que no se pueden multiplicar
#matrices_dimensiones_imposible = [(2, 3), (3, 5), (5, 2), (2, 4), (4, 3)]
#print(matrices_dimensiones_imposible)
#min_mat_mult_norder(matrices_dimensiones_imposible)

# Matrices que se pueden multiplicar
matrices_dimensiones_posible = [(2, 3), (3, 5), (5, 2), (2, 4), (4, 6), (6, 2)]
print(matrices_dimensiones_posible)
min_mat_mult_norder(matrices_dimensiones_posible)

matrices_dimensiones_posible = [(2, 3), (3, 5), (5, 2)]
print(matrices_dimensiones_posible)
min_mat_mult_norder(matrices_dimensiones_posible)


#O(n!) :c
