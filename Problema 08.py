import requests
import sqlite3
import datetime

def obtener_precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        precio_usd = data['bpi']['USD']['rate_float']
        precio_gbp = data['bpi']['GBP']['rate_float']
        precio_eur = data['bpi']['EUR']['rate_float']
        return precio_usd, precio_gbp, precio_eur
    except requests.RequestException as e:
        print("Error al consultar el precio del Bitcoin:", e)
        return None, None, None

def obtener_tipo_cambio_pen():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        precio_venta = data['venta']
        return precio_venta
    except requests.RequestException as e:
        print("Error al consultar el tipo de cambio PEN:", e)
        return None

def crear_tabla():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bitcoin (
            fecha TEXT,
            precio_usd REAL,
            precio_gbp REAL,
            precio_eur REAL,
            precio_pen REAL
        )
    ''')
    conn.commit()
    conn.close()

def guardar_precio_bitcoin(precio_usd, precio_gbp, precio_eur, precio_pen):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
        VALUES (?, ?, ?, ?, ?)
    ''', (fecha, precio_usd, precio_gbp, precio_eur, precio_pen))
    conn.commit()
    conn.close()
    print("Precio del Bitcoin guardado en la base de datos.")

def calcular_precio_10_bitcoins():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT precio_pen, precio_eur FROM bitcoin ORDER BY fecha DESC LIMIT 1
    ''')
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        precio_pen, precio_eur = resultado
        precio_10_bitcoins_pen = 10 * precio_pen
        precio_10_bitcoins_eur = 10 * precio_eur
        print(f"Precio de 10 Bitcoins en PEN: {precio_10_bitcoins_pen:,.4f}")
        print(f"Precio de 10 Bitcoins en EUR: {precio_10_bitcoins_eur:,.4f}")
    else:
        print("No se encontraron datos en la base de datos.")

def main():
    crear_tabla()
    precio_usd, precio_gbp, precio_eur = obtener_precio_bitcoin()
    precio_venta_pen = obtener_tipo_cambio_pen()
    
    if precio_usd is not None and precio_venta_pen is not None:
        precio_pen = precio_usd * precio_venta_pen
        guardar_precio_bitcoin(precio_usd, precio_gbp, precio_eur, precio_pen)
    
    calcular_precio_10_bitcoins()

if __name__ == "__main__":
    main()
