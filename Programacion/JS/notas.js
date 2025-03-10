// let n1 = prompt('Ingrese la nota del primer corte');
// let n2 = prompt('Ingrese la nota del segundo corte');
// let n3 = prompt('Ingrese la nota del tercer corte');
// let n4 = prompt('Ingrese evaluación final');

// let calificacion = (parseFloat(n1) + parseFloat(n2) + parseFloat(n3) + parseFloat(n4)) / 4;

// alert(`La calificación del primer corte es ${n1}
// La calificación del segundo corte es ${n2}
// La calificación del tercer corte es ${n3}
// Su examen final es ${n4}
// Su nota es final ${calificacion}`);

// if (calificacion => 3.0) {
// alert ('Felicitaciones pasaste');
// } else  {
//     alert('Lo siento, perdiste la materia')
// }

// let name1 = prompt('Ingrese nombre del alumno')
// let materia = prompt('Ingrese nombre de la materia')
// let n1 = parseFloat(prompt('Ingrese la nota de la materia'))

// if (n1 > 8 ){
//     alert(`El alumno ${name1} ha aprobado la materia ${materia} con una nota de ${n1}`)
// } else {
//     alert(`El alumno ${name1} ha reprobado la materia ${materia}con una nota de ${n1}`)
// }


// 4.	Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario. Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena. Diseñe un algoritmo que determine el monto de la compra, el monto del descuento, el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto.//

let producto = prompt('Ingrese el nombre del producto');
let cantidad = parseFloat(prompt('Ingrese la cantidad de productos a comprar'));

if (cantidad > 3) {
    let precio = cantidad * 12;
    let descuento = precio * 0.15;
    let total = precio - descuento;
    let obsequio = cantidad / 12;
    alert(`El monto de la compra es ${precio}
    El monto del descuento es ${descuento}
    El monto a pagar es ${total}
    El número de unidades de obsequio es ${obsequio}`);
} else {
    let precio = cantidad * 12;
    let descuento = precio * 0.10;
    let total = precio - descuento;
    alert(`El monto de la compra es ${precio}
    El monto del descuento es ${descuento}
    El monto a pagar es ${total}`);
}
