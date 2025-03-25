/*export function suma(){
    let n1=parseInt(prompt('Digite un numero'));
    let n2=parseInt(prompt('Digite un segundo numero'));
    let resultado = n1 + n2
    alert('El resultado de la sumas es: ' + resultado);

}

export function sumaDos(numero1, numero2){
    let resultado = numero1 + numero2;
    alert (`el resulta es ${resultado}`)
}*/

/*export function calificacion (){
    let nombre_estudiante = prompt('Ingrese el nombre del estudiante: ');
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
        📌 Calificación Final: ${nota_final.toFixed(2)} 🎯`);

} */

//Estacionamiento


export function estacionamiento (){
    let nombreVehiculo = prompt('Ingrese la placa del vehiculo: ')
    let horasRegistro = parseInt(prompt('Ingrese el numero de horas que el vehiculo ah estado estacionado: '))
    let cargo = horasRegistro * 1500;
    alert(`El vehiculo con la placa ${nombreVehiculo} \n
       Tiempo de parking: ${horasRegistro} \n
       Total a pagar: ${cargo} `);
    countMin(horasRegistro);
};
function countMin(horasRegistro) {
    let horasMin = horasRegistro * 60;
    alert(`El tiempo en minutos es:  ${horasMin}`);
};