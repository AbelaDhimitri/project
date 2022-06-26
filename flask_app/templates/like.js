var counter = 5;
var counterElement = document.querySelector ("#counter");
console.log (counterElement);

function add1(){
    counter ++;
    counterElement.innerText = counter + "like(s)";
    console.log(counter);

}