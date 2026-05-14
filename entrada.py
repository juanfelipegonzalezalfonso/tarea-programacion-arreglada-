def ingresar_matriz():
    while True:
        try:
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))
            if filas > 0 and columnas > 0:
                break
            print("Dimensiones deben ser mayores a 0.")
        except ValueError:
            print("Error: Ingrese números enteros.")

    matriz = []
    for i in range(filas):
        while True:
            try:
                fila = list(map(float, input(f"Ingrese la fila {i+1} separada por espacios: ").split()))
                if len(fila) != columnas:
                    print(f"Error: debe ingresar exactamente {columnas} valores.")
                else:
                    matriz.append(fila)
                    break
            except ValueError:
                print("Error: Ingrese solo números.")
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
