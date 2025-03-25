let age = parseInt(prompt("Ingrese su edad: "));
let sex;
let pron;

while (true) {
    sex = prompt("Ingrese genero: h/m");
    if (sex == "h"  || sex == "H") {
        pron = "o";
        break;
    } else if (sex == "m" || sex == "M") {
        pron = "a";
        break;
    } else {
        alert("Ingrese una letra valida.");
    }
}

if (age > 0) {
    if (age <= 5) {
        alert(`Niñ${pron} Pequeñ${pron}.`);
    } else if (age >= 6 && age <= 12) {
        alert(`Niñ${pron} Grande.`);
    } else if (age >= 13 && age <= 17) {
        alert(`Adult${pron} Joven.`);
    } else if (age >= 18 && age <= 65) {
        alert(`Adult${pron}.`);
    } else {
        alert(`Adult${pron} Mayor.`);
    }
} else {
    alert("Ingrese una edad valida.");
}

