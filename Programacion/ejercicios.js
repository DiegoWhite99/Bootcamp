//En una fábrica de computadoras se planea ofrecer a los clientes un descuento que dependerá del número de computadoras que compre. Si las computadoras son menos de cinco se les dará un 10% de descuento sobre el total de la compra; si el número de computadoras es mayor o igual a cinco, pero menos de diez se le otorga un 20% de descuento; y si son 10 o más se les da un 40% de descuento. El precio de cada computadora es de $11,000./

/*const precioComputadora = 11.000;

let cantidad = parseInt(prompt('Ingrese el numero de unidades que va a adquirir :'));

let precioTotal = cantidad * precioComputadora;

let descuento = 0;
if (cantidad < 5 ) {
    descuento = 0.10;
} else if ( cantidad >= 5 && cantidad < 10) {
    descuento = 0.20;
} else {
    descuento = 0.40;
}

let descuentoAplicado = precioTotal * descuento;
let precioFinal = precioTotal - descuentoAplicado;

alert (`Precio total sin descuento es : ${precioTotal}`)
alert (`El descuento aplicado es :${descuentoAplicado}`)
alert (`El precio con descuentos aplicados es : ${precioFinal}`) */

// En una llantera se ha establecido una promoción de las llantas marca Ponchadas, dicha promoción consiste en lo siguiente: Si se compran menos de cinco llantas el precio es de $300 cada una, de $250 si se compran de cinco a 10 y de $200 si se compran más de 10. Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las llantas que compra y la que tiene que pagar por el total de la compra.//

/*let count_Llantas = parseInt(prompt('Ingrese la cantidad de llantas a facturar :'));
let precio = 0;
let precio_Total;
if (count_Llantas < 5) {
    precio = 300 ; 
    precio_Total = precio * count_Llantas;
} else if (count_Llantas > 5 && count_Llantas <= 10) {
    precio = 2500 ;
    precio_Total = precio * count_Llantas;
} else {
    precio = 200;
    precio_Total = precio * count_Llantas;
}

alert (`La cantidad de llantas adquiridas es de : ${count_Llantas}`);
alert (`El precio por cada unidad es de : ${precio}`);
alert (`Valor a pagar en esta factura es: ${precio_Total}`);*/


//En un juego de preguntas a las que se responde Si o No gana quien responda correctamente las tres preguntas. Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:  ¿Colon descubrió América?  ¿La independencia de México fue en el año 1810?  ¿The Doors fue un grupo de rock Americano?//

alert('Bienvenido al juego de preguntas');
alert('Tendreas que responder tres preguntas correctamente 😁');
alert('Debes Responder con SI o No');
alert('Que empieze el juego !!! 🤗');
let pregunta1 = prompt('¿Colon descubrió América?');
let pregunta2 = prompt('¿La independencia de México fue en el año 1810?');
let pregunta3 = prompt('¿The Doors fue un grupo de rock Americano?')

if (pregunta1 == 'si' ) {
    alert (`Repuesta a la pregunta ${pregunta1} es correcta`)
} else if (pregunta2 == 'no') {
    alert (`Repuesta a la pregunta ${pregunta2} es correcta`)
} else if (pregunta3 == 'si') {
    alert (`Repuesta a la pregunta ${pregunta3} es correcta`)
} else {
     alert (`Repuesta a la pregunta ${pregunta1} es correcta`)
} 




// // Ejercicios de Condicionales y Lógica de Programación

// 1. Verificación de edad
// Pide al usuario su edad y muestra si es mayor o menor de edad.

// 2. Número par o impar
// Solicita un número y verifica si es par o impar.

// 3. Acceso con contraseña
// Pide al usuario una contraseña y verifica si es correcta o incorrecta.

// 4. Adivinanza
// Pregunta: "¿Cuál es el animal que hace miau?" y verifica la respuesta.

// 5. Descuento en tienda
// Si la compra es mayor a $100, aplica un 10% de descuento; si no, muestra el total normal.

// 6. Votación
// Pide la edad del usuario y determina si puede votar.

// 7. Cálculo de IMC
// Pide el peso y la altura, calcula el IMC y clasifica en bajo peso, normal, sobrepeso u obesidad.

// 8. Tarifa de transporte
// Pregunta si el usuario es estudiante o adulto mayor para aplicar descuento en el pasaje.

// 9. Promedio de notas
// Pide tres notas, calcula el promedio y determina si aprobó o reprobó.

// 10. Año bisiesto
// Pide un año y determina si es bisiesto (divisible por 4 y no por 100, o divisible por 400).
