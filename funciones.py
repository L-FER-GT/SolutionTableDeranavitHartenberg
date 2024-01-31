from sympy import symbols, cos, sin, Matrix, simplify, pi
from prettytable import PrettyTable

def mostrar_Tabla_DH(dh_params,field_names):
    print('\nTABLA D-H')
    tabla = PrettyTable()
    tabla.field_names = field_names
    for fila in dh_params:
        auxValue=[str(elemento) for elemento in fila]
        tabla.add_row(auxValue)
    print(tabla)

def grados_a_radianes(grados):
    radianes = (grados * pi) / 180
    return radianes

def imprimir_matriz(nombre, matriz):
    tabla = PrettyTable()
    print('\n',nombre)
    tabla.field_names = ['x','y','z','P_f']
    for fila in matriz.tolist():
        auxValue=[str(elemento) for elemento in fila]
        tabla.add_row(auxValue)
    print(tabla)

def multiplicar_matriz(matriz_1,matriz_2):
    return simplify(matriz_1*matriz_2)

def inversa_matriz(matriz):
    return simplify(matriz.inv())

def print_Ecuaciones(x_eq, y_eq, z_eq):
    # Imprimir las ecuaciones
    print('\n-----------')
    print("Ecuación X(q1, q2, q3):\t", x_eq)
    print('')
    print("Ecuación Y(q1, q2, q3):\t", y_eq)
    print('')
    print("Ecuación Z(q1, q2, q3):\t", z_eq)
    print('-----------\n')

def print_Solucions_XYZ(x_eq, y_eq, z_eq,values):
    sol_X=x_eq.subs(values).evalf()
    sol_Y=y_eq.subs(values).evalf()
    sol_Z=z_eq.subs(values).evalf()
    print('-----------')
    print("Solucion en X: ", sol_X)
    print("Solucion en Y: ", sol_Y)
    print("Solucion en Z: ", sol_Z)
    print('-------------')

def print_Solucions_T(result_matrix,values):
    sol_M=result_matrix.subs(values).evalf()
    imprimir_matriz("T(qi)", sol_M)
    return sol_M