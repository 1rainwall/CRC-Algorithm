from tqdm import tqdm
import time
from termcolor import colored


def polinomio_a_coeficientes(polinomio):
    coeficientes = []
    for i in range(len(polinomio)):
        if polinomio[i] == 'x':
            if i == 0 or polinomio[i-1] == '+':
                coeficientes.append(1)
            elif polinomio[i-1] == '-':
                coeficientes.append(-1)
            else:
                coeficientes.append(int(polinomio[i-1]))
    grado = len(coeficientes) - 1
    return coeficientes, grado


def evaluar_polinomio(coeficientes, x):
    resultado = 0
    for i in range(len(coeficientes)):
        resultado += coeficientes[i] * (x ** i)
    return resultado


def decimal_a_binario(decimal, num_bits):
    binario = bin(decimal)[2:]
    if len(binario) < num_bits:
        binario = '0' * (num_bits - len(binario)) + binario
    return binario


polinomio = input(
    "Ingrese un polinomio de la forma 'ax^n + bx^(n-1) + ... + c': ")
x = int(input("Ingrese el valor de x para evaluar el polinomio: "))
coeficientes, grado = polinomio_a_coeficientes(polinomio)
valor_digitado = evaluar_polinomio(coeficientes, x)
valor_binario = decimal_a_binario(valor_digitado, grado + 1)
polinomio_generador = [1, 1, 0, 1]
valor_extendido = valor_binario + "0" * (len(polinomio_generador) - 1)

with tqdm(total=len(valor_binario), desc="Procesando", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}", ncols=50) as pbar:
    for i in range(len(valor_binario)):
        if valor_extendido[i] == "1":
            for j in range(len(polinomio_generador)):
                valor_extendido = valor_extendido[:i+j] + str(int(
                    polinomio_generador[j] != int(valor_extendido[i+j])))+valor_extendido[i+j+1:]
        pbar.update(1)
        time.sleep(0.1)

valor_CRC = valor_extendido[-(len(polinomio_generador)-1):]
mensaje_CRC = valor_binario + valor_CRC
mensaje_CRC_C = mensaje_CRC[:len(valor_binario)] + \
    colored(mensaje_CRC[len(valor_binario):], "green")
print("Mensaje CRC:", mensaje_CRC_C)