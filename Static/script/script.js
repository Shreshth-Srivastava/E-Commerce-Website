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

var Acc = document.querySelector('.Acc');
var Acc_list = document.querySelector('.Acc_list');
var acc_arrow = document.querySelector('#acc_arrow');
var acc_flag = 0;
Acc.addEventListener('click',()=>{
    if(!acc_flag){
        // categoryList.classList.toggle('hidden');
        Acc_list.style.opacity = '1';
        Acc_list.style.height = '4rem';
        acc_arrow.style.transform = 'rotateX(180deg)';
        // categoryList.style.transform = 'translateY(0)';
        acc_flag = 1;
    }
    else{
        Acc_list.style.opacity = '0';
        Acc_list.style.height = '0';
        acc_arrow.style.transform = 'rotateX(0)';
        // categoryList.style.transform = 'translateY(-150%)';
        acc_flag = 0;
    }
})
