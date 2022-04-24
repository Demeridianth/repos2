let digit = prompt("enter number");

let str = "bruto>neto"

document.write(
    `<h3 class="title">${str}</h3>`)

let x = digit * 0.105,
    y = (digit - (digit * 0.105)) * 0.2;

let answer = digit - x - y;


if (digit >= 50 && confirm("do you understand?")) {
    document.write(answer);
} else {
    document.write("ERROR")
}

let number = 16.03;

let date;
switch (number) {
    case 16.03:
        date = "16 of Arpil, Year 2022";
        break;
    case 17.03:
        date = "17 of Arpil, Year 2022";
        break;
    case 18.03:
        date = "18 of Arpil, Year 2022";
        break;
    case 19.03:
        date = "19 of Arpil, Year 2022";
        break;


}

let str1 = date


document.write(`<h4 class="title">${str1}</h4>`);






// document.write(digit-(digit*0.105)-(digit-(digit*0.105))*0.2);