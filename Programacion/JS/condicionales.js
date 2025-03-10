let p1 =prompt("Ingrese producto 1")
let price1 =prompt("Igrese el valor del producto")
let p2 =prompt("Ingrese producto 2")
let price2 =prompt("Igrese el valor del producto")
let p3 =prompt("Ingrese producto 3")
let price3 =prompt("Igrese el valor del producto")
let total = parseFloat(price2) + parseFloat(price2) + parseFloat(price3);
let descuento = 0
let total_pago = 0

alert(`su producto es ${p1} y el valor es de \n${price1}
    su segundo producto es  ${p2} y el valor es \n${price2}
    su tercer producto es ${p3} y el valor es \n${price3}
    su compra es de un total ${total}`);

    if (total >= 100000) {
        descuento = total * 0.10;
    } else {
        descuento = total * 0.05;
    }
    total_pago = total - descuento;
    


alert(`El descuento aplicado es de ${descuento}.
    El total a pagar después del descuento es ${total_pago}.`);