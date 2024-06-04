details = document.querySelectorAll('.Details')
details.forEach((item) => {
    var userid = item.dataset.userid
    var product_name = item.dataset.name
    var url = "http://127.0.0.1:8000/product/json/"
    var pk = -1
    fetch(url)
    .then((response) => {
        return response.json()
    })
    .then(data => {
        // console.log(data)
        data.forEach(item => {
            if(item.name == product_name){
                pk = item.id
            }
        })
    })
    item.addEventListener('click', () => {
        window.location.href = `http://127.0.0.1:8000/category/${userid}/${pk}`
    })
})