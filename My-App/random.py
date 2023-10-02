# random_number_generator.py
import random

def generar_numero_aleatorio(minimo, maximo):
    return random.randint(minimo, maximo)

if __name__ == "__main__":
    numero_aleatorio = generar_numero_aleatorio(1, 100)
    print(f"Número aleatorio generado: {numero_aleatorio}")
