/* Debe, calcular el costo de producción de un artículo, teniendo como datos la descripción
y el número de unidades producidas. El costo se calcula multiplicando el nuero de
unidades producidas por un factor de costo de materiales de 3.5 y sumándole al
producto un costo fijo de 10.700 pesos. */

/*let unidades = parseInt(prompt('Ingrese el numero de unidades'));
let materiales = 3.5;
let costo = materiales * unidades + 10700;
 
alert(`su valor es: ${costo}`); */
    
/*Calcular el costo de un terreno cuadrado o rectangular, teniendo como datos la anchura
y el largo en metros y el costo del metro cuadrado.*/

/*let anchura = parseInt(prompt('Ingrese la anchura del terreno a cotizar:'));
let alto = parseInt(prompt('Ingrese la altura del terreno a cotizar: '));
 let metro_cuadrado = anchura * alto

let precio_m2 = parseInt(prompt('Ingrese el valor por m2 del area a cotizar:'));
let precio_total = metro_cuadrado * precio_m2
alert(`El valor del metro cuadrado es de: ${precio_total}`);*/
     
/*Teniendo en cuenta el número de horas calcule su equivalente en minutos, segundos y
días.*/

/*let n_horas = parseInt(prompt('Ingrese el numero de horas:'));

let minutos = n_horas * 60;
let segundos = n_horas * 3600;
let dias = n_horas/ 24;

alert(`la horas a calcular son : ${n_horas}`);
alert(`la horas en minutos son : ${minutos}`);
alert(`la horas en segundos son : ${segundos}`);
alert(`las horas equivalen a Dias son: ${dias}`);*/

/* Calcular el promedio de calificación de un estudiante. Los datos disponibles para lectura
son calificación 1, calificacion2, calificacion3, calificacion4 de cada uno de los cuatro
exámenes presentados. La información que se debe imprimir es el promedio de las
calificaciones.*/

/*let nota1 = parseFloat(prompt("ingrese la primera nota del examen 1 del estudiante: "));
let nota2 = parseFloat(prompt("ingrese la primera nota del examen 2 del estudiante: "));
let nota3 = parseFloat(prompt("ingrese la primera nota del examen 3 del estudiante: "));
let nota4 = parseFloat(prompt("ingrese la primera nota del examen 4 del estudiante: "));

let promedio = (nota1 + nota2 + nota3 + nota4) / 4;

alert (`el promedio del estudiantes es: ${promedio}`); */


/*Calcular el precio de venta de un articulo.se tienen los datos de descripción del artículo
el costo de producción. El precio de venta se calcula añadiendo al costo el 120% como
utilidad y el 15%de impuesto.*/

/*let articulo = prompt('Ingrese el nombre del articulo')
let precio = parseFloat(prompt('Ingrese  el precio del articulo:'));
let costo_produccion = precio;
let utilidad = costo_produccion * 1.2;
let precio_neto = costo_produccion + utilidad;
let impuesto = precio_neto * 0.15;
let precio_total = precio_neto + impuesto;
alert(
    `Detalle del cálculo para ${articulo}:\n\n` +
    `- Precio neto (costo + utilidad): $${precio_neto.toFixed(2)}\n` +
    `- Utilidad (120%): $${utilidad.toFixed(2)}\n` +
    `- Impuesto (15%): $${impuesto.toFixed(2)}\n` +
    `- Precio total: $${precio_total.toFixed(2)}`
  );*/



/*Calcule la hipotenusa de un triángulo rectángulo, los datos se ingresan desde teclado.*/

/*let a = parseInt(prompt('Ingresa el lado a de la hipotenusa'));
let b = parseInt(prompt('Ingresa el lado B de la hipotenusa'));
let cateto_a = Math.pow(a,2);
let cateto_b = Math.pow(b,2);
let suma_catetos = cateto_a + cateto_b;
let c = Math.sqrt(suma_catetos);
alert(`la hipotenusa del trigulo rectangulo es: ${c}`) */


/*Convierte grados centígrados a Fahrenheit y Fahrenheit a centígrados.*/

/*let celsius = parseInt(prompt('Ingrese el los grados celsius a convertir a fahrenheit'));
let valor_fahrenheit = 1.8;
let conversion = (valor_fahrenheit * celsius) + 32;
let fahrenheit = parseInt(prompt('Ingrese el valor fahrenheit a convertir a grados'));
let conversion2 = (fahrenheit - 32 ) / valor_fahrenheit; */

/*Calcular la calificación final de un estudiante. Los datos disponibles para lectura son
calificación 1, equivale al 30% de la nota final, calificacion2, equivale al 20% de la nota
final, calificacion3, equivale al 10% de la nota final, calificacion4, equivale al 40% de la
nota final de cada uno de los cuatro exámenes presentados. La información que se debe
imprimir es el promedio de las calificaciones.*/

/*let nombre_estudiante = prompt('Ingrese el nombre del estudiante: ');
    let curso = prompt('Ingrese la materia a subir la nota: ')
    let n1 = parseFloat(prompt('Ingrese la nota del primer corte: '));
    let corte1 = n1 * 0.3;
    let n2 = parseFloat(prompt('Ingrese la nota del segundo corte: '));
    let corte2 = n2 * 0.2;
    let n3 = parseFloat(prompt('Ingrese la nota del tercer corte: '));
    let corte3 = n3 * 0.1;
    let n4 = parseFloat(prompt('Ingrese la nota del examen Final: '));
    let final_examen = n4 * 0.4;

    let nota_final = corte1 + corte2+ corte3+ final_examen;
    
    alert(`📢 Resultado Final 📢

        📌 Estudiante: ${nombre_estudiante}  
        📌 Materia: ${curso}  
        📌 Calificación Final: ${nota_final.toFixed(2)} 🎯`); */

        /*La velocidad de la luz es de 300000 kilómetros por segundo. Calcular la distancia que
        recorre en dicho tiempo.*/

        let tiempo = 1;
        let velocidad = 300000;
        let formula = velocidad * tiempo;
        alert(`La velocidad de la luz es: ${formula}`);

