# Se solicita al usuario que ingrese un número decimal
valor_digitado = int(input("Ingrese un número decimal: "))

# Se convierte el valor digitado a binario
valor_binario = bin(valor_digitado)[2:]

# Se muestra en pantalla el valor digitado en binario
print("Valor digitado en binario:", valor_binario)

# Se define el polinomio generador en formato binario
polinomio_generador = [1, 1, 0, 1]

# Se extiende el valor binario con ceros adicionales al final
valor_extendido = valor_binario + "000"

# Se realiza la división sintética utilizando el polinomio generador
for i in range(len(valor_extendido) - len(polinomio_generador) + 1):
    if valor_extendido[i] == "1":
        # Si el bit en la posición i es 1, se realiza la operación XOR entre los bits del polinomio generador y los bits del valor extendido
        for j in range(len(polinomio_generador)):
            valor_extendido = valor_extendido[:i+j] + str(int(
                polinomio_generador[j] != int(valor_extendido[i+j]))) + valor_extendido[i+j+1:]

# Se obtiene el resultado del algoritmo CRC
resultado_crc = valor_extendido[-len(polinomio_generador)+1:]

# Se muestra en pantalla el valor digitado en binario y el resultado del algoritmo CRC
print("Valor digitado en binario:", valor_binario)
print("Resultado del algoritmo CRC:", resultado_crc)
