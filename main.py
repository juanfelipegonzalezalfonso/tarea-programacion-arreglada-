import menu
import entrada
import operaciones as ops


while True:
        opcion = menu.mostrar_menu()

        if opcion == 5:
            print("Saliendo del programa...")
            break

        print("--- Matriz A ---")
        A = entrada.ingresar_matriz()
        print("--- Matriz B ---")
        B = entrada.ingresar_matriz()

        resultado = None
        if opcion == 1:
            resultado = ops.sumar_matrices(A, B)
        elif opcion == 2:
            resultado = ops.multiplicar_matrices(A, B)
        elif opcion == 3:
            resultado = ops.hadamard_matrices(A, B)
        elif opcion == 4:
            resultado = ops.kronecker(A, B)

        if isinstance(resultado, str):
            print(resultado)
        else:
            print("--- Resultado ---")
            entrada.mostrar_matriz(resultado)
