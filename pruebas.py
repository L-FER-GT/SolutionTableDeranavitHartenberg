
from sympy import symbols, Eq, solve, Matrix

# Definir variables simbólicas
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = symbols('a b c d e f g h i j k l m n o p')

# Definir las matrices A y B
A = Matrix([[a, b, c, d], [e, f, g, h], [i, j, k, l], [m, n, o, p]])
B = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# Definir la ecuación A = B
ecuaciones = [Eq(A[i, j], B[i, j]) for i in range(4) for j in range(4)]

# Resolver el sistema de ecuaciones
soluciones = solve(ecuaciones)

# Imprimir las soluciones
print("Soluciones:")
for variable, valor in soluciones.items():
    print(f"{variable}: {valor}")
