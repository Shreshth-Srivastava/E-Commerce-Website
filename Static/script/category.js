wishlist = document.querySelectorAll('#Wishlist');
wishlist.forEach((item) => {
    var url1 = item.dataset.url1
    var url2 = "removefromwishlist_category"
    var product_name = item.dataset.product_name
    var url = "http://127.0.0.1:8000/wishlist/json/"
    var category = item.dataset.category
    var pk = -1
    var flag = false
    // console.log(`url1: http://127.0.0.1:8000/${url1}`)
    // console.log(`url2: http://127.0.0.1:8000/${url2}`)
    fetch(url)
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            // console.log(data)
            data.forEach(item => {
                if(product_name == item.name){
                    pk = item.id
                    flag = true
                }
            });
            if(flag){
                item.style.backgroundColor = "hsl(350, 100%, 75%)";
                item.style.color = "white";
            }
        })
    item.addEventListener('click',()=>{
        if(!flag){
            window.location.href = `http://127.0.0.1:8000/${url1}`
        }
        else{
            window.location.href = `http://127.0.0.1:8000/${url2}/${pk}/${category}/`
        }
    })
});
