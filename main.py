from sympy import symbols, cos, sin, Matrix, simplify, pi, Eq,solve
from funciones import grados_a_radianes, imprimir_matriz, multiplicar_matriz,inversa_matriz,mostrar_Tabla_DH
from funciones import print_Solucions_XYZ,print_Solucions_T,print_Ecuaciones,inversa_matriz
from constructors import build_dh_equations, filaConstructor,inputTable

def menu():
    print("\nMenú:")
    print("1. Crear Tabla D-H")
    print("2. Mostrar tabla D-H")
    print("3. Construir Matrices An")
    print("4. Mostrar Matrices An")
    print("5. Mostrar Ecuaciones (x,y,z)")
    print("6. Calcular y Mostrar Soluciones (x,y,z)")
    print("7. Calcular y Mostrar Matriz T")
    print("8. Mostrar Soluciones T")
    print("9. Agregar Valores Reales")
    print("10. Agregar Valores Hexagesimales")
    print("11. Reiniciar Valores de variables")
    print("12. Aplicar Valores a variables")
    print("13. Asignar Tablas Derecha e izquierda")
    print("14. Pasar a izquierda")
    print("15. Calcular Valores")
    print("16. Resolver Ecuaciones")
    print("17. Mostrar inversas An")
    print("0. Salir")
    opcion=input('Escoja una opcion: ')
    return opcion

def main():
    
    dh_params=[filaConstructor('180+q1' , '20'  , '0'   , '90'),
               filaConstructor('90+q2'  , '6'  , '2'  , '90'),
               filaConstructor('q3'     , '0'   , '3'  , '0')]
    values={}
    result_An=[]
    result_matrix=[]
    x_eq, y_eq, z_eq=(0,0,0)
    TDer=[]
    TIzq=[]
    TSol=[]
    while True:
        eleccion = menu()
        # Procesar la elección del usuario con else if
        if eleccion == '0': # Salir del programa
            print('-----BYE-----')
            break
        elif eleccion == '1': # Definir los parámetros de Denavit-Hartenberg para cada enlace
            num_enlaces=int(input('INGRESE EL NUMERO DE ENLACES: '))
            dh_params=inputTable(num_enlaces)
        elif eleccion == '2':
            mostrar_Tabla_DH(dh_params,['θ','di','ai','α'])
        elif eleccion == '3':
            x_eq, y_eq, z_eq, result_matrix, result_An = build_dh_equations(dh_params)
        elif eleccion == '4':
            for i in range(len(result_An)):
                An=result_An[i]
                imprimir_matriz("A_"+str(i+1), An)
        elif eleccion == '5':
            print_Ecuaciones(x_eq, y_eq, z_eq)
        elif eleccion == '6':
            print_Solucions_XYZ(x_eq, y_eq, z_eq,values)
        elif eleccion == '7':
            imprimir_matriz("T(qi)", result_matrix)
        elif eleccion == '8':
            TSol=print_Solucions_T(result_matrix,values)
        elif eleccion == '9':
            print('ingrese 0 para dejar de agregar variables')
            while True:
                x=input('Ingrese el nombre de la variable: ').lower()
                if x=='0':break
                y=float(input('-->Valor Real : '))
                values[x]=y
        elif eleccion == '10':
            print('ingrese 0 para dejar de agregar variables')
            while True:
                x=input('Ingrese el nombre de la variable: ').lower()
                if x=='0':break
                y=int(input('-->Angulo (grados): '))
                values[x]=grados_a_radianes(y)
        elif eleccion == '11':
            values={}
        elif eleccion == '12':
            dh_params=dh_params.subs(values)
        elif eleccion == '13':
            TIzq.append(TSol)
            for i in range(len(result_An)-1,-1,-1):
                An=result_An[i]
                TDer.append(An)
            print(f"Tabla izquierda {len(TIzq)} asignadas")
            print(f"Tabla derecha {len(TDer)} asignadas")
        elif eleccion == '14':
            auxAn=TDer.pop()
            TIzq.append(inversa_matriz(auxAn))
            print(f"Tabla izquierda {len(TIzq)} asignadas")
            print(f"Tabla derecha {len(TDer)} asignadas")
        elif eleccion == '15':
            TotalIzq=TIzq[0]
            TotalDer=TDer[0]
            for i in range(1,len(TIzq)):
                TotalIzq=multiplicar_matriz(TIzq[i],TotalIzq)
            for i in range(1,len(TIzq)):
                TotalDer=multiplicar_matriz(TDer[i],TotalDer)
            imprimir_matriz("T_Izquierda", TotalIzq)
            imprimir_matriz("T_Derecha", TotalDer)
        elif eleccion == '16':
            q1,q2,q3 = symbols('q1 q2 q3')
            ecuaciones = [Eq(TotalIzq[i, j], TotalDer[i, j]) for i in range(4) for j in range(4)]
            # Resolver el sistema de ecuaciones
            soluciones = solve(ecuaciones)
            # Imprimir las soluciones
            print("Soluciones:")
            print(soluciones)
            # for variable, valor in soluciones.items():
            #     print(f"{variable}: {valor}")
        elif eleccion == '17':
            for i in range(len(result_An)):
                An=result_An[i]
                inversaAn=inversa_matriz(An)
                imprimir_matriz("Inversa: A_"+str(i+1), inversaAn)
            
        else:
            print("\nOpción no válida. Por favor, selecciona una opción válida.\n")
        input("Presiona Enter para continuar...")


    # values={'q1':grados_a_radianes(210), 
    #         'q2':grados_a_radianes(20),
    #         'q3':grados_a_radianes(-45),
    #         'l1':20,
    #         'l2':6,
    #         'l3':2,
    #         'l4':3
    #         }
    

    # #Mostrar la tabla de Denavit y Hartember

    # # Construir las ecuaciones X(q1, q2, q3) con longitudes de brazos
    

    # #Mostrar las matrices An
    # array_a=[]
    # for i in range(len(result_An)):
    #     An=result_An[i]
    #     array_a.append(An)
    #     imprimir_matriz("A_"+str(i+1), An)

    # asd=multiplicar_matriz(array_a[1],array_a[2])
    # imprimir_matriz("A_2,A_3"+str(i+1), asd)
    # inversa=inversa_matriz(array_a[0])
    # imprimir_matriz("A_1 inversa"+str(i+1), inversa)

    # values={'q1':grados_a_radianes(210), 
    #         'q2':grados_a_radianes(20),
    #         'q3':grados_a_radianes(-45)
    #         }
    # sol_M=result_matrix.subs(values).evalf()

    # izqMatriz=multiplicar_matriz(inversa,sol_M)
    # imprimir_matriz("Izquierda"+str(i+1), izqMatriz)

    # imprimir_matriz("T(qi)", result_matrix)

    # #mostrar Las Ecuaciones
    # print_Ecuaciones(x_eq, y_eq, z_eq)


    # #mostrar las soluciones Si hace falta
    # if(True):
    #     print_Solucions(x_eq, y_eq, z_eq,result_matrix, values)
        


main()
