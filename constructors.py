from sympy import symbols, cos, sin, Matrix, simplify, pi
from funciones import grados_a_radianes

def dh_transform(theta, d, a, alpha):

    ct = cos(theta)
    st = sin(theta)
    ca = cos(alpha)
    sa = sin(alpha)

    # Matriz de transformación homogénea DH
    a_matrix = Matrix([
        [ct, -st*ca, st*sa, a*ct],
        [st, ct*ca, -ct*sa, a*st],
        [0, sa, ca, d],
        [0, 0, 0, 1]
    ])

    return a_matrix

def build_dh_equations(dh_params):

    n = len(dh_params)
    result_matrix = Matrix.eye(4)
    result_An=[]

    for i in range(n):
        alpha, a, d, theta = dh_params[i]

        # Reemplazar valores de ángulos articulares y longitudes de brazos en la matriz DH
        auxValue=dh_transform(alpha, a, d, theta)
        result_An.append(auxValue)
        result_matrix *= auxValue

    # Extraer las ecuaciones X(q1, q2, ..., qn)
    x_eq = result_matrix[0, 3]
    y_eq = result_matrix[1, 3]
    z_eq = result_matrix[2, 3]

    return simplify(x_eq), simplify(y_eq), simplify(z_eq), result_matrix, result_An


def convertElement(cadena,esAngulo):
    arrValue=[]
    if '+' in cadena:
        arrValue=cadena.split('+')
    else:
        arrValue=cadena.split('-')
    value=0
    for x in range(len(arrValue)):
        if arrValue[x].isdigit():
            if(esAngulo):
                value+=grados_a_radianes(int(arrValue[x]))
            else:
                value+=int(arrValue[x])
        else:
            value+=symbols(arrValue[x].strip())
    return value

def filaConstructor(theta, d, a, alpha):
    cadena=''
    arr=[]
    arr.append(convertElement(theta,True))
    arr.append(convertElement(d,False))
    arr.append(convertElement(a,False))
    arr.append(convertElement(alpha,True))
    return arr

def inputTable(num_enlaces):
    dh_params=[]
    print('INGRESE LA TABLA D-H')
    for i in range(num_enlaces):
        print('\n')
        print('Ingrese la fila', i+1)
        theta = input('intrese theta: ').lower()
        d = input('intrese d: ').lower()
        a = input('intrese a: ').lower()
        alpha = input('intrese alpha: ').lower()
        newArr=filaConstructor(theta, d, a, alpha)
        dh_params.append(newArr)
    return dh_params