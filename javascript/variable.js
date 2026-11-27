let height = 180;
let anotherHeight = height;
let weight;
console.log(height);
console.log(anotherHeight);

weight = 70;
console.log(weight);

// Declarations and strict mode
"use strict";
height = 180;
console.log(height);

// Changing Variable values

let steps = 100;
console.log(steps);
steps = 120;
console.log(steps);
steps = steps + 200;
console.log(steps);

// The Var keyword
var  globalGreeting  =  "Good";
   
function  testFunction()  {
         var  localGreeting  =  "Morning";    
         console.log("function:");
         console.log(globalGreeting);
         console.log(localGreeting);
}
   
testFunction();
   
console.log("main  program:");
console.log(globalGreeting);
console.log(localGreeting);  
