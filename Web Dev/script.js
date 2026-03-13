// let nums = [1,2,3,4];
// let square = nums.map (n=> n*n);
// console.log(square)

// let nums = [1,2,3,4];
// let even = nums.filter( n=> n%2===0);
// console.log(even)

// let nums = [1,2,3,4,5];
// let sum = nums.reduce((total,n)=> total+n,0);
// console.log(sum); // 15 Adds up all the elements in the array.

// setTimeout(function(){
// console.log("Hello");
// },2000);

// let btn=document.getElementById("btn");

// btn.addEventListener("click",function(){
// alert("Button clicked");
// });

// // ...existing code...
// // JSON.stringify example: convert object to JSON string and back
// const user = { id: 1, name: "Ana", roles: ["admin", "user"] };
// const jsonString = JSON.stringify(user);
// console.log("Stringified:", jsonString);

// // store string (e.g., localStorage) and restore
// localStorage.setItem("user", jsonString);
// const restored = JSON.parse(localStorage.getItem("user"));
// console.log("Parsed:", restored);
// // ...existing code...

// let x = 5;
// x += 10;
// console.log(x)

// typeof "1234";
// console.log(typeof 1234);

// // ...existing code...
// // TDZ (Temporal Dead Zone) example
// try {
//   console.log(a); // ReferenceError: Cannot access 'a' before initialization
// } catch (e) {
//   console.log("TDZ error:", e.message);
// }
// let a = 10;
// console.log("a after declaration:", a); // 10

// // var does not have TDZ
// console.log("b before declaration (var):", b); // undefined
// var b = 20;
// console.log("b after declaration (var):", b); // 20
// // ...existing code...

// arr = [1,2,3,4,5,6,7,8,9,10];
// // console.log(arr.filter(x=> x>5));
// // console.log(arr.filter(x=> x>5));
// console.log(arr.reduce((a,b)=> a * b));

// // forEach example: loop through array and print each element
// const fruits = ["apple", "banana", "orange"];
// fruits.forEach((fruit) => {
//   console.log(fruit);
// });
// Output:
// apple
// banana
// orange

// ...existing code...

// String methods examples
// const str = "Hello World";

// // length: get string length
// console.log(str.length); // 11

// // toUpperCase(): convert to uppercase
// console.log(str.toUpperCase()); // HELLO WORLD

// // toLowerCase(): convert to lowercase
// console.log(str.toLowerCase()); // hello world

// // slice(): extract part of string
// console.log(str.slice(0, 5)); // Hello
// console.log(str.slice(6)); // World

// // replace(): replace first occurrence
// console.log(str.replace("World", "JavaScript")); // Hello JavaScript

// // includes(): check if string contains substring
// console.log(str.includes("World")); // true
// console.log(str.includes("Python")); // false


// ...existing code...

// Object methods examples
// const user = { id: 1, name: "Ana", role: "admin" };

// // Object.keys(): get all property names
// console.log(Object.keys(user)); // ["id", "name", "role"]

// // Object.values(): get all property values
// console.log(Object.values(user)); // [1, "Ana", "admin"]

// // Object.entries(): get key-value pairs as arrays
// console.log(Object.entries(user)); // [["id", 1], ["name", "Ana"], ["role", "admin"]]

// // Loop through entries
// Object.entries(user).forEach(([key, value]) => {
//   console.log(`${key}: ${value}`);
// });
// Output:
// id: 1
// name: Ana
// role: admin

// function add(a, b) {
//     a = 10
//     b = 5
//     return a + b
// }
// console.log(add())

// a = 11
// b = 5
// const addz = (a, b) => a + b;
// console.log(addz(a,b))

// ...existing code...

// DOM class manipulation examples
const element = document.querySelector(".box");

// add(): add a class to element
element.classList.add("active");
element.classList.add("highlight", "visible"); // add multiple classes

// remove(): remove a class from element
element.classList.remove("active");
element.classList.remove("highlight", "visible"); // remove multiple classes

// toggle(): add class if not present, remove if present
element.classList.toggle("active"); // adds if missing, removes if present
element.classList.toggle("disabled"); // toggles on each call