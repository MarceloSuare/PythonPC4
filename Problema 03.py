import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)
        print(f"Imagen descargada como {nombre_archivo}")
    except requests.RequestException as e:
        print("Error al descargar la imagen:", e)

def crear_zip(nombre_archivo, nombre_zip):
    try:
        with zipfile.ZipFile(nombre_zip, 'w') as zipf:
            zipf.write(nombre_archivo, os.path.basename(nombre_archivo))
        print(f"Archivo ZIP creado como {nombre_zip}")
    except Exception as e:
        print("Error al crear el archivo ZIP:", e)

def descomprimir_zip(nombre_zip, carpeta_destino):
    try:
        with zipfile.ZipFile(nombre_zip, 'r') as zipf:
            zipf.extractall(carpeta_destino)
        print(f"Archivo ZIP descomprimido en {carpeta_destino}")
    except Exception as e:
        print("Error al descomprimir el archivo ZIP:", e)

def main():
    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    nombre_imagen = "imagen.jpg"
    nombre_zip = "imagen.zip"
    carpeta_destino = "descomprimido"
    
    descargar_imagen(url_imagen, nombre_imagen)
    crear_zip(nombre_imagen, nombre_zip)
    descomprimir_zip(nombre_zip, carpeta_destino)

if __name__ == "__main__":
    main()
