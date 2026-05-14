def sumar_matrices(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return "Error: Dimensiones incompatibles para suma."

def multiplicar_matrices(A, B):
    if len(A[0]) == len(B):
        return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]
    return "Error: Columnas de A deben ser iguales a filas de B."

def hadamard_matrices(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        return [[A[i][j] * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return "Error: Dimensiones incompatibles para Hadamard."

def kronecker(A, B):
    fA, cA = len(A), len(A[0])
    fB, cB = len(B), len(B[0])
    return [[A[i // fB][j // cB] * B[i % fB][j % cB] for j in range(cA * cB)] for i in range(fA * fB)]
