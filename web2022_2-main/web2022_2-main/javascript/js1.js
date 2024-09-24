// Типы данных


// Integer INT - Number
let x = 123;
//x = "kuku";
// String STR - Text
let str = "Hello World";
let str2 = "Hello everyone!";
// Float
let x2 = 2.45;
//Boolean
let bool = true; //false

//Arrays
let arr = ["BMW",2.5,true];

// Objects
let mobj1 = {
    name: "Vitaly",
    age:37
}
let 
a = 1,
b = 3,
c = 4;
let arr2;

// document.write(x,str,bool); //вывод данных в документ
// document.write(arr,obj1); //вывод данных в документ
// document.write(arr[1]);
// document.write(mobj1.age);

// document.write(arr3);

// console.log(arr,obj1); //вывод данных в консоль

//ES6 let
// const author = "V.K.";


let answer = x * x2;
 answer = x + x2;
 answer = x - x2;
 answer = x / x2;
document.write(answer);

// document.write(
//         "<h1 class=\"title1\">" + str + "</h1>",
//         "<h1 class=\"title2\">" + str2 + "</h1>" //Конкатенация \'
//         );

//ES6
document.write(
    `
    <h1 class="title">${str}</h1>
    <h1 class="title2">${str2}</h1>
    `
)


// input from user

// let ans = prompt("How old are you???");

// alert("You are " + ans + " years old!");
// let conf = confirm("Are you 18 years old?");
// console.log(conf);

let digit = +prompt("введите число");
let digit2 = +prompt("введите второе число");

document.write(digit * digit2);

//сделать калькулятор отделочных работ (квадратура, высота потолка)
// сделать кредитный калькулятор (Сумма займа, срок займа, ежемесячный платеж и переплата)
// Зарплата после уплаты налогов
//Отформаировать вывод (результат)