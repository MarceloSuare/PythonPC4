import requests
import datetime

def obtener_precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        precio_usd = data['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException as e:
        print("Error al consultar el precio del Bitcoin:", e)
        return None

def guardar_precio_en_archivo(precio_usd):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("precio_bitcoin.txt", "a") as file:
        file.write(f"{fecha} - Precio Bitcoin: ${precio_usd:,.4f}\n")
    print("Precio guardado en precio_bitcoin.txt")

def main():
    precio_usd = obtener_precio_bitcoin()
    if precio_usd is not None:
        guardar_precio_en_archivo(precio_usd)

if __name__ == "__main__":
    main()
