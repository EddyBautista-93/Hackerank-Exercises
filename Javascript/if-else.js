//es6 and tenerary operator best practice
const weird = (n) => (n % 2 == 1 || n >= 6 && n <= 20 ? "Weird" : "Not wierd" )

console.log(weird(24));
console.log(weird(7));