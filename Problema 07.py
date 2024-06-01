import requests
import sqlite3
import datetime

def obtener_precio_dolar():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        precio_compra = data['compra']
        precio_venta = data['venta']
        return precio_compra, precio_venta
    except requests.RequestException as e:
        print("Error al consultar el precio del dólar:", e)
        return None, None

def crear_tabla():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT,
            compra REAL,
            venta REAL
        )
    ''')
    conn.commit()
    conn.close()

def guardar_precio_en_db(precio_compra, precio_venta):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sunat_info (fecha, compra, venta)
        VALUES (?, ?, ?)
    ''', (fecha, precio_compra, precio_venta))
    conn.commit()
    conn.close()
    print("Precio guardado en la base de datos.")

def main():
    crear_tabla()
    precio_compra, precio_venta = obtener_precio_dolar()
    if precio_compra is not None and precio_venta is not None:
        guardar_precio_en_db(precio_compra, precio_venta)

if __name__ == "__main__":
    main()



