import random
from pyfiglet import Figlet

def obtener_fuente(figlet):
    fuentes = figlet.getFonts()
    return random.choice(fuentes)

def main():
    figlet = Figlet()
    
    fuente_usuario = input("Ingrese el nombre de una fuente (o presione Enter para una fuente aleatoria): ").strip()
    if not fuente_usuario:
        fuente_usuario = obtener_fuente(figlet)
    
    figlet.setFont(font=fuente_usuario)
    texto = input("Ingrese el texto a convertir en arte ASCII: ")
    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()
