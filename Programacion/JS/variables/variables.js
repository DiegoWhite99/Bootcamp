let p1 =prompt("Ingrese el nombre del producto");
let precio1 = prompt("Ingrese el precio del producto");
let p2 =prompt("Ingrese el nombre del producto");
let precio2 = prompt("Ingrese el precio del producto");
let p3 =prompt("Ingrese el nombre del producto");
let precio3 = prompt("Ingrese el precio del producto");

let total = parseInt(precio1) + parseInt(precio2) + parseInt(precio3);

alert(`Lista de Productos\n${p1} cuesta ${precio1}\n${p2} cuesta ${precio2}\n${p3} cuesta ${precio3} \nSuman en total ${total}`)


