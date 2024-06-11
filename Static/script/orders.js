var root_path = window.location.host;
var url = `http://${root_path}/orders/json/`;
var count;
fetch(url)
    .then((response) => {
        return response.json()
    })
    .then(data => {
        count = data.length - 1;
        var numbers = document.querySelectorAll('.number')
        numbers.forEach((e)=>{
            e.textContent = `Order-${count}`;
            count--;
        })
    })