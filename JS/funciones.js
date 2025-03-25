export function estacionamiento() {
    let nombreVehiculo = prompt('Ingrese la placa del vehiculo: ');
    let horasRegistro = parseInt(prompt('Ingrese el numero de horas que el vehiculo ha estado estacionado: '), 10);
    if (isNaN(horasRegistro)) {
        alert('Por favor, ingrese un número válido de horas.');
        return;
    }
    let cargo = horasRegistro * 1500;
    alert(`El vehiculo con la placa ${nombreVehiculo} \n
       Tiempo de parking: ${horasRegistro} \n
       Total a pagar: ${cargo}`);
    countMin(horasRegistro);
}

function countMin(horasRegistro) {
    let horasMin = horasRegistro * 60;
    alert(`El tiempo en minutos es: ${horasMin}`);
}