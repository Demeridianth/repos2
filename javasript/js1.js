//type of data


// integer INT - number
let x = 123;
// x = "kuku";
// String STR - Text
let str = "Hello World";
let str2 = "somth;"

// Float
let x2 = 2.45;
//Boolean
let bool = true; //false

//Arrays
let arr = ["BMW", 2.5, true];

// Objects
obj1 = {
    name: "Name",
    age: 37,
}

let
    a = 1,
    b = 3,
    c = 4;
let arr2;

// document.write(x,str,bool); //data to document
document.write(arr,obj1) //data to document
// document.write(arr1[1]);
// document.write(obj1.age);
// document.write(arr2);
// console.log(arr,obj1) //data to console

//ES6 let
// const author = "V.K.";




let answer = x * x2;
answer = x + x2;
answer = x - x2;
answer = x / x2;

document.write(answer);


document.write(
    // "<h1 class=\"title1\
    // ">" + str + "</h1>",

    "<h1>" + str2 + "</h1>"); //COncatenacija


document.write(
    `<h1 class="title">${str}</h1>
    <h1 class="title2">${str2}</h1>
    `
)


// input from user

// let ans =  prompt("How old are you???");

// alert("You are " + ans + " years old!");
// let conf = confirm("you are 18 years old?");
// console.log(conf);

let digit = prompt("enter number");
let digit2 = prompt("enter number");

document.write(digit*digit2);