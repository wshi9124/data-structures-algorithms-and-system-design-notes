/* 
undefined and null not the same - 
undefined is data declared but not assigned value
null is an assignment value (variable as representation of no value)

**Use let and const and never var anymore
Using let for declaring a variable, unlike var, will throw an error if you try to declare the same variable a second time
let lets you reassign its value
const will not let you reassign its value

* use strict instead of loose equality operators
strict equality operator (===)
strict inequality operator (!==)

`` is used for string interpolation
&& and
|| or

Lexical Scope- can access variables in outer scope cant access variables in nested scope
global / functional / block 

*/

function whatColor(color) {
    if (color === "red") {
        console.log("Color is red");
    } else if (typeof color === "string"){
        console.log(`Color is ${color}`);
    } else {
        console.log("Not a color");
    };
};
 
whatColor("red")
whatColor("yellow")
whatColor(2)

const whatColor2 = (color) => console.log(color === "red" ? "Color is red" : "Color is not red");

whatColor2("red")
whatColor2("blue")

/* 
Arrays 
.push()/ .pop() - add/remove end of array 
.unshift()/ .shift() - add/remove beginning of array
... spread operator 
.slice()/ .splice() - non destructive/ destructuve way of getting new array containing removed elements 
 */

const allstates = ["NY", "NJ"]
const newStates = ["FL", ...allstates]
console.log(newStates)

/*
Objects
*/

person = {
    name: "Willie",
    Address: "NYC"
};

console.log(person.name)
console.log(Object.keys(person))
console.log(Object.values(person))
