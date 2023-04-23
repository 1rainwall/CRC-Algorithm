// Se define el valor digitado en decimal
let valorDigitado = 564054;
// Se convierte el valor digitado a binario
let valorBinario = valorDigitado.toString(2);
// Se muestra en pantalla el valor digitado en binario
console.log("Valor digitado en binario: " + valorBinario);
// Se define el polinomio generador en formato binario
let polinomioGenerador = [1, 1, 0, 1];
// e extiende el valor binario con ceros adicionales al final
let valorExtendido = valorBinario + "000";
// Se realiza la división sintética utilizando el polinomio generador
for (
  let i = 0;
  i < valorExtendido.length - polinomioGenerador.length + 1;
  i++
) {
  if (valorExtendido[i] === "1") {
    // Si el bit en la posición i es 1, se realiza la operación XOR entre los bits del polinomio generador y los bits del valor extendido
    for (let j = 0; j < polinomioGenerador.length; j++) {
      valorExtendido =
        valorExtendido.substr(0, i + j) +
        (polinomioGenerador[j] ^ parseInt(valorExtendido[i + j])) +
        valorExtendido.substr(i + j + 1);
    }
  }
}
// Se obtiene el resultado del algoritmo CRC
let resultadoCRC = valorExtendido.substr(-polinomioGenerador.length + 1);
// Se muestra en pantalla el valor digitado en binario y el resultado del algoritmo CRC
console.log("Valor digitado en binario: " + valorBinario);
console.log("Resultado del algoritmo CRC: " + resultadoCRC);