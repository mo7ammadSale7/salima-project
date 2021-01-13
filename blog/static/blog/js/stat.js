// <!-- =====================
//         start input show in scroll 250
//  ====================== -->

$(document).scroll(function(){
    // console.log(window.scrollY)
    if(window.scrollY > 250){
        $('.serch').show(5000);
    }1000;
});



// <!-- =====================
//         start input show placeholder or hiden when on click
//  ====================== -->


// <!-- =====================
//         start input in footer show placeholder or hiden when on click
//  ====================== -->
// let myinpu = document.getElementById('myinpu');
// myinpu.onfocus = function (){
//     'use strict';
//     this.setAttribute('data-place', this.getAttribute('placeholder'));
//     this.setAttribute('placeholder', '')
// };
// myinpu.onblur = function (){
//     'use strict';
//     this.setAttribute('placeholder', this.getAttribute('data-place'));
//     this.setAttribute('data-place', '')
// }

// <!-- =====================
//         start card1 image show in scroll 250
//  ====================== -->
$(document).scroll(function(){
    // console.log(window.scrollY)
    if(window.scrollY > 650){
        $('.cart').show(1000);
        setTimeout(() => {
        $('.cart1').show(1000);
        }, 1000);
    }
});


// <!-- =====================
//         start up page
//  ====================== -->

let mybtn = document.getElementById('goup');
     window.onscroll = function () {
         'us strict'

         if (window.pageYOffset >= 400){
         mybtn.style.display = 'block';
       
         }else{
            mybtn.style.display = 'none';

         }};

mybtn.onclick = function (){
    'user strict';
    window.scrollTo(0,0);
};
     

