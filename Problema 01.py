import requests

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

def calcular_valor_bitcoins(n, precio_usd):
    valor_total = n * precio_usd
    return valor_total

def main():
    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    precio_usd = obtener_precio_bitcoin()
    if precio_usd is not None:
        valor_total = calcular_valor_bitcoins(n, precio_usd)
        print(f"El valor de {n} Bitcoins en USD es: ${valor_total:,.4f}")

if __name__ == "__main__":
    main()
