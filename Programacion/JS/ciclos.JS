/*let num = 2

while(num <=20){
    alert(num)
    num += 2
} */

    function calcularPromedio() {
        let suma = 0;
        let contador = 0;
        let numero;
    
        while (true) {
            numero = parseFloat(prompt("Ingresa un número positivo (o un número negativo para terminar):"));
    
            if (numero < 0) {
                break; // Sale del ciclo si se ingresa un número negativo
            }
    
            suma += numero;
            contador++;
        }
    
        if (contador === 0) {
            console.log("No se ingresaron números válidos.");
        } else {
            const promedio = suma / contador;
            console.log(`El promedio de los números ingresados es: ${promedio.toFixed(2)}`);
        }
    }
    
    calcularPromedio();