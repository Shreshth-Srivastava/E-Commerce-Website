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
