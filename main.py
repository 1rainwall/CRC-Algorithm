trama_binaria = input("Ingrese la trama D(x): ")
polinomio_generador_binario = input("Ingrese el polinomio generador G(x): ")

# Convertir la trama y el polinomio generador a listas de enteros
trama = [int(digito) for digito in trama_binaria]
polinomio_generador = [int(digito) for digito in polinomio_generador_binario]

# Agregar ceros al final de la trama para que tenga la misma longitud que el polinomio generador
trama.extend([0] * (len(polinomio_generador) - 1))

# Inicializar el residuo como la trama extendida
residuo = trama.copy()

for i in range(len(trama) - len(polinomio_generador) + 1):
    if residuo[i] == 1:
        for j in range(len(polinomio_generador)):
            residuo[i+j] = residuo[i+j] ^ polinomio_generador[j]
    print("División paso", i+1, ":", ''.join([str(bit) for bit in residuo]))

# El resultado del algoritmo CRC son los últimos bits del residuo
resultado_crc = residuo[-len(polinomio_generador)+1:]

print("Procedimiento de la división:")
print("Trama en binario:", trama_binaria)
print("Polinomio generador en binario:", polinomio_generador_binario)
print("Residuo:", ''.join([str(bit) for bit in residuo]))
print("Resultado del algoritmo CRC:", ''.join([str(bit) for bit in resultado_crc]))

if 1 in resultado_crc:
    print("Se detectaron errores en la trama.")
else:
    print("No se detectaron errores en la trama.")