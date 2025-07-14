const mainNav = document.getElementById('mainNav')
const image = document.getElementsByTagName('img')[0]

document.addEventListener('scroll', function(){
    if(document.documentElement.scrollTop > 0){
      
        image.style.height = '64px'
        mainNav.classList.add('bg-black')
        mainNav.classList.add('txt-white')
    }else{
        image.style.height = '84px'
        mainNav.classList.remove('bg-black')
        mainNav.classList.remove('txt-white')
    }
})