var a = 1;
var numbers = document.querySelectorAll('.number')
numbers.forEach((e)=>{
    e.textContent = `Order-${a}`;
    a++;
})