def contar_lineas_codigo(ruta_archivo):
    try:
        if not ruta_archivo.endswith(".py"):
            print("El archivo debe tener una extensión .py")
            return
        
        with open(ruta_archivo, "r") as file:
            lineas = file.readlines()
        
        lineas_codigo = 0
        for linea in lineas:
            linea_strip = linea.strip()
            if linea_strip and not linea_strip.startswith("#"):
                lineas_codigo += 1
        
        print(f"Número de líneas de código (excluyendo comentarios y líneas en blanco): {lineas_codigo}")
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Error al contar las líneas de código:", e)

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)

if __name__ == "__main__":
    main()
