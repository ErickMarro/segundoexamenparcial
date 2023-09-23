import sys
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_rectangulo(ancho, altura):
    return ancho * altura

def main():
    if len(sys.argv) < 3:
        print("Uso: programa.py <tipo_de_figura> <valores_separados_por_pipe>")
        return

    tipo_figura = sys.argv[1]
    valores = sys.argv[2].split("|")

    if tipo_figura == "circulo" and len(valores) == 1:
        try:
            radio = float(valores[0])
            area = calcular_area_circulo(radio)
            print(f"El área del círculo con radio {radio} es {area:.2f}")
        except ValueError:
            print("Error: El radio debe ser un número válido.")
    elif tipo_figura == "rectangulo" and len(valores) == 2:
        try:
            ancho = float(valores[0])
            altura = float(valores[1])
            area = calcular_area_rectangulo(ancho, altura)
            print(f"El área del rectángulo con ancho {ancho} y altura {altura} es {area:.2f}")
        except ValueError:
            print("Error: El ancho y la altura deben ser números válidos.")
    else:
        print("Error: Tipo de figura no válido o cantidad incorrecta de valores.")

if __name__ == "__main__":
    main()
