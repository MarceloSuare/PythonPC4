def escribir_tabla_multiplicar(n):
    try:
        with open(f"tabla-{n}.txt", "w") as file:
            for i in range(1, 11):
                file.write(f"{n} x {i} = {n * i}\n")
        print(f"Tabla de multiplicar del {n} guardada en tabla-{n}.txt")
    except Exception as e:
        print("Error al escribir la tabla de multiplicar:", e)

def leer_tabla_multiplicar(n):
    try:
        with open(f"tabla-{n}.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")
    except Exception as e:
        print("Error al leer la tabla de multiplicar:", e)

def leer_linea_tabla_multiplicar(n, m):
    try:
        with open(f"tabla-{n}.txt", "r") as file:
            lineas = file.readlines()
            if 1 <= m <= 10:
                print(lineas[m-1].strip())
            else:
                print("Número de línea fuera de rango.")
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")
    except Exception as e:
        print("Error al leer la línea de la tabla de multiplicar:", e)

def main():
    while True:
        print("Opciones:")
        print("1. Escribir tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Leer línea específica de la tabla de multiplicar")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                n = int(input("Ingrese un número entre 1 y 10: "))
                if 1 <= n <= 10:
                    escribir_tabla_multiplicar(n)
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "2":
            try:
                n = int(input("Ingrese un número entre 1 y 10: "))
                if 1 <= n <= 10:
                    leer_tabla_multiplicar(n)
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "3":
            try:
                n = int(input("Ingrese un número entre 1 y 10: "))
                m = int(input("Ingrese el número de línea entre 1 y 10: "))
                if 1 <= n <= 10 and 1 <= m <= 10:
                    leer_linea_tabla_multiplicar(n, m)
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
