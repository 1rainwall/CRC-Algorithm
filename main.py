
from tqdm import tqdm
import time  
from termcolor import colored  

# Definimos la función que transforma un polinomio en una lista de coeficientes y su grado


def polinomio_a_coeficientes(polinomio):
    coeficientes = []  # lista para almacenar los coeficientes
    for i in range(len(polinomio)):
        if polinomio[i] == 'x':  # si encontramos una 'x'
            # si es el primer término o el signo anterior es un '+'
            if i == 0 or polinomio[i-1] == '+':
                coeficientes.append(1)  # añadimos un coeficiente de 1
            elif polinomio[i-1] == '-':  # si el signo anterior es un '-'
                coeficientes.append(-1)  # añadimos un coeficiente de -1
            else:  # en cualquier otro caso
                # añadimos el coeficiente correspondiente
                coeficientes.append(int(polinomio[i-1]))
    grado = len(coeficientes) - 1  # calculamos el grado del polinomio
    return coeficientes, grado

# Definimos la función que evalúa un polinomio con los coeficientes dados en un punto dado


def evaluar_polinomio(coeficientes, x):
    resultado = 0  # variable para almacenar el resultado de la evaluación
    for i in range(len(coeficientes)):  # para cada coeficiente
        # multiplicamos el coeficiente por x elevado a su posición y sumamos el resultado
        resultado += coeficientes[i] * (x ** i)
    return resultado

# Definimos la función que convierte un número decimal a binario con un número de bits dado


def decimal_a_binario(decimal, num_bits):
    # convertimos el número decimal a binario, eliminando los dos primeros caracteres ('0b')
    binario = bin(decimal)[2:]
    if len(binario) < num_bits:  # si el número de bits del binario es menor que el número de bits deseado
        # añadimos ceros a la izquierda hasta completar el número de bits
        binario = '0' * (num_bits - len(binario)) + binario
    return binario


# Pedimos al usuario que ingrese un polinomio y un valor de x para evaluarlo
polinomio = input(
    "Ingrese un polinomio de la forma 'ax^n + bx^(n-1) + ... + c': ")
x = int(input("Ingrese el valor de x para evaluar el polinomio: "))

# Convertimos el polinomio a una lista de coeficientes y su grado
coeficientes, grado = polinomio_a_coeficientes(polinomio)

# Evaluamos el polinomio en el valor de x dado
valor_digitado = evaluar_polinomio(coeficientes, x)

# Convertimos el valor obtenido a binario con un número de bits igual al grado del polinomio más 1
valor_binario = decimal_a_binario(valor_digitado, grado + 1)

# Definimos el polinomio generador
polinomio_generador = [1, 1, 0, 1]
# Se extiende el valor_binario con ceros a la derecha para poder calcular el CRC
valor_extendido = valor_binario + "0" * (len(polinomio_generador) - 1)

with tqdm(total=len(valor_binario), desc="Procesando", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}", ncols=50) as pbar:
    for i in range(len(valor_binario)):
        if valor_extendido[i] == "1":  # si el bit es 1 (True)
            # para cada bit del polinomio generador
            for j in range(len(polinomio_generador)):
                valor_extendido = valor_extendido[:i+j] + str(int(
                    polinomio_generador[j] != int(valor_extendido[i+j])))+valor_extendido[i+j+1:]  # realizamos la operación XOR
        pbar.update(1)
        time.sleep(0.1)
# Se obtiene el valor del CRC, que corresponde a los últimos len(polinomio_generador)-1 bits de valor_extendido
valor_CRC = valor_extendido[-(len(polinomio_generador)-1):]
# Mostramos el mensaje CRC
# Se concatena el mensaje original con el CRC obtenido
mensaje_CRC = valor_binario + valor_CRC

mensaje_CRC_C = mensaje_CRC[:len(valor_binario)] + \
    colored(mensaje_CRC[len(valor_binario):], "green")
# Se muestra el mensaje original con el CRC obtenido
print("Mensaje CRC:", mensaje_CRC_C)
