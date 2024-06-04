var category = document.querySelector('.categorybtn');
var categoryList = document.querySelector('.categoryList');
var arrow = document.querySelector('#arrow');
var flag = 0;
category.addEventListener('click',()=>{
    if(!flag){
        // categoryList.classList.toggle('hidden');
        categoryList.style.opacity = '1';
        categoryList.style.height = '10rem';
        arrow.style.transform = 'rotateX(180deg)';
        // categoryList.style.transform = 'translateY(0)';
        flag = 1;
    }
    else{
        categoryList.style.opacity = '0';
        categoryList.style.height = '0';
        arrow.style.transform = 'rotateX(0)';
        // categoryList.style.transform = 'translateY(-150%)';
        flag = 0;
    }
})

let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
// function currentSlide(n) {
//   showSlides(slideIndex = n);
// }

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("banner");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}

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
